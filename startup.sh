#!/bin/bash
# -*- mode: shell-script -*-

set -eu  # <= 0以外が返るものがあったら止まる, 未定義の変数を使おうとしたときに打ち止め

if [ ! -e halide ]; then
    git clone https://github.com/halide/Halide.git halide
fi

cd halide
git fetch
git checkout release_2018_02_15 
cd ..



