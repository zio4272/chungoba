#!/bin/bash
eval `ssh-agent`

git config pull.rebase false

sudo systemctl restart chungoba.service