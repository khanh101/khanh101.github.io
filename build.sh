#!/usr/bin/env bash
mkdir -p build
cd build
make4ht -d ../docs ../src/index.tex
