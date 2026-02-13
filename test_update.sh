#!/bin/bash
set -e

username=$1
hostname=$2

# Fetch from GitHub
git fetch origin || { echo "ERROR: Failed to fetch from the upstream"; exit 1; }

# Check that there are NO unstaged changes
if ! git diff --quiet; then
  echo "ERROR: There are unstaged changes. Please commit or stash them first."
  exit 1
fi

# Rebase on top of the upstream branch
git rebase origin/main || { echo "ERROR: Failed to rebase on top of Upstream"; exit 1; }

# Push to upstream
git push origin main || { echo "ERROR: Failed to push to upstream"; exit 1; }

# Rsync website
rsync -i -r -P --exclude '2025' --timeout=120 -e "ssh -o ServerAliveInterval=60" ./${hostname} ${username}@${hostname}:/home/${username}/