#!/bin/bash

set -euo pipefail

# Enable remote execution
cd "$(dirname "$0")"

# Start virtual environment
source .venv/bin/activate

# Run tests
python -m unittest tests/text_test.py
