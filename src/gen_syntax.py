#! /usr/bin/env python3
""" Generate Vim syntax file for kitty config. """

# To run the script, cd into the repo and run kitty +launch gen_syntax.py.
#
# For debugging, enter the following into the shell to print the output into
# the terminal:
#   kitty +runpy 'from kitty.actions import get_all_actions; actions=sorted(list({a.name for _, act_list in get_all_actions().items() for a in act_list})); print(actions)'
#   kitty +runpy 'from kitty.config import option_names_for_completion; opts=sorted(list(set(option_names_for_completion()))); print(opts)'

import textwrap as tw
from kitty.actions import get_all_actions
from kitty.config import option_names_for_completion

INFILE="kitty.vim.in"
OUTFILE="../syntax/kitty.vim"

if __name__ == "__main__":
    wrapper = tw.TextWrapper(
        initial_indent="  \\ ", subsequent_indent="  \\ ", width=78
    )

    EXTRAS = { "click" } # hard-code some missing keywords...

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

    KITTY_KEYWORDS = "syn keyword kittyKeyword contained\n" + wrapper.fill(
        ALL_OPTIONS
    )
    KITTY_ACTIONS = "syn keyword kittyAction contained\n" + wrapper.fill(
        ALL_ACTIONS
    )

    with open(INFILE, "r", encoding="utf-8") as f:
        infile = f.read()

    updated_file = infile + "\n" + KITTY_KEYWORDS + "\n" + "\n" + KITTY_ACTIONS

    with open(OUTFILE, "w", encoding="utf-8") as f:
        f.writelines(updated_file)
