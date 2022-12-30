#!/bin/bash

[ -z "$1" ] && echo "Give dir name" && exit
dir="$1"
mkdir "$dir" && cd "$dir"
touch a.py b.py input.txt tools.py
tmux
