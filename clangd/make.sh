#!/bin/bash
scram b llvm-ccdb -j 4
if [ -z "$CMSSW_BASE" ]; then
    # echo "Warning: unset cmsenv"
    cmsenv
fi
python3 $CMSSW_BASE/make_compile_commands.py
