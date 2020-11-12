#!/bin/bash
eval `ssh-agent`

git config pull.rebase false

sudo service chungoba start