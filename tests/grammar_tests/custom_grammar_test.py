import unittest

from project_toki.grammar_parser import GrammarParser
from project_toki.phrase import Phrase
from project_toki.phrase_comparer import PhraseComparer


class TestGrammarCustom(unittest.TestCase):
    COMPARER: PhraseComparer = PhraseComparer()

    def test_unknown_words(self):
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("masimelo pona"),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    └── NOUN_PHRASE",
                    '        ├── NOUN: "masimelo"',
                    "        └── ADJECTIVE_PHRASE",
                    '            └── ADJECTIVE: "pona"',
                ],
            ),
        )

    def test_punctuation(self):
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("mi, sina, ona."),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    ├── ADJECTIVE_PHRASE",
                    '    │   └── ADJECTIVE: "mi"',
                    "    ├── ,",
                    "    ├── ADJECTIVE_PHRASE",
                    '    │   └── ADJECTIVE: "sina"',
                    "    ├── ,",
                    "    ├── ADJECTIVE_PHRASE",
                    '    │   └── ADJECTIVE: "ona"',
                    "    └── .",
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("kala - moku"),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    ├── ADJECTIVE_PHRASE",
                    '    │   └── ADJECTIVE: "kala"',
                    "    ├── -",
                    "    └── ADJECTIVE_PHRASE",
                    '        └── ADJECTIVE: "moku"',
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("wile? wile!"),
            Phrase.from_lines(
                [
                    "TEXT",
                    "├── SENTENCE",
                    "│   ├── ADJECTIVE_PHRASE",
                    '│   │   └── ADJECTIVE: "wile"',
                    "│   └── ?",
                    "└── SENTENCE",
                    "    ├── ADJECTIVE_PHRASE",
                    '    │   └── ADJECTIVE: "wile"',
                    "    └── !",
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("sina... awen"),
            Phrase.from_lines(
                [
                    "TEXT",
                    "├── SENTENCE",
                    "│   ├── ADJECTIVE_PHRASE",
                    '│   │   └── ADJECTIVE: "sina"',
                    "│   └── ...",
                    "└── SENTENCE",
                    "    └── ADJECTIVE_PHRASE",
                    '        └── ADJECTIVE: "awen"',
                ],
            ),
        )
