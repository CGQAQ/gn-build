# how-to-gn

## Official refrence
- [The reference](https://gn.googlesource.com/gn/+/main/docs/reference.md)
- [The repo](https://gn.googlesource.com/gn/)

## prerequisites
- python3

## HOWTO
```console
git clone --recurse-submodules git@github.com:CGQAQ/how-to-gn.git
# git clone --recurse-submodules https://github.com/CGQAQ/how-to-gn.git
cd how-to-gn
# build ninja & gn
python3 build-tools.py
# run gn
python3 gn.py gnargs...
```