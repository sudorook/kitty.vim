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

if __name__ == "__main__":
    # Set and check inputs.
    if os.path.exists(sys.argv[1]):
        INFILE = sys.argv[1]
    if sys.argv[2]:
        OUTFILE = sys.argv[2]

    # Instantiate text wrapper object.
    wrapper = tw.TextWrapper(
        initial_indent="  \\ ", subsequent_indent="  \\ ", width=78
    )

    # 'Click' keyword is missing from kitty actions list as of 0.24.0, so add
    # it manually.
    EXTRAS = {"click"}

    # Get all kitty actions and options and convert to list.
    ALL_OPTIONS = " ".join(option_names_for_completion())
    ALL_ACTIONS = " ".join(
        sorted(
            list(
                {
                    a.name
                    for _, act_list in get_all_actions().items()
                    for a in act_list
                }.union(EXTRAS)
            )
        )
    )

    # Generate text blocks to write to file.
    KITTY_KEYWORDS = "syn keyword kittyKeyword contained\n" + wrapper.fill(
        ALL_OPTIONS
    )
    KITTY_ACTIONS = "syn keyword kittyAction contained\n" + wrapper.fill(
        ALL_ACTIONS
    )

    with open(INFILE, "r", encoding="utf-8") as f:
        infile = f.read()
        updated_text = infile + "\n" + KITTY_KEYWORDS + "\n\n" + KITTY_ACTIONS

    with open(OUTFILE, "w", encoding="utf-8") as f:
        f.writelines(updated_text)
