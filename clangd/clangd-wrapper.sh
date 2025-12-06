#!/usr/bin/env bash
# Example wrapper for clangd

# Load your environment (adapt this line!)
cd <absolutePathTo_$CMSSWBASE>/src
cmsenv 2>&1

# Optionally print for debugging
# env | grep -E "LD_LIBRARY_PATH|INCLUDE"

# Execute clangd with all passed arguments
exec clangd "$@"
