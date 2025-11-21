#!/bin/bash

set -euo pipefail

# Enable remote execution
cd "$(dirname "$0")"

# Start virtual environment
source .venv/bin/activate

# Run tests
coverage run -m unittest tests/text_test.py

# Create coverage report
coverage xml
