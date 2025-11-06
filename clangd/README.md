# Clangd for cmssw-developing
Working with CMSSW could be difficult and any benefits from using language server integrations in vscode are very useful.

If you are developing a new module, the `compile_commands.json` of the CMSSW release shall be updated with the updated/new entries with the content of your `$CMSSW_BASE/src`.

This can be done by generating the llvm compile comands, using the target `scram b llvm-ccdb -j 4`, which makes a `compile_commands.json` file for the content of your src.

These commands shall be appended to the full list of compile commands, that are found in the `$CMSSW_RELEASE_BASE`.

To do so, a `make_compile_commands.py` script takes the 'local' compile commands of your area and merges with those of the release, by updating when necessary the references already existing with those from your area.

## Install
- copy `make_compile_commands.py` in `$CMSSW_BASE`
- copy `make.sh` in `$CMSSW_BASE/src`
- set the following in the clangd setting in vscode (Ctrl+P -> Preferences: Open Remote Settings (JSON) -i.e., remote if your are using Remote-SSH)
- get the absolute path `AREAPATH` to area (i.e. `/eos/home-X/XXXX/<somepath>/CMSSW_15_1_0_patch1`), and replace in copy the following setting
```json
    "clangd.arguments": [
        "--limit-references=100",
        "--header-insertion=never",
        "--limit-results=20",
        "-j=1",
        "--background-index=false",
        "--pch-storage=memory",
        "--compile-commands-dir=<AREAPATH>"
    ],
```
The argument `-j=1` determines how many threads clangd indexer uses.
The `--background-index` avoids background usage of your resources for indexing.
The `--limit-*` avoids large memory usage

## Usage
- `cd $CMSSW_BASE/src && ./make.sh`


## Troubleshoot
If your environment has not `clangd`, you can use the one that is loaded with the cmssw area. For this
- copy `clangd-wrapper.sh` into `$CMSSW_BASE`
- set in the clangd settings in vscode the path for the launcher (replace `<AREAPATH>` with the content of `$CMSSW_BASE`)
```json
    "clangd.path": "<AREAPATH>/clangd-wrapper.sh",
```