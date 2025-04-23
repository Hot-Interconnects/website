#!/bin/bash

username=$1
hostname=$2

rsync -i -r ./${hostname} ${username}@${hostname}:/home/${username}/

