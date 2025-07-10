#!/bin/sh

tmux kill-server

cd PE-Portfolio-Website

git fetch

git reset origin/main --hard

source python3-virtualenv/bin/activate

pip install -r requirements.txt

tmux new-session -d "exec flask run --host=0.0.0.0"