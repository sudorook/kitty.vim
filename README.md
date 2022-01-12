# kitty.vim

Vim syntax files for kitty session and config files.

To install, extract the contents into your Vim directory, or clone the repo
into the `.vim/pack/dist/start` subdirectory.

To rebuild the 'kitty.vim' file, run:
```
cd src/
kitty +launch ./gen_syntax.py
```

The script will overwrite the file in `syntax/kitty.vim`.
