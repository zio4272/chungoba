#!/bin/bash
eval `ssh-agent`

git config pull.rebase false

git pull