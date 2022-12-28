#!/bin/bash

[ -z "$1" ] && echo "Give dir name" && exit
dir="$1"
mkdir "$dir" && cd "$dir"
touch run.py input.txt
tmux
