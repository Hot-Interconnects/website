#!/bin/bash

# Build the 2026 site (output to hoti.org/2026 as per _config.yml)
chruby ruby-3.3.5
bundle exec jekyll build

# Copy the 2025 archive into the deployment directory
# Note: _config.yml sets destination to hoti.org/2026, so hoti.org is the parent.
# But Jekyll might clean the destination or parent?
# Jekyll cleans `destination`. It does NOT clean the parent directories unless they are inside destination.
# So `hoti.org/2026` is cleaned. `hoti.org/2025` should be safe if it exists, or we create it.

# Ensure 2025 exists in the deployment folder
mkdir -p hoti.org/2025
cp -r 2025/* hoti.org/2025/

# Copy the root redirect
cp root_index.html hoti.org/index.html

echo "Build complete. Content layout:"
ls -F hoti.org/
