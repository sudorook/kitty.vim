# kitty.vim

Vim syntax files for kitty session and config files.

To install, extract the contents into your Vim directory, or clone the repo
into the `.vim/pack/dist/start` subdirectory.

To rebuild the 'kitty.vim' file, run:
```
./build
```

The `build` script is a wrapper around `src/gen_syntax.py` and will overwrite
the file in `syntax/kitty.vim`.
