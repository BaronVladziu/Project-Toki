#!/bin/bash

set -euo pipefail

# Enable remote execution
cd "$(dirname "$0")"

# Start virtual environment
source .venv/bin/activate

# Run tests
coverage run -m pytest tests/*

# Create coverage report
coverage xml
