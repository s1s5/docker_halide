#!/bin/bash
# -*- mode: shell-script -*-

set -eu  # <= 0以外が返るものがあったら止まる, 未定義の変数を使おうとしたときに打ち止め


docker tag s1s5/llvm:50 halide-base
docker build -f Dockerfile -t s1s5/halide .
