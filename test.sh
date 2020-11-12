#!/bin/bash
eval `ssh-agent`

ssh-add ~/.ssh/id_rsa.pub

git config pull.rebase false

sudo systemctl restart chungoba