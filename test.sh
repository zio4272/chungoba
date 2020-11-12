#!/bin/bash
eval `ssh-agent`

ssh-add ~/.ssh/id_rsa.pub

cd /home/ubuntu/chungoba

git pull origin master
sudo systemctl restart chungoba