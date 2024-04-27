# cmssw_vscode
Recipies to develop CMSSW using VSCode

## Indexing files
Indexing files allows VSCode to easily resolve references to imported files.

### C++
Indexing C++ files is based on the *clangd* extension alongside a *compile-commands.json* file.
1. Install clangd.
    1. In VSCode in the side bar go to *Extensions*.
    2. In the search bar type **clangd**.
    3. Click *Install*.
    4. Click *Install in SSH: lxplus.cern.ch*.
    5. Disable IntelliSense if you have to installed (comes with the C/C++ Microsoft extension).
        1. In VSCode go to *File -> Settings -> Remote [SSH: lxplus.cern.ch]*.
        2. In the search bar type **C_Cpp.intelliSenseEngine**.
        3. Switch to *disabled*.
2. Point *clangd* to the *compile_commands.json* file. A couple of options exist:
    - Add the directory with the file to the clangd settings:
        1. Go to *File -> Settings -> Remote [SSH: lxplus.cern.ch]*
        2. In the search bar type **clangd.arguments**.
        3. Add a new argument: `--compile-commands-dir=<path-to-cvmfs-repo>`. For instance: `--compile-commands-dir=/cvmfs/cms.cern.ch/el9_amd64_gcc12/cms/cmssw/CMSSW_14_0_2`.
    - Create a symbolic link to the file: in your terminal execute `ln -s <path-to-cvmfs-repo> <path-to-your-repo>`. For instance: `ln -s /cvmfs/cms.cern.ch/el9_amd64_gcc12/cms/cmssw/CMSSW_14_0_2/compile_commands.json /afs/cern.ch/user/t/tostafin/scratch1/CMSSW_14_0_2`.
    - Copy the file: in your terminal execute `cp <path-to-cvmfs-repo> <path-to-your-repo>`. For instance: `cp /cvmfs/cms.cern.ch/el9_amd64_gcc12/cms/cmssw/CMSSW_14_0_2/compile_commands.json /afs/cern.ch/user/t/tostafin/scratch1/CMSSW_14_0_2`.
3. Restart the clangd server. Press Ctrl + Shift + P, type **clangd: Restart language server** and execute it.
