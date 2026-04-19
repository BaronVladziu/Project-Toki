import unittest

from project_toki.grammar_parser import GrammarParser
from project_toki.phrase import Phrase
from project_toki.phrase_comparer import PhraseComparer


class TestGrammarPuLessons(unittest.TestCase):
    COMPARER: PhraseComparer = PhraseComparer()

    def test_lesson_1(self):
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("jelo"),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    └── ADJECTIVE_PHRASE",
                    '        └── ADJECTIVE: "jelo"',
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("toki"),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    └── ADJECTIVE_PHRASE",
                    '        └── ADJECTIVE: "toki"',
                ],
            ),
        )

    def test_lesson_2(self):
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("ijo li ijo."),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    ├── NOUN_PHRASE",
                    '    │   └── NOUN: "ijo"',
                    '    ├── PARTICLE: "li"',
                    "    ├── VERB_PHRASE",
                    "    │   └── ADJECTIVE_PHRASE",
                    '    │       └── ADJECTIVE: "ijo"',
                    "    └── .",
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("ni li jan."),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    ├── NOUN_PHRASE",
                    '    │   └── NOUN: "ni"',
                    '    ├── PARTICLE: "li"',
                    "    ├── VERB_PHRASE",
                    "    │   └── ADJECTIVE_PHRASE",
                    '    │       └── ADJECTIVE: "jan"',
                    "    └── .",
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("ni li kili."),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    ├── NOUN_PHRASE",
                    '    │   └── NOUN: "ni"',
                    '    ├── PARTICLE: "li"',
                    "    ├── VERB_PHRASE",
                    "    │   └── ADJECTIVE_PHRASE",
                    '    │       └── ADJECTIVE: "kili"',
                    "    └── .",
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("lipu li ijo."),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    ├── NOUN_PHRASE",
                    '    │   └── NOUN: "lipu"',
                    '    ├── PARTICLE: "li"',
                    "    ├── VERB_PHRASE",
                    "    │   └── ADJECTIVE_PHRASE",
                    '    │       └── ADJECTIVE: "ijo"',
                    "    └── .",
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("jan li meli."),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    ├── NOUN_PHRASE",
                    '    │   └── NOUN: "jan"',
                    '    ├── PARTICLE: "li"',
                    "    ├── VERB_PHRASE",
                    "    │   └── ADJECTIVE_PHRASE",
                    '    │       └── ADJECTIVE: "meli"',
                    "    └── .",
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("soweli li ijo."),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    ├── NOUN_PHRASE",
                    '    │   └── NOUN: "soweli"',
                    '    ├── PARTICLE: "li"',
                    "    ├── VERB_PHRASE",
                    "    │   └── ADJECTIVE_PHRASE",
                    '    │       └── ADJECTIVE: "ijo"',
                    "    └── .",
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("meli li jan."),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    ├── NOUN_PHRASE",
                    '    │   └── NOUN: "meli"',
                    '    ├── PARTICLE: "li"',
                    "    ├── VERB_PHRASE",
                    "    │   └── ADJECTIVE_PHRASE",
                    '    │       └── ADJECTIVE: "jan"',
                    "    └── .",
                ],
            ),
        )

    def test_lesson_3(self):
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("ijo li pona."),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    ├── NOUN_PHRASE",
                    '    │   └── NOUN: "ijo"',
                    '    ├── PARTICLE: "li"',
                    "    ├── VERB_PHRASE",
                    "    │   └── ADJECTIVE_PHRASE",
                    '    │       └── ADJECTIVE: "pona"',
                    "    └── .",
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("tomo suli"),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    └── NOUN_PHRASE",
                    '        ├── NOUN: "tomo"',
                    "        └── ADJECTIVE_PHRASE",
                    '            └── ADJECTIVE: "suli"',
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("jan pona"),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    └── NOUN_PHRASE",
                    '        ├── NOUN: "jan"',
                    "        └── ADJECTIVE_PHRASE",
                    '            └── ADJECTIVE: "pona"',
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("meli lili"),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    └── NOUN_PHRASE",
                    '        ├── NOUN: "meli"',
                    "        └── ADJECTIVE_PHRASE",
                    '            └── ADJECTIVE: "lili"',
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("telo suli"),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    └── NOUN_PHRASE",
                    '        ├── NOUN: "telo"',
                    "        └── ADJECTIVE_PHRASE",
                    '            └── ADJECTIVE: "suli"',
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("lipu soweli"),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    └── NOUN_PHRASE",
                    '        ├── NOUN: "lipu"',
                    "        └── ADJECTIVE_PHRASE",
                    '            └── ADJECTIVE: "soweli"',
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("tomo meli"),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    └── NOUN_PHRASE",
                    '        ├── NOUN: "tomo"',
                    "        └── ADJECTIVE_PHRASE",
                    '            └── ADJECTIVE: "meli"',
                ],
            ),
        )

    def test_lesson_4(self):
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("mi mije."),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    ├── NOUN_PHRASE",
                    '    │   └── NOUN: "mi"',
                    "    ├── VERB_PHRASE",
                    "    │   └── ADJECTIVE_PHRASE",
                    '    │       └── ADJECTIVE: "mije"',
                    "    └── .",
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("sina sin."),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    ├── NOUN_PHRASE",
                    '    │   └── NOUN: "sina"',
                    "    ├── VERB_PHRASE",
                    "    │   └── ADJECTIVE_PHRASE",
                    '    │       └── ADJECTIVE: "sin"',
                    "    └── .",
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("tomo mi"),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    └── NOUN_PHRASE",
                    '        ├── NOUN: "tomo"',
                    "        └── ADJECTIVE_PHRASE",
                    '            └── ADJECTIVE: "mi"',
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("kulupu sina"),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    └── NOUN_PHRASE",
                    '        ├── NOUN: "kulupu"',
                    "        └── ADJECTIVE_PHRASE",
                    '            └── ADJECTIVE: "sina"',
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("tomo sina li sin."),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    ├── NOUN_PHRASE",
                    '    │   ├── NOUN: "tomo"',
                    "    │   └── ADJECTIVE_PHRASE",
                    '    │       └── ADJECTIVE: "sina"',
                    '    ├── PARTICLE: "li"',
                    "    ├── VERB_PHRASE",
                    "    │   └── ADJECTIVE_PHRASE",
                    '    │       └── ADJECTIVE: "sin"',
                    "    └── .",
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("mije li jan pona."),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    ├── NOUN_PHRASE",
                    '    │   └── NOUN: "mije"',
                    '    ├── PARTICLE: "li"',
                    "    ├── VERB_PHRASE",
                    "    │   └── NOUN_PHRASE",
                    '    │       ├── NOUN: "jan"',
                    "    │       └── ADJECTIVE_PHRASE",
                    '    │           └── ADJECTIVE: "pona"',
                    "    └── .",
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("tomo soweli li lili."),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    ├── NOUN_PHRASE",
                    '    │   ├── NOUN: "tomo"',
                    "    │   └── ADJECTIVE_PHRASE",
                    '    │       └── ADJECTIVE: "soweli"',
                    '    ├── PARTICLE: "li"',
                    "    ├── VERB_PHRASE",
                    "    │   └── ADJECTIVE_PHRASE",
                    '    │       └── ADJECTIVE: "lili"',
                    "    └── .",
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("sina mije wawa."),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    ├── NOUN_PHRASE",
                    '    │   └── NOUN: "sina"',
                    "    ├── VERB_PHRASE",
                    "    │   └── NOUN_PHRASE",
                    '    │       ├── NOUN: "mije"',
                    "    │       └── ADJECTIVE_PHRASE",
                    '    │           └── ADJECTIVE: "wawa"',
                    "    └── .",
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("kulupu sin li wawa."),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    ├── NOUN_PHRASE",
                    '    │   ├── NOUN: "kulupu"',
                    "    │   └── ADJECTIVE_PHRASE",
                    '    │       └── ADJECTIVE: "sin"',
                    '    ├── PARTICLE: "li"',
                    "    ├── VERB_PHRASE",
                    "    │   └── ADJECTIVE_PHRASE",
                    '    │       └── ADJECTIVE: "wawa"',
                    "    └── .",
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("ni li lipu sina."),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    ├── NOUN_PHRASE",
                    '    │   └── NOUN: "ni"',
                    '    ├── PARTICLE: "li"',
                    "    ├── VERB_PHRASE",
                    "    │   └── NOUN_PHRASE",
                    '    │       ├── NOUN: "lipu"',
                    "    │       └── ADJECTIVE_PHRASE",
                    '    │           └── ADJECTIVE: "sina"',
                    "    └── .",
                ],
            ),
        )

    def test_lesson_5(self):
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("ijo li pali e ijo."),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    ├── NOUN_PHRASE",
                    '    │   └── NOUN: "ijo"',
                    '    ├── PARTICLE: "li"',
                    "    ├── VERB_PHRASE",
                    '    │   ├── VERB: "pali"',
                    '    │   ├── PARTICLE: "e"',
                    "    │   └── NOUN_PHRASE",
                    '    │       └── NOUN: "ijo"',
                    "    └── .",
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("mi moku e telo."),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    ├── NOUN_PHRASE",
                    '    │   └── NOUN: "mi"',
                    "    ├── VERB_PHRASE",
                    '    │   ├── VERB: "moku"',
                    '    │   ├── PARTICLE: "e"',
                    "    │   └── NOUN_PHRASE",
                    '    │       └── NOUN: "telo"',
                    "    └── .",
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("mije li sona."),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    ├── NOUN_PHRASE",
                    '    │   └── NOUN: "mije"',
                    '    ├── PARTICLE: "li"',
                    "    ├── VERB_PHRASE",
                    "    │   └── ADJECTIVE_PHRASE",
                    '    │       └── ADJECTIVE: "sona"',
                    "    └── .",
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("mije li sona e ijo."),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    ├── NOUN_PHRASE",
                    '    │   └── NOUN: "mije"',
                    '    ├── PARTICLE: "li"',
                    "    ├── VERB_PHRASE",
                    '    │   ├── VERB: "sona"',
                    '    │   ├── PARTICLE: "e"',
                    "    │   └── NOUN_PHRASE",
                    '    │       └── NOUN: "ijo"',
                    "    └── .",
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("mi sona e toki pona."),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    ├── NOUN_PHRASE",
                    '    │   └── NOUN: "mi"',
                    "    ├── VERB_PHRASE",
                    '    │   ├── VERB: "sona"',
                    '    │   ├── PARTICLE: "e"',
                    "    │   └── NOUN_PHRASE",
                    '    │       ├── NOUN: "toki"',
                    "    │       └── ADJECTIVE_PHRASE",
                    '    │           └── ADJECTIVE: "pona"',
                    "    └── .",
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("mije ni li jan toki."),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    ├── NOUN_PHRASE",
                    '    │   ├── NOUN: "mije"',
                    "    │   └── ADJECTIVE_PHRASE",
                    '    │       └── ADJECTIVE: "ni"',
                    '    ├── PARTICLE: "li"',
                    "    ├── VERB_PHRASE",
                    "    │   └── NOUN_PHRASE",
                    '    │       ├── NOUN: "jan"',
                    "    │       └── ADJECTIVE_PHRASE",
                    '    │           └── ADJECTIVE: "toki"',
                    "    └── .",
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("soweli suli li moku e sina."),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    ├── NOUN_PHRASE",
                    '    │   ├── NOUN: "soweli"',
                    "    │   └── ADJECTIVE_PHRASE",
                    '    │       └── ADJECTIVE: "suli"',
                    '    ├── PARTICLE: "li"',
                    "    ├── VERB_PHRASE",
                    '    │   ├── VERB: "moku"',
                    '    │   ├── PARTICLE: "e"',
                    "    │   └── NOUN_PHRASE",
                    '    │       └── NOUN: "sina"',
                    "    └── .",
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("lipu kulupu li wawa."),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    ├── NOUN_PHRASE",
                    '    │   ├── NOUN: "lipu"',
                    "    │   └── ADJECTIVE_PHRASE",
                    '    │       └── ADJECTIVE: "kulupu"',
                    '    ├── PARTICLE: "li"',
                    "    ├── VERB_PHRASE",
                    "    │   └── ADJECTIVE_PHRASE",
                    '    │       └── ADJECTIVE: "wawa"',
                    "    └── .",
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("sina pali e moku sin."),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    ├── NOUN_PHRASE",
                    '    │   └── NOUN: "sina"',
                    "    ├── VERB_PHRASE",
                    '    │   ├── VERB: "pali"',
                    '    │   ├── PARTICLE: "e"',
                    "    │   └── NOUN_PHRASE",
                    '    │       ├── NOUN: "moku"',
                    "    │       └── ADJECTIVE_PHRASE",
                    '    │           └── ADJECTIVE: "sin"',
                    "    └── .",
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("jan sona li kute."),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    ├── NOUN_PHRASE",
                    '    │   ├── NOUN: "jan"',
                    "    │   └── ADJECTIVE_PHRASE",
                    '    │       └── ADJECTIVE: "sona"',
                    '    ├── PARTICLE: "li"',
                    "    ├── VERB_PHRASE",
                    "    │   └── ADJECTIVE_PHRASE",
                    '    │       └── ADJECTIVE: "kute"',
                    "    └── .",
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("tomo sona li jo e lipu."),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    ├── NOUN_PHRASE",
                    '    │   ├── NOUN: "tomo"',
                    "    │   └── ADJECTIVE_PHRASE",
                    '    │       └── ADJECTIVE: "sona"',
                    '    ├── PARTICLE: "li"',
                    "    ├── VERB_PHRASE",
                    '    │   ├── VERB: "jo"',
                    '    │   ├── PARTICLE: "e"',
                    "    │   └── NOUN_PHRASE",
                    '    │       └── NOUN: "lipu"',
                    "    └── .",
                ],
            ),
        )

    def test_lesson_6(self):
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("mi moku ala e soweli."),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    ├── NOUN_PHRASE",
                    '    │   └── NOUN: "mi"',
                    "    ├── VERB_PHRASE",
                    '    │   ├── VERB: "moku"',
                    "    │   ├── ADJECTIVE_PHRASE",
                    '    │   │   └── ADJECTIVE: "ala"',
                    '    │   ├── PARTICLE: "e"',
                    "    │   └── NOUN_PHRASE",
                    '    │       └── NOUN: "soweli"',
                    "    └── .",
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("mi toki pona e ijo."),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    ├── NOUN_PHRASE",
                    '    │   └── NOUN: "mi"',
                    "    ├── VERB_PHRASE",
                    '    │   ├── VERB: "toki"',
                    "    │   ├── ADJECTIVE_PHRASE",
                    '    │   │   └── ADJECTIVE: "pona"',
                    '    │   ├── PARTICLE: "e"',
                    "    │   └── NOUN_PHRASE",
                    '    │       └── NOUN: "ijo"',
                    "    └── .",
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("pona mute"),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    └── NOUN_PHRASE",
                    '        ├── NOUN: "pona"',
                    "        └── ADJECTIVE_PHRASE",
                    '            └── ADJECTIVE: "mute"',
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("wawa lili"),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    └── NOUN_PHRASE",
                    '        ├── NOUN: "wawa"',
                    "        └── ADJECTIVE_PHRASE",
                    '            └── ADJECTIVE: "lili"',
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("pali sina li pona mute."),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    ├── NOUN_PHRASE",
                    '    │   ├── NOUN: "pali"',
                    "    │   └── ADJECTIVE_PHRASE",
                    '    │       └── ADJECTIVE: "sina"',
                    '    ├── PARTICLE: "li"',
                    "    ├── VERB_PHRASE",
                    "    │   └── NOUN_PHRASE",
                    '    │       ├── NOUN: "pona"',
                    "    │       └── ADJECTIVE_PHRASE",
                    '    │           └── ADJECTIVE: "mute"',
                    "    └── .",
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("telo li wawa e mi."),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    ├── NOUN_PHRASE",
                    '    │   └── NOUN: "telo"',
                    '    ├── PARTICLE: "li"',
                    "    ├── VERB_PHRASE",
                    '    │   ├── VERB: "wawa"',
                    '    │   ├── PARTICLE: "e"',
                    "    │   └── NOUN_PHRASE",
                    '    │       └── NOUN: "mi"',
                    "    └── .",
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("jan sona li pu."),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    ├── NOUN_PHRASE",
                    '    │   ├── NOUN: "jan"',
                    "    │   └── ADJECTIVE_PHRASE",
                    '    │       └── ADJECTIVE: "sona"',
                    '    ├── PARTICLE: "li"',
                    "    ├── VERB_PHRASE",
                    "    │   └── ADJECTIVE_PHRASE",
                    '    │       └── ADJECTIVE: "pu"',
                    "    └── .",
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("meli lili li kute ike e mama."),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    ├── NOUN_PHRASE",
                    '    │   ├── NOUN: "meli"',
                    "    │   └── ADJECTIVE_PHRASE",
                    '    │       └── ADJECTIVE: "lili"',
                    '    ├── PARTICLE: "li"',
                    "    ├── VERB_PHRASE",
                    '    │   ├── VERB: "kute"',
                    "    │   ├── ADJECTIVE_PHRASE",
                    '    │   │   └── ADJECTIVE: "ike"',
                    '    │   ├── PARTICLE: "e"',
                    "    │   └── NOUN_PHRASE",
                    '    │       └── NOUN: "mama"',
                    "    └── .",
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("sewi li wan."),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    ├── NOUN_PHRASE",
                    '    │   └── NOUN: "sewi"',
                    '    ├── PARTICLE: "li"',
                    "    ├── VERB_PHRASE",
                    "    │   └── NUMBER_PHRASE",
                    '    │       └── NUMBER: "wan"',
                    "    └── .",
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("jan ala li ike."),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    ├── NOUN_PHRASE",
                    '    │   ├── NOUN: "jan"',
                    "    │   └── ADJECTIVE_PHRASE",
                    '    │       └── ADJECTIVE: "ala"',
                    '    ├── PARTICLE: "li"',
                    "    ├── VERB_PHRASE",
                    "    │   └── ADJECTIVE_PHRASE",
                    '    │       └── ADJECTIVE: "ike"',
                    "    └── .",
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("mama mije li pu mute."),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    ├── NOUN_PHRASE",
                    '    │   ├── NOUN: "mama"',
                    "    │   └── ADJECTIVE_PHRASE",
                    '    │       └── ADJECTIVE: "mije"',
                    '    ├── PARTICLE: "li"',
                    "    ├── VERB_PHRASE",
                    "    │   └── NOUN_PHRASE",
                    '    │       ├── NOUN: "pu"',
                    "    │       └── ADJECTIVE_PHRASE",
                    '    │           └── ADJECTIVE: "mute"',
                    "    └── .",
                ],
            ),
        )

    def test_lesson_7(self):
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("seme li sin?"),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    ├── NOUN_PHRASE",
                    '    │   └── NOUN: "seme"',
                    '    ├── PARTICLE: "li"',
                    "    ├── VERB_PHRASE",
                    "    │   └── ADJECTIVE_PHRASE",
                    '    │       └── ADJECTIVE: "sin"',
                    "    └── ?",
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("jan seme li toki?"),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    ├── NOUN_PHRASE",
                    '    │   ├── NOUN: "jan"',
                    "    │   └── ADJECTIVE_PHRASE",
                    '    │       └── ADJECTIVE: "seme"',
                    '    ├── PARTICLE: "li"',
                    "    ├── VERB_PHRASE",
                    "    │   └── ADJECTIVE_PHRASE",
                    '    │       └── ADJECTIVE: "toki"',
                    "    └── ?",
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("sina pu anu seme?"),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    ├── NOUN_PHRASE",
                    '    │   └── NOUN: "sina"',
                    "    ├── VERB_PHRASE",
                    "    │   └── ADJECTIVE_PHRASE",
                    '    │       └── ADJECTIVE: "pu"',
                    '    ├── PARTICLE: "anu"',
                    '    ├── PARTICLE: "seme"',
                    "    └── ?",
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("ona li mama ala mama?"),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    ├── NOUN_PHRASE",
                    '    │   └── NOUN: "ona"',
                    '    ├── PARTICLE: "li"',
                    "    ├── VERB_PHRASE",
                    "    │   └── ADJECTIVE_PHRASE",
                    '    │       ├── ADJECTIVE: "mama"',
                    '    │       ├── PARTICLE: "ala"',
                    '    │       └── ADJECTIVE: "mama"',
                    "    └── ?",
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("mama."),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    ├── ADJECTIVE_PHRASE",
                    '    │   └── ADJECTIVE: "mama"',
                    "    └── .",
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("mama ala."),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    ├── NOUN_PHRASE",
                    '    │   ├── NOUN: "mama"',
                    "    │   └── ADJECTIVE_PHRASE",
                    '    │       └── ADJECTIVE: "ala"',
                    "    └── .",
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("ala."),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    ├── NUMBER_PHRASE",
                    '    │   └── NUMBER: "ala"',
                    "    └── .",
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("ona li jo ala jo e kili mute?"),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    ├── NOUN_PHRASE",
                    '    │   └── NOUN: "ona"',
                    '    ├── PARTICLE: "li"',
                    "    ├── VERB_PHRASE",
                    '    │   ├── VERB: "jo"',
                    '    │   ├── PARTICLE: "ala"',
                    '    │   ├── VERB: "jo"',
                    '    │   ├── PARTICLE: "e"',
                    "    │   └── NOUN_PHRASE",
                    '    │       ├── NOUN: "kili"',
                    "    │       └── ADJECTIVE_PHRASE",
                    '    │           └── ADJECTIVE: "mute"',
                    "    └── ?",
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("jo."),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    ├── ADJECTIVE_PHRASE",
                    '    │   └── ADJECTIVE: "jo"',
                    "    └── .",
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("mije sona li jo e kala anu seme?"),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    ├── NOUN_PHRASE",
                    '    │   ├── NOUN: "mije"',
                    "    │   └── ADJECTIVE_PHRASE",
                    '    │       └── ADJECTIVE: "sona"',
                    '    ├── PARTICLE: "li"',
                    "    ├── VERB_PHRASE",
                    '    │   ├── VERB: "jo"',
                    '    │   ├── PARTICLE: "e"',
                    "    │   └── NOUN_PHRASE",
                    '    │       └── NOUN: "kala"',
                    '    ├── PARTICLE: "anu"',
                    '    ├── PARTICLE: "seme"',
                    "    └── ?",
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("sina seme e ona?"),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    ├── NOUN_PHRASE",
                    '    │   └── NOUN: "sina"',
                    "    ├── VERB_PHRASE",
                    '    │   ├── VERB: "seme"',
                    '    │   ├── PARTICLE: "e"',
                    "    │   └── NOUN_PHRASE",
                    '    │       └── NOUN: "ona"',
                    "    └── ?",
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("tomo li jo e ilo toki."),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    ├── NOUN_PHRASE",
                    '    │   └── NOUN: "tomo"',
                    '    ├── PARTICLE: "li"',
                    "    ├── VERB_PHRASE",
                    '    │   ├── VERB: "jo"',
                    '    │   ├── PARTICLE: "e"',
                    "    │   └── NOUN_PHRASE",
                    '    │       ├── NOUN: "ilo"',
                    "    │       └── ADJECTIVE_PHRASE",
                    '    │           └── ADJECTIVE: "toki"',
                    "    └── .",
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("sina kute ala kute e mama sina?"),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    ├── NOUN_PHRASE",
                    '    │   └── NOUN: "sina"',
                    "    ├── VERB_PHRASE",
                    '    │   ├── VERB: "kute"',
                    '    │   ├── PARTICLE: "ala"',
                    '    │   ├── VERB: "kute"',
                    '    │   ├── PARTICLE: "e"',
                    "    │   └── NOUN_PHRASE",
                    '    │       ├── NOUN: "mama"',
                    "    │       └── ADJECTIVE_PHRASE",
                    '    │           └── ADJECTIVE: "sina"',
                    "    └── ?",
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("kala wawa li moku e seme?"),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    ├── NOUN_PHRASE",
                    '    │   ├── NOUN: "kala"',
                    "    │   └── ADJECTIVE_PHRASE",
                    '    │       └── ADJECTIVE: "wawa"',
                    '    ├── PARTICLE: "li"',
                    "    ├── VERB_PHRASE",
                    '    │   ├── VERB: "moku"',
                    '    │   ├── PARTICLE: "e"',
                    "    │   └── NOUN_PHRASE",
                    '    │       └── NOUN: "seme"',
                    "    └── ?",
                ],
            ),
        )

    def test_lesson_8(self):
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("mi pana e kala tawa ona."),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    ├── NOUN_PHRASE",
                    '    │   └── NOUN: "mi"',
                    "    ├── VERB_PHRASE",
                    '    │   ├── VERB: "pana"',
                    '    │   ├── PARTICLE: "e"',
                    "    │   ├── NOUN_PHRASE",
                    '    │   │   └── NOUN: "kala"',
                    "    │   └── PREPOSITION_PHRASE",
                    '    │       ├── PREPOSITION: "tawa"',
                    "    │       └── NOUN_PHRASE",
                    '    │           └── NOUN: "ona"',
                    "    └── .",
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("mi pana e kala lon tomo."),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    ├── NOUN_PHRASE",
                    '    │   └── NOUN: "mi"',
                    "    ├── VERB_PHRASE",
                    '    │   ├── VERB: "pana"',
                    '    │   ├── PARTICLE: "e"',
                    "    │   ├── NOUN_PHRASE",
                    '    │   │   └── NOUN: "kala"',
                    "    │   └── PREPOSITION_PHRASE",
                    '    │       ├── PREPOSITION: "lon"',
                    "    │       └── NOUN_PHRASE",
                    '    │           └── NOUN: "tomo"',
                    "    └── .",
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("mi pana e kala tawa ona lon tomo."),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    ├── NOUN_PHRASE",
                    '    │   └── NOUN: "mi"',
                    "    ├── VERB_PHRASE",
                    '    │   ├── VERB: "pana"',
                    '    │   ├── PARTICLE: "e"',
                    "    │   ├── NOUN_PHRASE",
                    '    │   │   └── NOUN: "kala"',
                    "    │   ├── PREPOSITION_PHRASE",
                    '    │   │   ├── PREPOSITION: "tawa"',
                    "    │   │   └── NOUN_PHRASE",
                    '    │   │       └── NOUN: "ona"',
                    "    │   └── PREPOSITION_PHRASE",
                    '    │       ├── PREPOSITION: "lon"',
                    "    │       └── NOUN_PHRASE",
                    '    │           └── NOUN: "tomo"',
                    "    └── .",
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("mi lon tomo."),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    ├── NOUN_PHRASE",
                    '    │   └── NOUN: "mi"',
                    "    ├── VERB_PHRASE",
                    "    │   └── PREPOSITION_PHRASE",
                    '    │       ├── PREPOSITION: "lon"',
                    "    │       └── NOUN_PHRASE",
                    '    │           └── NOUN: "tomo"',
                    "    └── .",
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("mi tawa sina."),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    ├── NOUN_PHRASE",
                    '    │   └── NOUN: "mi"',
                    "    ├── VERB_PHRASE",
                    "    │   └── PREPOSITION_PHRASE",
                    '    │       ├── PREPOSITION: "tawa"',
                    "    │       └── NOUN_PHRASE",
                    '    │           └── NOUN: "sina"',
                    "    └── .",
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("mama mi li tawa telo suli."),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    ├── NOUN_PHRASE",
                    '    │   ├── NOUN: "mama"',
                    "    │   └── ADJECTIVE_PHRASE",
                    '    │       └── ADJECTIVE: "mi"',
                    '    ├── PARTICLE: "li"',
                    "    ├── VERB_PHRASE",
                    "    │   └── PREPOSITION_PHRASE",
                    '    │       ├── PREPOSITION: "tawa"',
                    "    │       └── NOUN_PHRASE",
                    '    │           ├── NOUN: "telo"',
                    "    │           └── ADJECTIVE_PHRASE",
                    '    │               └── ADJECTIVE: "suli"',
                    "    └── .",
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("mi pali mute tan ni."),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    ├── NOUN_PHRASE",
                    '    │   └── NOUN: "mi"',
                    "    ├── VERB_PHRASE",
                    '    │   ├── VERB: "pali"',
                    "    │   ├── ADJECTIVE_PHRASE",
                    '    │   │   └── ADJECTIVE: "mute"',
                    "    │   └── PREPOSITION_PHRASE",
                    '    │       ├── PREPOSITION: "tan"',
                    "    │       └── NOUN_PHRASE",
                    '    │           └── NOUN: "ni"',
                    "    └── .",
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("mi toki lon toki pona."),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    ├── NOUN_PHRASE",
                    '    │   └── NOUN: "mi"',
                    "    ├── VERB_PHRASE",
                    '    │   ├── VERB: "toki"',
                    "    │   └── PREPOSITION_PHRASE",
                    '    │       ├── PREPOSITION: "lon"',
                    "    │       └── NOUN_PHRASE",
                    '    │           ├── NOUN: "toki"',
                    "    │           └── ADJECTIVE_PHRASE",
                    '    │               └── ADJECTIVE: "pona"',
                    "    └── .",
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("soweli lili li pona tawa mi."),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    ├── NOUN_PHRASE",
                    '    │   ├── NOUN: "soweli"',
                    "    │   └── ADJECTIVE_PHRASE",
                    '    │       └── ADJECTIVE: "lili"',
                    '    ├── PARTICLE: "li"',
                    "    ├── VERB_PHRASE",
                    '    │   ├── VERB: "pona"',
                    "    │   └── PREPOSITION_PHRASE",
                    '    │       ├── PREPOSITION: "tawa"',
                    "    │       └── NOUN_PHRASE",
                    '    │           └── NOUN: "mi"',
                    "    └── .",
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("kulupu pali li kepeken seme?"),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    ├── NOUN_PHRASE",
                    '    │   ├── NOUN: "kulupu"',
                    "    │   └── ADJECTIVE_PHRASE",
                    '    │       └── ADJECTIVE: "pali"',
                    '    ├── PARTICLE: "li"',
                    "    ├── VERB_PHRASE",
                    "    │   └── PREPOSITION_PHRASE",
                    '    │       ├── PREPOSITION: "kepeken"',
                    "    │       └── NOUN_PHRASE",
                    '    │           └── NOUN: "seme"',
                    "    └── ?",
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("mi sona e toki mute tan meli ni."),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    ├── NOUN_PHRASE",
                    '    │   └── NOUN: "mi"',
                    "    ├── VERB_PHRASE",
                    '    │   ├── VERB: "sona"',
                    '    │   ├── PARTICLE: "e"',
                    "    │   ├── NOUN_PHRASE",
                    '    │   │   ├── NOUN: "toki"',
                    "    │   │   └── ADJECTIVE_PHRASE",
                    '    │   │       └── ADJECTIVE: "mute"',
                    "    │   └── PREPOSITION_PHRASE",
                    '    │       ├── PREPOSITION: "tan"',
                    "    │       └── NOUN_PHRASE",
                    '    │           ├── NOUN: "meli"',
                    "    │           └── ADJECTIVE_PHRASE",
                    '    │               └── ADJECTIVE: "ni"',
                    "    └── .",
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("mije sin li lon tomo telo anu seme?"),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    ├── NOUN_PHRASE",
                    '    │   ├── NOUN: "mije"',
                    "    │   └── ADJECTIVE_PHRASE",
                    '    │       └── ADJECTIVE: "sin"',
                    '    ├── PARTICLE: "li"',
                    "    ├── VERB_PHRASE",
                    "    │   └── PREPOSITION_PHRASE",
                    '    │       ├── PREPOSITION: "lon"',
                    "    │       └── NOUN_PHRASE",
                    '    │           ├── NOUN: "tomo"',
                    "    │           └── ADJECTIVE_PHRASE",
                    '    │               └── ADJECTIVE: "telo"',
                    '    ├── PARTICLE: "anu"',
                    '    ├── PARTICLE: "seme"',
                    "    └── ?",
                ],
            ),
        )

    def test_lesson_9(self):
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("ma tomo"),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    └── NOUN_PHRASE",
                    '        ├── NOUN: "ma"',
                    "        └── ADJECTIVE_PHRASE",
                    '            └── ADJECTIVE: "tomo"',
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("ma tomo Isanpu"),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    └── NOUN_PHRASE",
                    '        ├── NOUN: "ma"',
                    "        └── ADJECTIVE_PHRASE",
                    '            ├── ADJECTIVE: "tomo"',
                    '            └── ADJECTIVE: "Isanpu"',
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("nimi mi li Apu."),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    ├── NOUN_PHRASE",
                    '    │   ├── NOUN: "nimi"',
                    "    │   └── ADJECTIVE_PHRASE",
                    '    │       └── ADJECTIVE: "mi"',
                    '    ├── PARTICLE: "li"',
                    "    ├── VERB_PHRASE",
                    "    │   └── ADJECTIVE_PHRASE",
                    '    │       └── ADJECTIVE: "Apu"',
                    "    └── .",
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("ma Apika li jo e jan mute."),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    ├── NOUN_PHRASE",
                    '    │   ├── NOUN: "ma"',
                    "    │   └── ADJECTIVE_PHRASE",
                    '    │       └── ADJECTIVE: "Apika"',
                    '    ├── PARTICLE: "li"',
                    "    ├── VERB_PHRASE",
                    '    │   ├── VERB: "jo"',
                    '    │   ├── PARTICLE: "e"',
                    "    │   └── NOUN_PHRASE",
                    '    │       ├── NOUN: "jan"',
                    "    │       └── ADJECTIVE_PHRASE",
                    '    │           └── ADJECTIVE: "mute"',
                    "    └── .",
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("meli Sonko li tawa nasin Kuwin."),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    ├── NOUN_PHRASE",
                    '    │   ├── NOUN: "meli"',
                    "    │   └── ADJECTIVE_PHRASE",
                    '    │       └── ADJECTIVE: "Sonko"',
                    '    ├── PARTICLE: "li"',
                    "    ├── VERB_PHRASE",
                    "    │   └── PREPOSITION_PHRASE",
                    '    │       ├── PREPOSITION: "tawa"',
                    "    │       └── NOUN_PHRASE",
                    '    │           ├── NOUN: "nasin"',
                    "    │           └── ADJECTIVE_PHRASE",
                    '    │               └── ADJECTIVE: "Kuwin"',
                    "    └── .",
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("jan Epawam Linkan li tan ma Mewika."),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    ├── NOUN_PHRASE",
                    '    │   ├── NOUN: "jan"',
                    "    │   └── ADJECTIVE_PHRASE",
                    '    │       ├── ADJECTIVE: "Epawam"',
                    '    │       └── ADJECTIVE: "Linkan"',
                    '    ├── PARTICLE: "li"',
                    "    ├── VERB_PHRASE",
                    "    │   └── PREPOSITION_PHRASE",
                    '    │       ├── PREPOSITION: "tan"',
                    "    │       └── NOUN_PHRASE",
                    '    │           ├── NOUN: "ma"',
                    "    │           └── ADJECTIVE_PHRASE",
                    '    │               └── ADJECTIVE: "Mewika"',
                    "    └── .",
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("ma tomo Pelin li lon ma Tosi."),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    ├── NOUN_PHRASE",
                    '    │   ├── NOUN: "ma"',
                    "    │   └── ADJECTIVE_PHRASE",
                    '    │       ├── ADJECTIVE: "tomo"',
                    '    │       └── ADJECTIVE: "Pelin"',
                    '    ├── PARTICLE: "li"',
                    "    ├── VERB_PHRASE",
                    "    │   └── PREPOSITION_PHRASE",
                    '    │       ├── PREPOSITION: "lon"',
                    "    │       └── NOUN_PHRASE",
                    '    │           ├── NOUN: "ma"',
                    "    │           └── ADJECTIVE_PHRASE",
                    '    │               └── ADJECTIVE: "Tosi"',
                    "    └── .",
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("sina sona ala sona e toki Inli?"),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    ├── NOUN_PHRASE",
                    '    │   └── NOUN: "sina"',
                    "    ├── VERB_PHRASE",
                    '    │   ├── VERB: "sona"',
                    '    │   ├── PARTICLE: "ala"',
                    '    │   ├── VERB: "sona"',
                    '    │   ├── PARTICLE: "e"',
                    "    │   └── NOUN_PHRASE",
                    '    │       ├── NOUN: "toki"',
                    "    │       └── ADJECTIVE_PHRASE",
                    '    │           └── ADJECTIVE: "Inli"',
                    "    └── ?",
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("nena sewi Kepelitepe li lon ma Tuki."),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    ├── NOUN_PHRASE",
                    '    │   ├── NOUN: "nena"',
                    "    │   └── ADJECTIVE_PHRASE",
                    '    │       ├── ADJECTIVE: "sewi"',
                    '    │       └── ADJECTIVE: "Kepelitepe"',
                    '    ├── PARTICLE: "li"',
                    "    ├── VERB_PHRASE",
                    "    │   └── PREPOSITION_PHRASE",
                    '    │       ├── PREPOSITION: "lon"',
                    "    │       └── NOUN_PHRASE",
                    '    │           ├── NOUN: "ma"',
                    "    │           └── ADJECTIVE_PHRASE",
                    '    │               └── ADJECTIVE: "Tuki"',
                    "    └── .",
                ],
            ),
        )

    def test_lesson_10(self):
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("toki!"),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    ├── ADJECTIVE_PHRASE",
                    '    │   └── ADJECTIVE: "toki"',
                    "    └── !",
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("pona tawa sina!"),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    ├── ADJECTIVE_PHRASE",
                    '    │   └── ADJECTIVE: "pona"',
                    "    ├── PREPOSITION_PHRASE",
                    '    │   ├── PREPOSITION: "tawa"',
                    "    │   └── NOUN_PHRASE",
                    '    │       └── NOUN: "sina"',
                    "    └── !",
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("kama pona!"),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    ├── NOUN_PHRASE",
                    '    │   ├── NOUN: "kama"',
                    "    │   └── ADJECTIVE_PHRASE",
                    '    │       └── ADJECTIVE: "pona"',
                    "    └── !",
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("seme li sin?"),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    ├── NOUN_PHRASE",
                    '    │   └── NOUN: "seme"',
                    '    ├── PARTICLE: "li"',
                    "    ├── VERB_PHRASE",
                    "    │   └── ADJECTIVE_PHRASE",
                    '    │       └── ADJECTIVE: "sin"',
                    "    └── ?",
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("mi tawa."),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    ├── NOUN_PHRASE",
                    '    │   └── NOUN: "mi"',
                    "    ├── VERB_PHRASE",
                    "    │   └── ADJECTIVE_PHRASE",
                    '    │       └── ADJECTIVE: "tawa"',
                    "    └── .",
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("tawa pona."),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    ├── PREPOSITION_PHRASE",
                    '    │   ├── PREPOSITION: "tawa"',
                    "    │   └── NOUN_PHRASE",
                    '    │       └── NOUN: "pona"',
                    "    └── .",
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("o toki ala. o pali."),
            Phrase.from_lines(
                [
                    "TEXT",
                    "├── SENTENCE",
                    '│   ├── PARTICLE: "o"',
                    "│   ├── VERB_PHRASE",
                    '│   │   ├── VERB: "toki"',
                    "│   │   └── ADJECTIVE_PHRASE",
                    '│   │       └── ADJECTIVE: "ala"',
                    "│   └── .",
                    "└── SENTENCE",
                    '    ├── PARTICLE: "o"',
                    "    ├── VERB_PHRASE",
                    '    │   └── VERB: "pali"',
                    "    └── .",
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("jan Mosima o, ni li soweli sina anu seme?"),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    ├── NOUN_PHRASE",
                    '    │   ├── NOUN: "jan"',
                    "    │   └── ADJECTIVE_PHRASE",
                    '    │       └── ADJECTIVE: "Mosima"',
                    '    ├── PARTICLE: "o"',
                    "    ├── ,",
                    "    ├── NOUN_PHRASE",
                    '    │   └── NOUN: "ni"',
                    '    ├── PARTICLE: "li"',
                    "    ├── VERB_PHRASE",
                    "    │   └── NOUN_PHRASE",
                    '    │       ├── NOUN: "soweli"',
                    "    │       └── ADJECTIVE_PHRASE",
                    '    │           └── ADJECTIVE: "sina"',
                    '    ├── PARTICLE: "anu"',
                    '    ├── PARTICLE: "seme"',
                    "    └── ?",
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("o moku ala e kili mi."),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    '    ├── PARTICLE: "o"',
                    "    ├── VERB_PHRASE",
                    '    │   ├── VERB: "moku"',
                    "    │   ├── ADJECTIVE_PHRASE",
                    '    │   │   └── ADJECTIVE: "ala"',
                    '    │   ├── PARTICLE: "e"',
                    "    │   └── NOUN_PHRASE",
                    '    │       ├── NOUN: "kili"',
                    "    │       └── ADJECTIVE_PHRASE",
                    '    │           └── ADJECTIVE: "mi"',
                    "    └── .",
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("sina pilin ike tan seme?"),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    ├── NOUN_PHRASE",
                    '    │   └── NOUN: "sina"',
                    "    ├── VERB_PHRASE",
                    '    │   ├── VERB: "pilin"',
                    "    │   ├── ADJECTIVE_PHRASE",
                    '    │   │   └── ADJECTIVE: "ike"',
                    "    │   └── PREPOSITION_PHRASE",
                    '    │       ├── PREPOSITION: "tan"',
                    "    │       └── NOUN_PHRASE",
                    '    │           └── NOUN: "seme"',
                    "    └── ?",
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("sewi o pana e pona tawa mi."),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    ├── NOUN_PHRASE",
                    '    │   └── NOUN: "sewi"',
                    '    ├── PARTICLE: "o"',
                    "    ├── VERB_PHRASE",
                    '    │   ├── VERB: "pana"',
                    '    │   ├── PARTICLE: "e"',
                    "    │   ├── NOUN_PHRASE",
                    '    │   │   └── NOUN: "pona"',
                    "    │   └── PREPOSITION_PHRASE",
                    '    │       ├── PREPOSITION: "tawa"',
                    "    │       └── NOUN_PHRASE",
                    '    │           └── NOUN: "mi"',
                    "    └── .",
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("o kute e mama sina."),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    '    ├── PARTICLE: "o"',
                    "    ├── VERB_PHRASE",
                    '    │   ├── VERB: "kute"',
                    '    │   ├── PARTICLE: "e"',
                    "    │   └── NOUN_PHRASE",
                    '    │       ├── NOUN: "mama"',
                    "    │       └── ADJECTIVE_PHRASE",
                    '    │           └── ADJECTIVE: "sina"',
                    "    └── .",
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("sina suli a!"),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    ├── NOUN_PHRASE",
                    '    │   └── NOUN: "sina"',
                    "    ├── VERB_PHRASE",
                    "    │   └── ADJECTIVE_PHRASE",
                    '    │       └── ADJECTIVE: "suli"',
                    '    ├── PARTICLE: "a"',
                    "    └── !",
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("pona!"),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    ├── ADJECTIVE_PHRASE",
                    '    │   └── ADJECTIVE: "pona"',
                    "    └── !",
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("mi o moku e ijo pona."),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    ├── NOUN_PHRASE",
                    '    │   └── NOUN: "mi"',
                    '    ├── PARTICLE: "o"',
                    "    ├── VERB_PHRASE",
                    '    │   ├── VERB: "moku"',
                    '    │   ├── PARTICLE: "e"',
                    "    │   └── NOUN_PHRASE",
                    '    │       ├── NOUN: "ijo"',
                    "    │       └── ADJECTIVE_PHRASE",
                    '    │           └── ADJECTIVE: "pona"',
                    "    └── .",
                ],
            ),
        )

    def test_lesson_11(self):
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("jan pona"),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    └── NOUN_PHRASE",
                    '        ├── NOUN: "jan"',
                    "        └── ADJECTIVE_PHRASE",
                    '            └── ADJECTIVE: "pona"',
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("mije sona"),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    └── NOUN_PHRASE",
                    '        ├── NOUN: "mije"',
                    "        └── ADJECTIVE_PHRASE",
                    '            └── ADJECTIVE: "sona"',
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("jan pona mute"),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    └── NOUN_PHRASE",
                    '        ├── NOUN: "jan"',
                    "        └── ADJECTIVE_PHRASE",
                    '            ├── ADJECTIVE: "pona"',
                    '            └── ADJECTIVE: "mute"',
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("mije sona lili"),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    └── NOUN_PHRASE",
                    '        ├── NOUN: "mije"',
                    "        └── ADJECTIVE_PHRASE",
                    '            ├── ADJECTIVE: "sona"',
                    '            └── ADJECTIVE: "lili"',
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("jan pi pona mute"),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    └── NOUN_PHRASE",
                    '        ├── NOUN: "jan"',
                    '        ├── PARTICLE: "pi"',
                    '        ├── NOUN: "pona"',
                    "        └── ADJECTIVE_PHRASE",
                    '            └── ADJECTIVE: "mute"',
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("mije pi sona lili"),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    └── NOUN_PHRASE",
                    '        ├── NOUN: "mije"',
                    '        ├── PARTICLE: "pi"',
                    '        ├── NOUN: "sona"',
                    "        └── ADJECTIVE_PHRASE",
                    '            └── ADJECTIVE: "lili"',
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("tenpo suno ni li pona mute tawa mi."),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    ├── NOUN_PHRASE",
                    '    │   ├── NOUN: "tenpo"',
                    "    │   └── ADJECTIVE_PHRASE",
                    '    │       ├── ADJECTIVE: "suno"',
                    '    │       └── ADJECTIVE: "ni"',
                    '    ├── PARTICLE: "li"',
                    "    ├── VERB_PHRASE",
                    '    │   ├── VERB: "pona"',
                    "    │   ├── ADJECTIVE_PHRASE",
                    '    │   │   └── ADJECTIVE: "mute"',
                    "    │   └── PREPOSITION_PHRASE",
                    '    │       ├── PREPOSITION: "tawa"',
                    "    │       └── NOUN_PHRASE",
                    '    │           └── NOUN: "mi"',
                    "    └── .",
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("meli lili pi sijelo pona li telo e kasi."),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    ├── NOUN_PHRASE",
                    '    │   ├── NOUN: "meli"',
                    "    │   ├── ADJECTIVE_PHRASE",
                    '    │   │   └── ADJECTIVE: "lili"',
                    '    │   ├── PARTICLE: "pi"',
                    '    │   ├── NOUN: "sijelo"',
                    "    │   └── ADJECTIVE_PHRASE",
                    '    │       └── ADJECTIVE: "pona"',
                    '    ├── PARTICLE: "li"',
                    "    ├── VERB_PHRASE",
                    '    │   ├── VERB: "telo"',
                    '    │   ├── PARTICLE: "e"',
                    "    │   └── NOUN_PHRASE",
                    '    │       └── NOUN: "kasi"',
                    "    └── .",
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("mije pi pilin pona li pali e ilo tenpo suno."),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    ├── NOUN_PHRASE",
                    '    │   ├── NOUN: "mije"',
                    '    │   ├── PARTICLE: "pi"',
                    '    │   ├── NOUN: "pilin"',
                    "    │   └── ADJECTIVE_PHRASE",
                    '    │       └── ADJECTIVE: "pona"',
                    '    ├── PARTICLE: "li"',
                    "    ├── VERB_PHRASE",
                    '    │   ├── VERB: "pali"',
                    '    │   ├── PARTICLE: "e"',
                    "    │   └── NOUN_PHRASE",
                    '    │       ├── NOUN: "ilo"',
                    "    │       └── ADJECTIVE_PHRASE",
                    '    │           ├── ADJECTIVE: "tenpo"',
                    '    │           └── ADJECTIVE: "suno"',
                    "    └── .",
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("mama mama mi li lili."),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    ├── NOUN_PHRASE",
                    '    │   ├── NOUN: "mama"',
                    "    │   └── ADJECTIVE_PHRASE",
                    '    │       ├── ADJECTIVE: "mama"',
                    '    │       └── ADJECTIVE: "mi"',
                    '    ├── PARTICLE: "li"',
                    "    ├── VERB_PHRASE",
                    "    │   └── ADJECTIVE_PHRASE",
                    '    │       └── ADJECTIVE: "lili"',
                    "    └── .",
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("sina mute li jo ala jo e tomo tawa?"),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    ├── NOUN_PHRASE",
                    '    │   ├── NOUN: "sina"',
                    "    │   └── ADJECTIVE_PHRASE",
                    '    │       └── ADJECTIVE: "mute"',
                    '    ├── PARTICLE: "li"',
                    "    ├── VERB_PHRASE",
                    '    │   ├── VERB: "jo"',
                    '    │   ├── PARTICLE: "ala"',
                    '    │   ├── VERB: "jo"',
                    '    │   ├── PARTICLE: "e"',
                    "    │   └── NOUN_PHRASE",
                    '    │       ├── NOUN: "tomo"',
                    "    │       └── ADJECTIVE_PHRASE",
                    '    │           └── ADJECTIVE: "tawa"',
                    "    └── ?",
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("o awen lon tenpo pi suli mute."),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    '    ├── PARTICLE: "o"',
                    "    ├── VERB_PHRASE",
                    '    │   ├── VERB: "awen"',
                    "    │   └── PREPOSITION_PHRASE",
                    '    │       ├── PREPOSITION: "lon"',
                    "    │       └── NOUN_PHRASE",
                    '    │           ├── NOUN: "tenpo"',
                    '    │           ├── PARTICLE: "pi"',
                    '    │           ├── NOUN: "suli"',
                    "    │           └── ADJECTIVE_PHRASE",
                    '    │               └── ADJECTIVE: "mute"',
                    "    └── .",
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("jan sona pi toki pona li pu lon tenpo mute."),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    ├── NOUN_PHRASE",
                    '    │   ├── NOUN: "jan"',
                    "    │   ├── ADJECTIVE_PHRASE",
                    '    │   │   └── ADJECTIVE: "sona"',
                    '    │   ├── PARTICLE: "pi"',
                    '    │   ├── NOUN: "toki"',
                    "    │   └── ADJECTIVE_PHRASE",
                    '    │       └── ADJECTIVE: "pona"',
                    '    ├── PARTICLE: "li"',
                    "    ├── VERB_PHRASE",
                    '    │   ├── VERB: "pu"',
                    "    │   └── PREPOSITION_PHRASE",
                    '    │       ├── PREPOSITION: "lon"',
                    "    │       └── NOUN_PHRASE",
                    '    │           ├── NOUN: "tenpo"',
                    "    │           └── ADJECTIVE_PHRASE",
                    '    │               └── ADJECTIVE: "mute"',
                    "    └── .",
                ],
            ),
        )

    def test_lesson_12(self):
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("kili ala"),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    └── NOUN_PHRASE",
                    '        ├── NOUN: "kili"',
                    "        └── ADJECTIVE_PHRASE",
                    '            └── ADJECTIVE: "ala"',
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("mije wan"),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    └── NOUN_PHRASE",
                    '        ├── NOUN: "mije"',
                    "        └── ADJECTIVE_PHRASE",
                    '            └── ADJECTIVE: "wan"',
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("tomo tu"),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    └── NOUN_PHRASE",
                    '        ├── NOUN: "tomo"',
                    "        └── ADJECTIVE_PHRASE",
                    '            └── ADJECTIVE: "tu"',
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("soweli mute"),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    └── NOUN_PHRASE",
                    '        ├── NOUN: "soweli"',
                    "        └── ADJECTIVE_PHRASE",
                    '            └── ADJECTIVE: "mute"',
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("jan ale"),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    └── NOUN_PHRASE",
                    '        ├── NOUN: "jan"',
                    "        └── ADJECTIVE_PHRASE",
                    '            └── ADJECTIVE: "ale"',
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("wan"),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    └── NUMBER_PHRASE",
                    '        └── NUMBER: "wan"',
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("tu"),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    └── NUMBER_PHRASE",
                    '        └── NUMBER: "tu"',
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("luka"),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    └── NUMBER_PHRASE",
                    '        └── NUMBER: "luka"',
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("mute"),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    └── NUMBER_PHRASE",
                    '        └── NUMBER: "mute"',
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("ale"),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    └── NUMBER_PHRASE",
                    '        └── NUMBER: "ale"',
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("tu wan"),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    └── NUMBER_PHRASE",
                    '        ├── NUMBER: "tu"',
                    '        └── NUMBER: "wan"',
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("tu tu"),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    └── NUMBER_PHRASE",
                    '        ├── NUMBER: "tu"',
                    '        └── NUMBER: "tu"',
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("luka wan"),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    └── NUMBER_PHRASE",
                    '        ├── NUMBER: "luka"',
                    '        └── NUMBER: "wan"',
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("luka tu"),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    └── NUMBER_PHRASE",
                    '        ├── NUMBER: "luka"',
                    '        └── NUMBER: "tu"',
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("luka tu wan"),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    └── NUMBER_PHRASE",
                    '        ├── NUMBER: "luka"',
                    '        ├── NUMBER: "tu"',
                    '        └── NUMBER: "wan"',
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("luka tu tu"),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    └── NUMBER_PHRASE",
                    '        ├── NUMBER: "luka"',
                    '        ├── NUMBER: "tu"',
                    '        └── NUMBER: "tu"',
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("luka luka"),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    └── NUMBER_PHRASE",
                    '        ├── NUMBER: "luka"',
                    '        └── NUMBER: "luka"',
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("luka luka tu wan"),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    └── NUMBER_PHRASE",
                    '        ├── NUMBER: "luka"',
                    '        ├── NUMBER: "luka"',
                    '        ├── NUMBER: "tu"',
                    '        └── NUMBER: "wan"',
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("mute mute mute luka luka luka tu wan"),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    └── NUMBER_PHRASE",
                    '        ├── NUMBER: "mute"',
                    '        ├── NUMBER: "mute"',
                    '        ├── NUMBER: "mute"',
                    '        ├── NUMBER: "luka"',
                    '        ├── NUMBER: "luka"',
                    '        ├── NUMBER: "luka"',
                    '        ├── NUMBER: "tu"',
                    '        └── NUMBER: "wan"',
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("ale tu"),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    └── NUMBER_PHRASE",
                    '        ├── NUMBER: "ale"',
                    '        └── NUMBER: "tu"',
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("toki nanpa wan"),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    └── NOUN_PHRASE",
                    '        ├── NOUN: "toki"',
                    "        └── ADJECTIVE_PHRASE",
                    "            └── NUMBER_PHRASE",
                    '                ├── ADJECTIVE: "nanpa"',
                    '                └── NUMBER: "wan"',
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("tomo nanpa mute tu wan"),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    └── NOUN_PHRASE",
                    '        ├── NOUN: "tomo"',
                    "        └── ADJECTIVE_PHRASE",
                    "            └── NUMBER_PHRASE",
                    '                ├── ADJECTIVE: "nanpa"',
                    '                ├── NUMBER: "mute"',
                    '                ├── NUMBER: "tu"',
                    '                └── NUMBER: "wan"',
                ],
            ),
        )

    def test_lesson_13(self):
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("jan li wile pali..."),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    ├── NOUN_PHRASE",
                    '    │   └── NOUN: "jan"',
                    '    ├── PARTICLE: "li"',
                    "    ├── VERB_PHRASE",
                    '    │   ├── PREVERB: "wile"',
                    '    │   └── VERB: "pali"',
                    "    └── ...",
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("kama"),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    └── ADJECTIVE_PHRASE",
                    '        └── ADJECTIVE: "kama"',
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("lukin"),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    └── ADJECTIVE_PHRASE",
                    '        └── ADJECTIVE: "lukin"',
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("ma tomo li kama suli."),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    ├── NOUN_PHRASE",
                    '    │   ├── NOUN: "ma"',
                    "    │   └── ADJECTIVE_PHRASE",
                    '    │       └── ADJECTIVE: "tomo"',
                    '    ├── PARTICLE: "li"',
                    "    ├── VERB_PHRASE",
                    '    │   ├── PREVERB: "kama"',
                    '    │   └── VERB: "suli"',
                    "    └── .",
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("mi kama sona e toki pona."),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    ├── NOUN_PHRASE",
                    '    │   └── NOUN: "mi"',
                    "    ├── VERB_PHRASE",
                    '    │   ├── PREVERB: "kama"',
                    '    │   ├── VERB: "sona"',
                    '    │   ├── PARTICLE: "e"',
                    "    │   └── NOUN_PHRASE",
                    '    │       ├── NOUN: "toki"',
                    "    │       └── ADJECTIVE_PHRASE",
                    '    │           └── ADJECTIVE: "pona"',
                    "    └── .",
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("mije wawa li lukin jo e meli pona."),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    ├── NOUN_PHRASE",
                    '    │   ├── NOUN: "mije"',
                    "    │   └── ADJECTIVE_PHRASE",
                    '    │       └── ADJECTIVE: "wawa"',
                    '    ├── PARTICLE: "li"',
                    "    ├── VERB_PHRASE",
                    '    │   ├── PREVERB: "lukin"',
                    '    │   ├── VERB: "jo"',
                    '    │   ├── PARTICLE: "e"',
                    "    │   └── NOUN_PHRASE",
                    '    │       ├── NOUN: "meli"',
                    "    │       └── ADJECTIVE_PHRASE",
                    '    │           └── ADJECTIVE: "pona"',
                    "    └── .",
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("mi mute li kama awen lon ma tomo Towano."),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    ├── NOUN_PHRASE",
                    '    │   ├── NOUN: "mi"',
                    "    │   └── ADJECTIVE_PHRASE",
                    '    │       └── ADJECTIVE: "mute"',
                    '    ├── PARTICLE: "li"',
                    "    ├── VERB_PHRASE",
                    '    │   ├── PREVERB: "kama"',
                    '    │   ├── VERB: "awen"',
                    "    │   └── PREPOSITION_PHRASE",
                    '    │       ├── PREPOSITION: "lon"',
                    "    │       └── NOUN_PHRASE",
                    '    │           ├── NOUN: "ma"',
                    "    │           └── ADJECTIVE_PHRASE",
                    '    │               ├── ADJECTIVE: "tomo"',
                    '    │               └── ADJECTIVE: "Towano"',
                    "    └── .",
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("jan lili mi o, sina wile moku e kala anu seme?"),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    ├── NOUN_PHRASE",
                    '    │   ├── NOUN: "jan"',
                    "    │   └── ADJECTIVE_PHRASE",
                    '    │       ├── ADJECTIVE: "lili"',
                    '    │       └── ADJECTIVE: "mi"',
                    '    ├── PARTICLE: "o"',
                    "    ├── ,",
                    "    ├── NOUN_PHRASE",
                    '    │   └── NOUN: "sina"',
                    "    ├── VERB_PHRASE",
                    '    │   ├── PREVERB: "wile"',
                    '    │   ├── VERB: "moku"',
                    '    │   ├── PARTICLE: "e"',
                    "    │   └── NOUN_PHRASE",
                    '    │       └── NOUN: "kala"',
                    '    ├── PARTICLE: "anu"',
                    '    ├── PARTICLE: "seme"',
                    "    └── ?",
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("jan mute li sona ala tawa lon telo."),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    ├── NOUN_PHRASE",
                    '    │   ├── NOUN: "jan"',
                    "    │   └── ADJECTIVE_PHRASE",
                    '    │       └── ADJECTIVE: "mute"',
                    '    ├── PARTICLE: "li"',
                    "    ├── VERB_PHRASE",
                    '    │   ├── PREVERB: "sona"',
                    "    │   ├── ADJECTIVE_PHRASE",
                    '    │   │   └── ADJECTIVE: "ala"',
                    '    │   ├── VERB: "tawa"',
                    "    │   └── PREPOSITION_PHRASE",
                    '    │       ├── PREPOSITION: "lon"',
                    "    │       └── NOUN_PHRASE",
                    '    │           └── NOUN: "telo"',
                    "    └── .",
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("sina ken ala ken kama?"),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    ├── NOUN_PHRASE",
                    '    │   └── NOUN: "sina"',
                    "    ├── VERB_PHRASE",
                    '    │   ├── PREVERB: "ken"',
                    '    │   ├── PARTICLE: "ala"',
                    '    │   ├── PREVERB: "ken"',
                    '    │   └── VERB: "kama"',
                    "    └── ?",
                ],
            ),
        )
