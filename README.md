# gn-build
Build the latest & greatest `GN-build-system` and `ninja` from source, and give you the wrapper to call it

## Official refrence
- [The reference](https://gn.googlesource.com/gn/+/main/docs/reference.md)
- [The repo](https://gn.googlesource.com/gn/)
- [The presentation](https://docs.google.com/presentation/d/15Zwb53JcncHfEwHpnG_PoIbbzQ3GQi_cpujYwbpcbZo/edit)

## prerequisites
- python3

## HOWTO
```console
git clone --recurse-submodules git@github.com:CGQAQ/gn-build.git
# git clone --recurse-submodules https://github.com/CGQAQ/gn-build.git

# On Windows
# run gn
python gn.py ...gnargs
# run ninja
python ninja.py ...ninjaargs

# On nonWindows
# run gn
python3 gn.py ...gnargs
# run ninja
python3 ninja.py ...ninjaargs
# ------------- OR ---------------
chmod +x ./gn.py ./ninja.py
# run gn
./gn.py ...gnargs
# run ninja
./ninja.py ...ninjaarg
```
