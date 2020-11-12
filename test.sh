#!/bin/bash
eval `ssh-agent`

git config pull.rebase false

sudo systemctl start chungoba.service
sudo systemctl enable chungoba.service