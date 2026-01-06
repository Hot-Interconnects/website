#!/bin/bash

username=$1
hostname=$2

rsync -i -r ./${hostname} ${username}@${hostname}:/home/${username}/

git add *
git commit -m "Archive 2025"
git push origin main