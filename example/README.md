# Complile & Run
```console
python ..\gn.py gen out
python ..\ninja.py -C out
.\out\hello_world.exe
```

## NOTE
if you are not on windows with msvc, you shoud modify the `BUILDCONFIG.gn` file, and change `set_default_toolchain("//toolchains/gcc")` to `set_default_toolchain("//toolchains/gcc")` OR `set_default_toolchain("//toolchains/clang")` respectively