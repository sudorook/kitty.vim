# kitty.vim

Vim syntax files for kitty session and config files.

## Install

To install, you can clone this repository to your Vim dot-directory as a
plugin, or your can run the `./install` script.

If you use the latter option, you can uninstall this plugin by using the
`./uninstall` script.

## Update

To update the syntax file using a new version of `kitty`, use the `build`
script to rebuild the 'kitty.vim' file:
```
./build
```

The `build` script is a wrapper around `src/gen_syntax.py` and will overwrite
the file in `syntax/kitty.vim`.

Then, re-install this plugin to copy the updated syntax rules to your Vim
setup.
