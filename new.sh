#!/bin/bash

[ -z "$1" ] && echo "Give dir name" && exit
dir="$1"
mkdir "$dir" && cd "$dir"
touch first.py second.py input.txt tools.py
tmux
