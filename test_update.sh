#!/bin/bash

username=$1
hostname=$2

rsync -i -r -P --exclude '2025' --timeout=120 -e "ssh -o ServerAliveInterval=60" ./${hostname} ${username}@${hostname}:/home/${username}/

# git add -A
# git commit -m "Update 2026 website"
# git push origin main