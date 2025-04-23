#!/bin/bash

username=$1
hostname=$2
LOCAL_DIR=$3

rsync -i -r ${LOCAL_DIR} ${username}@${hostname}:/home/${username}/

