#! /usr/bin/env python3
""" Generate Vim syntax file for kitty config. """

# To run the script, cd into the repo and run kitty +launch gen_syntax.py.
#
# For debugging, enter the following into the shell to print the output into
# the terminal:
#   kitty +runpy 'from kitty.actions import get_all_actions; actions=sorted(list({a.name for _, act_list in get_all_actions().items() for a in act_list})); print(actions)'
#   kitty +runpy 'from kitty.config import option_names_for_completion; opts=sorted(list(set(option_names_for_completion()))); print(opts)'

import sys
import os
import textwrap as tw
from kitty.actions import get_all_actions
from kitty.config import option_names_for_completion
from kitty.constants import version
from kitty.options import utils

if __name__ == "__main__":
    # Set and check inputs.
    if os.path.exists(sys.argv[1]):
        INFILE = sys.argv[1]
    else:
        sys.stderr.write(
            "Input '" + sys.argv[1] + "' does not exist. Exiting."
        )
        sys.exit(3)
    if sys.argv[2]:
        OUTFILE = sys.argv[2]
    else:
        sys.stderr.write("No output file given. Exiting.")
        sys.exit(3)

    # Instantiate text wrapper object.
    WRAPPER = tw.TextWrapper(
        initial_indent="  \\ ", subsequent_indent="  \\ ", width=78
    )

    # Get all kitty actions and options and convert to list.
    ALL_MODS = " ".join(
        sorted(
            [
                item.lower()
                for item in set(utils.mod_map.keys()).union(
                    set(utils.mod_map.values())
                )
            ]
        )
    )
    ALL_OPTIONS = " ".join(option_names_for_completion())
    ALL_ACTIONS = " ".join(
        sorted(
            list(
                {
                    a.name
                    for _, act_list in get_all_actions().items()
                    for a in act_list
                }.union(utils.mouse_trigger_count_map.keys())
            )
        )
    )

    KITTY_VERSION = (
        str(version.major)
        + "."
        + str(version.minor)
        + "."
        + str(version.patch)
    )

    # Generate text blocks to write to file.
    KITTY_MODS = "syn keyword kittyMod contained\n" + WRAPPER.fill(ALL_MODS)
    KITTY_KEYWORDS = "syn keyword kittyKeyword contained\n" + WRAPPER.fill(
        ALL_OPTIONS
    )
    KITTY_ACTIONS = "syn keyword kittyAction contained\n" + WRAPPER.fill(
        ALL_ACTIONS
    )

    with open(INFILE, "r", encoding="utf-8") as f:
        TEXT = f.read()

    TEXT = TEXT.replace("@VERSION@", KITTY_VERSION)
    TEXT = (
        TEXT
        + "\n"
        + KITTY_MODS
        + "\n\n"
        + KITTY_KEYWORDS
        + "\n\n"
        + KITTY_ACTIONS
        + "\n"
    )

    with open(OUTFILE, "w", encoding="utf-8") as f:
        f.writelines(TEXT)
