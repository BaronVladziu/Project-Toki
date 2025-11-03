#!/bin/bash

set -euo pipefail

# Enable remote execution
cd "$(dirname "$0")"

# Create virtual environment
python3.14 -m venv .venv
# shellcheck disable=SC1091
source .venv/bin/activate

# Upgrade pip
pip3 install pip --upgrade

# Install repository
pip3 install -e . --no-cache-dir

echo "VIRTUALENV INSTALLED SUCCESSFULLY!"
