#!/bin/bash

set -euo pipefail

# Enable remote execution
cd "$(dirname "$0")"

# Start virtual environment
source .venv/bin/activate

# Run tests
coverage run -m unittest tests/dictionary_test.py
coverage run -m unittest tests/word_test.py
coverage run -m unittest tests/punctuation_test.py
coverage run -m unittest tests/phrase_test.py
coverage run -m unittest tests/grammar_tests/pu_lessons_grammar_test.py
coverage run -m unittest tests/grammar_tests/custom_grammar_test.py
coverage run -m unittest tests/text_test.py

# Create coverage report
coverage xml
