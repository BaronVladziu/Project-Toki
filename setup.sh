#!/bin/bash

set -euo pipefail

# Enable remote execution
cd "$(dirname "$0")"

# Create virtual environment
python3.14 -m venv .venv
source .venv/bin/activate

# Upgrade pip
pip3 install pip --upgrade

# Install repository
pip3 install -e . --no-cache-dir

# Install other requirements
pip3 install coverage==7.11.3

# Build pre-commit
pre-commit install --config=".pre-commit-config.yaml"
pre-commit run --all-files --config=".pre-commit-config.yaml"

echo "VIRTUALENV INSTALLED SUCCESSFULLY!"
