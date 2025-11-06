#!/bin/bash
scram b llvm-ccdb -j 4
python3 $CMSSW_BASE/make_compile_commands.py
#scram b -j 16
