#!/bin/bash
set -e

username=$1
hostname=$2

# Fetch from GitHub
git fetch origin || echo "Failed to fetch from the upstream"

# Check that there are NO unstaged changes
if ! git diff --quiet; then
  echo "ERROR: There are unstaged changes. Please commit or stash them first."
  exit 1
fi

# Rebase on top of the upstream branch
git rebase origin/main || echo "Failed to rebase on top of Upstream"

# Push to upstream
git push origin main

# Rsync website
rsync -i -r -P --exclude '2025' --timeout=120 -e "ssh -o ServerAliveInterval=60" ./${hostname} ${username}@${hostname}:/home/${username}/