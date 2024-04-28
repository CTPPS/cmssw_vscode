# cmssw_vscode
Recipies to develop CMSSW using VSCode

## Indexing files
Indexing files allows VSCode to easily resolve references to imported files. This provides:
- go to definition

    ![Go to definition](./static/go_to_def.gif "Go to definition")

- find references

    ![Find references](./static/find_references.gif "Find references")

- errors and warnings detection

    ![Errors and warnings detection](./static/errors_and_warnings.gif "Errors and warnings detection")

More details and features in the [VSCode](https://code.visualstudio.com/docs/editor/editingevolved#_go-to-definition) and [clangd](https://clangd.llvm.org/features) documentations.

### C++
Indexing C++ files is based on the *clangd* extension alongside a *compile-commands.json* file.
1. Install clangd.
    1. In VSCode in the side bar go to *Extensions*.
    2. In the search bar type **clangd**.
    3. Click *Install*.
    4. Click *Install in SSH: lxplus.cern.ch*.
    5. Disable IntelliSense if you have to installed (comes with the C/C++ Microsoft extension).
        1. In VSCode press Ctrl + Shift + P, type **Preferences: Open Settings (UI)** and click Enter.
        2. Switch to *Remote [SSH: lxplus.cern.ch]*.
        3. In the search bar type **C_Cpp.intelliSenseEngine**.
        4. Switch to *disabled*.
2. Initialize your CMSSW release environment: execute `cmsenv` in the *src* subdirectory of your CMSSW repo. This will add two additional environment variables:
    - `CMSSW_RELEASE_BASE`: path to the CMSSW repo on the CVMFS shared network file system.
    - `CMSSW_BASE`: path to your locally cloned CMSSW repo.
3. Point clangd to the *compile_commands.json* file. VSCode will look for it on the `CMSSW_BASE` path, regardless which subdirectory you open. A couple of options exist:
    - Add the directory with the file to the clangd settings:
        1. In VSCode press Ctrl + Shift + P, type **Preferences: Open Settings (UI)** and click Enter.
        2. Switch to *Remote [SSH: lxplus.cern.ch]*.
        3. In the search bar type **clangd.arguments**.
        4. Add a new argument: `--compile-commands-dir=${env:CMSSW_RELEASE_BASE}`.
    - Create a symbolic link to the file: in your terminal with the environment set up execute `ln -s $CMSSW_RELEASE_BASE/compile_commands.json $CMSSW_BASE`.
    - Copy the file: in your terminal with the environment set up execute `cp $CMSSW_RELEASE_BASE/compile_commands.json $CMSSW_BASE`.
4. Restart the clangd server. Press Ctrl + Shift + P, type **clangd: Restart language server** and click Enter.
