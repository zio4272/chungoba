#!/bin/bash
eval `ssh-agent`

ssh-add ~/.ssh/id_rsa.pub

git pull origin master
sudo systemctl restart chungoba