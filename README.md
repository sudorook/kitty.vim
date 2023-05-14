# kitty.vim

Vim syntax files for kitty session and config files.

## Install

To install, you can 1) clone this repository to your Vim dot-directory as a
plugin, or 2) run the `./install` script.

If you use the latter option, you can uninstall this plugin by running the
`./uninstall` script.

## Update

This repository will be kept up-to-date with new kitty releases, so if you
installed the syntax rules as a Vim plugin, simply update the plugin (i.e.
`git pull` the changes).

Otherwise, to update the syntax file, run the `build` script. `build` is a
wrapper around `src/gen_syntax.py` that will overwrite `syntax/kitty.vim`. Then,
re-install by running `./install`.
