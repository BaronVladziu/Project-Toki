#!/usr/bin/env python3

import argparse

from project_toki.grammar_parser import GrammarParser


def parser():
    parser = argparse.ArgumentParser(
        description="Produces an analysis on an input text",
    )
    parser.add_argument(
        "-i",
        "--input_text",
        action="store",
        help="Input text in Toki Pona.",
        required=True,
        type=str,
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parser()
    print(
        GrammarParser.parse_text(
            text=args.input_text,
        ),
    )
