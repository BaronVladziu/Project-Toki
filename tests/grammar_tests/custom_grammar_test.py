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
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("nimi sona: sina sona"),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    ├── NOUN_PHRASE",
                    '    │   ├── NOUN: "nimi"',
                    "    │   └── ADJECTIVE_PHRASE",
                    '    │       └── ADJECTIVE: "sona"',
                    "    ├── :",
                    "    ├── NOUN_PHRASE",
                    '    │   └── NOUN: "sina"',
                    "    └── VERB_PHRASE",
                    "        └── ADJECTIVE_PHRASE",
                    '            └── ADJECTIVE: "sona"',
                ],
            ),
        )

    def test_difficult(self):
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("jan ale li wile kama e jan ike mi"),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    ├── NOUN_PHRASE",
                    '    │   ├── NOUN: "jan"',
                    "    │   └── ADJECTIVE_PHRASE",
                    '    │       └── ADJECTIVE: "ale"',
                    '    ├── PARTICLE: "li"',
                    "    └── VERB_PHRASE",
                    '        ├── PREVERB: "wile"',
                    '        ├── VERB: "kama"',
                    '        ├── PARTICLE: "e"',
                    "        └── NOUN_PHRASE",
                    '            ├── NOUN: "jan"',
                    "            └── ADJECTIVE_PHRASE",
                    '                ├── ADJECTIVE: "ike"',
                    '                └── ADJECTIVE: "mi"',
                ],
            ),
        )

    def test_numbers(self):
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("li nanpa tu ala tu"),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    '    ├── PARTICLE: "li"',
                    "    └── VERB_PHRASE",
                    "        └── NUMBER_PHRASE",
                    '            ├── NOUN: "nanpa"',
                    '            ├── NUMBER: "tu"',
                    '            ├── PARTICLE: "ala"',
                    '            └── NUMBER: "tu"',
                ],
            ),
        )

    def test_short(self):
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("a!"),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    '    ├── PARTICLE: "a"',
                    "    └── !",
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("jan pona lon awen"),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    ├── NOUN_PHRASE",
                    '    │   ├── NOUN: "jan"',
                    "    │   └── ADJECTIVE_PHRASE",
                    '    │       └── ADJECTIVE: "pona"',
                    "    └── PREPOSITION_PHRASE",
                    '        ├── PREPOSITION: "lon"',
                    "        └── NOUN_PHRASE",
                    '            └── NOUN: "awen"',
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("a mute"),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    '    ├── PARTICLE: "a"',
                    "    └── NUMBER_PHRASE",
                    '        └── NUMBER: "mute"',
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("li sona"),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    '    ├── PARTICLE: "li"',
                    "    └── VERB_PHRASE",
                    "        └── ADJECTIVE_PHRASE",
                    '            └── ADJECTIVE: "sona"',
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("li pana e pan"),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    '    ├── PARTICLE: "li"',
                    "    └── VERB_PHRASE",
                    '        ├── VERB: "pana"',
                    '        ├── PARTICLE: "e"',
                    "        └── NOUN_PHRASE",
                    '            └── NOUN: "pan"',
                ],
            ),
        )
