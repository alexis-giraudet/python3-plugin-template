# python3-plugin-template

# Debian package

## Build using mkosi

First, build `python3-plugin-template` Debian package and put the generated .deb into the ./mkosi.packages/ folder.

Build debian package (output to ./mkosi.builddir/ folder):

```sh
mkosi build
# Build debug:
mkosi build -- -d
```

# References
 - [setuptools - Entry Points for Plugins](https://setuptools.pypa.io/en/latest/userguide/entry_point.html#entry-points-for-plugins)
