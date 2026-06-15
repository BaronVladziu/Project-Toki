import unittest

from project_toki.grammar_parser import GrammarParser
from project_toki.phrase import Phrase
from project_toki.phrase_comparer import PhraseComparer


class TestGrammarPuOther(unittest.TestCase):
    COMPARER: PhraseComparer = PhraseComparer()

    def test_pu_proverbs(self):
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("ale li jo e tenpo."),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    ├── NOUN_PHRASE",
                    '    │   └── NOUN: "ale"',
                    '    ├── PARTICLE: "li"',
                    "    ├── VERB_PHRASE",
                    '    │   ├── VERB: "jo"',
                    '    │   ├── PARTICLE: "e"',
                    "    │   └── NOUN_PHRASE",
                    '    │       └── NOUN: "tenpo"',
                    "    └── .",
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("ale li pona."),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    ├── NOUN_PHRASE",
                    '    │   └── NOUN: "ale"',
                    '    ├── PARTICLE: "li"',
                    "    ├── VERB_PHRASE",
                    "    │   └── ADJECTIVE_PHRASE",
                    '    │       └── ADJECTIVE: "pona"',
                    "    └── .",
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("toki pona li toki pona."),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    ├── NOUN_PHRASE",
                    '    │   ├── NOUN: "toki"',
                    "    │   └── ADJECTIVE_PHRASE",
                    '    │       └── ADJECTIVE: "pona"',
                    '    ├── PARTICLE: "li"',
                    "    ├── VERB_PHRASE",
                    "    │   └── NOUN_PHRASE",
                    '    │       ├── NOUN: "toki"',
                    "    │       └── ADJECTIVE_PHRASE",
                    '    │           └── ADJECTIVE: "pona"',
                    "    └── .",
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("ante li kama."),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    ├── NOUN_PHRASE",
                    '    │   └── NOUN: "ante"',
                    '    ├── PARTICLE: "li"',
                    "    ├── VERB_PHRASE",
                    "    │   └── ADJECTIVE_PHRASE",
                    '    │       └── ADJECTIVE: "kama"',
                    "    └── .",
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("ike li kama."),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    ├── NOUN_PHRASE",
                    '    │   └── NOUN: "ike"',
                    '    ├── PARTICLE: "li"',
                    "    ├── VERB_PHRASE",
                    "    │   └── ADJECTIVE_PHRASE",
                    '    │       └── ADJECTIVE: "kama"',
                    "    └── .",
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("jan li suli mute. mani li suli lili."),
            Phrase.from_lines(
                [
                    "TEXT",
                    "├── SENTENCE",
                    "│   ├── NOUN_PHRASE",
                    '│   │   └── NOUN: "jan"',
                    '│   ├── PARTICLE: "li"',
                    "│   ├── VERB_PHRASE",
                    "│   │   └── NOUN_PHRASE",
                    '│   │       ├── NOUN: "suli"',
                    "│   │       └── ADJECTIVE_PHRASE",
                    '│   │           └── ADJECTIVE: "mute"',
                    "│   └── .",
                    "└── SENTENCE",
                    "    ├── NOUN_PHRASE",
                    '    │   └── NOUN: "mani"',
                    '    ├── PARTICLE: "li"',
                    "    ├── VERB_PHRASE",
                    "    │   └── NOUN_PHRASE",
                    '    │       ├── NOUN: "suli"',
                    "    │       └── ADJECTIVE_PHRASE",
                    '    │           └── ADJECTIVE: "lili"',
                    "    └── .",
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("jan sona li jan nasa."),
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
                    "    │   └── NOUN_PHRASE",
                    '    │       ├── NOUN: "jan"',
                    "    │       └── ADJECTIVE_PHRASE",
                    '    │           └── ADJECTIVE: "nasa"',
                    "    └── .",
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("lupa meli li mama pi ijo ale."),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    ├── NOUN_PHRASE",
                    '    │   ├── NOUN: "lupa"',
                    "    │   └── ADJECTIVE_PHRASE",
                    '    │       └── ADJECTIVE: "meli"',
                    '    ├── PARTICLE: "li"',
                    "    ├── VERB_PHRASE",
                    "    │   └── NOUN_PHRASE",
                    '    │       ├── NOUN: "mama"',
                    '    │       ├── PARTICLE: "pi"',
                    '    │       ├── NOUN: "ijo"',
                    "    │       └── ADJECTIVE_PHRASE",
                    '    │           └── ADJECTIVE: "ale"',
                    "    └── .",
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("mi pona e ale mi, la mi pona e mi."),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    ├── NOUN_PHRASE",
                    '    │   └── NOUN: "mi"',
                    "    ├── VERB_PHRASE",
                    '    │   ├── VERB: "pona"',
                    '    │   ├── PARTICLE: "e"',
                    "    │   └── NOUN_PHRASE",
                    '    │       ├── NOUN: "ale"',
                    "    │       └── ADJECTIVE_PHRASE",
                    '    │           └── ADJECTIVE: "mi"',
                    "    ├── ,",
                    '    ├── PARTICLE: "la"',
                    "    ├── NOUN_PHRASE",
                    '    │   └── NOUN: "mi"',
                    "    ├── VERB_PHRASE",
                    '    │   ├── VERB: "pona"',
                    '    │   ├── PARTICLE: "e"',
                    "    │   └── NOUN_PHRASE",
                    '    │       └── NOUN: "mi"',
                    "    └── .",
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("nasin pona li mute."),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    ├── NOUN_PHRASE",
                    '    │   ├── NOUN: "nasin"',
                    "    │   └── ADJECTIVE_PHRASE",
                    '    │       └── ADJECTIVE: "pona"',
                    '    ├── PARTICLE: "li"',
                    "    ├── VERB_PHRASE",
                    "    │   └── NUMBER_PHRASE",
                    '    │       └── NUMBER: "mute"',
                    "    └── .",
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("o olin e jan poka."),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    '    ├── PARTICLE: "o"',
                    "    ├── VERB_PHRASE",
                    '    │   ├── VERB: "olin"',
                    '    │   ├── PARTICLE: "e"',
                    "    │   └── NOUN_PHRASE",
                    '    │       ├── NOUN: "jan"',
                    "    │       └── ADJECTIVE_PHRASE",
                    '    │           └── ADJECTIVE: "poka"',
                    "    └── .",
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("o sona e sina!"),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    '    ├── PARTICLE: "o"',
                    "    ├── VERB_PHRASE",
                    '    │   ├── VERB: "sona"',
                    '    │   ├── PARTICLE: "e"',
                    "    │   └── NOUN_PHRASE",
                    '    │       └── NOUN: "sina"',
                    "    └── !",
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("pali li pana e sona."),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    ├── NOUN_PHRASE",
                    '    │   └── NOUN: "pali"',
                    '    ├── PARTICLE: "li"',
                    "    ├── VERB_PHRASE",
                    '    │   ├── VERB: "pana"',
                    '    │   ├── PARTICLE: "e"',
                    "    │   └── NOUN_PHRASE",
                    '    │       └── NOUN: "sona"',
                    "    └── .",
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("pilin pona li pana e sijelo pona."),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    ├── NOUN_PHRASE",
                    '    │   ├── NOUN: "pilin"',
                    "    │   └── ADJECTIVE_PHRASE",
                    '    │       └── ADJECTIVE: "pona"',
                    '    ├── PARTICLE: "li"',
                    "    ├── VERB_PHRASE",
                    '    │   ├── VERB: "pana"',
                    '    │   ├── PARTICLE: "e"',
                    "    │   └── NOUN_PHRASE",
                    '    │       ├── NOUN: "sijelo"',
                    "    │       └── ADJECTIVE_PHRASE",
                    '    │           └── ADJECTIVE: "pona"',
                    "    └── .",
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("sina pana e ike, la sina kama jo e ike."),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    ├── NOUN_PHRASE",
                    '    │   └── NOUN: "sina"',
                    "    ├── VERB_PHRASE",
                    '    │   ├── VERB: "pana"',
                    '    │   ├── PARTICLE: "e"',
                    "    │   └── NOUN_PHRASE",
                    '    │       └── NOUN: "ike"',
                    "    ├── ,",
                    '    ├── PARTICLE: "la"',
                    "    ├── NOUN_PHRASE",
                    '    │   └── NOUN: "sina"',
                    "    ├── VERB_PHRASE",
                    '    │   ├── PREVERB: "kama"',
                    '    │   ├── VERB: "jo"',
                    '    │   ├── PARTICLE: "e"',
                    "    │   └── NOUN_PHRASE",
                    '    │       └── NOUN: "ike"',
                    "    └── .",
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("wawa li lon insa."),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    ├── NOUN_PHRASE",
                    '    │   └── NOUN: "wawa"',
                    '    ├── PARTICLE: "li"',
                    "    ├── VERB_PHRASE",
                    "    │   └── PREPOSITION_PHRASE",
                    '    │       ├── PREPOSITION: "lon"',
                    "    │       └── NOUN_PHRASE",
                    '    │           └── NOUN: "insa"',
                    "    └── .",
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("weka lili li pona tawa lawa."),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    ├── NOUN_PHRASE",
                    '    │   ├── NOUN: "weka"',
                    "    │   └── ADJECTIVE_PHRASE",
                    '    │       └── ADJECTIVE: "lili"',
                    '    ├── PARTICLE: "li"',
                    "    ├── VERB_PHRASE",
                    '    │   ├── VERB: "pona"',
                    "    │   └── PREPOSITION_PHRASE",
                    '    │       ├── PREPOSITION: "tawa"',
                    "    │       └── NOUN_PHRASE",
                    '    │           └── NOUN: "lawa"',
                    "    └── .",
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("wile sona li mute e sona."),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    ├── NOUN_PHRASE",
                    '    │   ├── NOUN: "wile"',
                    "    │   └── ADJECTIVE_PHRASE",
                    '    │       └── ADJECTIVE: "sona"',
                    '    ├── PARTICLE: "li"',
                    "    ├── VERB_PHRASE",
                    '    │   ├── VERB: "mute"',
                    '    │   ├── PARTICLE: "e"',
                    "    │   └── NOUN_PHRASE",
                    '    │       └── NOUN: "sona"',
                    "    └── .",
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("jan lili li sona ala e ike."),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    ├── NOUN_PHRASE",
                    '    │   ├── NOUN: "jan"',
                    "    │   └── ADJECTIVE_PHRASE",
                    '    │       └── ADJECTIVE: "lili"',
                    '    ├── PARTICLE: "li"',
                    "    ├── VERB_PHRASE",
                    '    │   ├── VERB: "sona"',
                    "    │   ├── ADJECTIVE_PHRASE",
                    '    │   │   └── ADJECTIVE: "ala"',
                    '    │   ├── PARTICLE: "e"',
                    "    │   └── NOUN_PHRASE",
                    '    │       └── NOUN: "ike"',
                    "    └── .",
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("meli li nasa e mije."),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    ├── NOUN_PHRASE",
                    '    │   └── NOUN: "meli"',
                    '    ├── PARTICLE: "li"',
                    "    ├── VERB_PHRASE",
                    '    │   ├── VERB: "nasa"',
                    '    │   ├── PARTICLE: "e"',
                    "    │   └── NOUN_PHRASE",
                    '    │       └── NOUN: "mije"',
                    "    └── .",
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("mi weka e ike jan, la mi weka e ike mi."),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    ├── NOUN_PHRASE",
                    '    │   └── NOUN: "mi"',
                    "    ├── VERB_PHRASE",
                    '    │   ├── VERB: "weka"',
                    '    │   ├── PARTICLE: "e"',
                    "    │   └── NOUN_PHRASE",
                    '    │       ├── NOUN: "ike"',
                    "    │       └── ADJECTIVE_PHRASE",
                    '    │           └── ADJECTIVE: "jan"',
                    "    ├── ,",
                    '    ├── PARTICLE: "la"',
                    "    ├── NOUN_PHRASE",
                    '    │   └── NOUN: "mi"',
                    "    ├── VERB_PHRASE",
                    '    │   ├── VERB: "weka"',
                    '    │   ├── PARTICLE: "e"',
                    "    │   └── NOUN_PHRASE",
                    '    │       ├── NOUN: "ike"',
                    "    │       └── ADJECTIVE_PHRASE",
                    '    │           └── ADJECTIVE: "mi"',
                    "    └── .",
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("nasin ante li pona tawa jan ante."),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    ├── NOUN_PHRASE",
                    '    │   ├── NOUN: "nasin"',
                    "    │   └── ADJECTIVE_PHRASE",
                    '    │       └── ADJECTIVE: "ante"',
                    '    ├── PARTICLE: "li"',
                    "    ├── VERB_PHRASE",
                    '    │   ├── VERB: "pona"',
                    "    │   └── PREPOSITION_PHRASE",
                    '    │       ├── PREPOSITION: "tawa"',
                    "    │       └── NOUN_PHRASE",
                    '    │           ├── NOUN: "jan"',
                    "    │           └── ADJECTIVE_PHRASE",
                    '    │               └── ADJECTIVE: "ante"',
                    "    └── .",
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("telo li pona."),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    ├── NOUN_PHRASE",
                    '    │   └── NOUN: "telo"',
                    '    ├── PARTICLE: "li"',
                    "    ├── VERB_PHRASE",
                    "    │   └── ADJECTIVE_PHRASE",
                    '    │       └── ADJECTIVE: "pona"',
                    "    └── .",
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("lape li pona."),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    ├── NOUN_PHRASE",
                    '    │   └── NOUN: "lape"',
                    '    ├── PARTICLE: "li"',
                    "    ├── VERB_PHRASE",
                    "    │   └── ADJECTIVE_PHRASE",
                    '    │       └── ADJECTIVE: "pona"',
                    "    └── .",
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("toki li pona."),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    ├── NOUN_PHRASE",
                    '    │   └── NOUN: "toki"',
                    '    ├── PARTICLE: "li"',
                    "    ├── VERB_PHRASE",
                    "    │   └── ADJECTIVE_PHRASE",
                    '    │       └── ADJECTIVE: "pona"',
                    "    └── .",
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("o pana e pona tawa ma."),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    '    ├── PARTICLE: "o"',
                    "    ├── VERB_PHRASE",
                    '    │   ├── VERB: "pana"',
                    '    │   ├── PARTICLE: "e"',
                    "    │   ├── NOUN_PHRASE",
                    '    │   │   └── NOUN: "pona"',
                    "    │   └── PREPOSITION_PHRASE",
                    '    │       ├── PREPOSITION: "tawa"',
                    "    │       └── NOUN_PHRASE",
                    '    │           └── NOUN: "ma"',
                    "    └── .",
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("utala li ike."),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    ├── NOUN_PHRASE",
                    '    │   └── NOUN: "utala"',
                    '    ├── PARTICLE: "li"',
                    "    ├── VERB_PHRASE",
                    "    │   └── ADJECTIVE_PHRASE",
                    '    │       └── ADJECTIVE: "ike"',
                    "    └── .",
                ],
            ),
        )

        # ...
        # ...
        # ...
        # ...
        # ...
        # ...
        # ...
        # ...
        # ...

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
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("pona"),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    └── ADJECTIVE_PHRASE",
                    '        └── ADJECTIVE: "pona"',
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("pona tawa sina"),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    ├── NOUN_PHRASE",
                    '    │   └── NOUN: "pona"',
                    "    └── PREPOSITION_PHRASE",
                    '        ├── PREPOSITION: "tawa"',
                    "        └── NOUN_PHRASE",
                    '            └── NOUN: "sina"',
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("mi tawa"),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    ├── NOUN_PHRASE",
                    '    │   └── NOUN: "mi"',
                    "    └── VERB_PHRASE",
                    "        └── ADJECTIVE_PHRASE",
                    '            └── ADJECTIVE: "tawa"',
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("tawa pona"),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    └── PREPOSITION_PHRASE",
                    '        ├── PREPOSITION: "tawa"',
                    "        └── NOUN_PHRASE",
                    '            └── NOUN: "pona"',
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("ale li pona"),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    ├── NOUN_PHRASE",
                    '    │   └── NOUN: "ale"',
                    '    ├── PARTICLE: "li"',
                    "    └── VERB_PHRASE",
                    "        └── ADJECTIVE_PHRASE",
                    '            └── ADJECTIVE: "pona"',
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("ike a"),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    ├── ADJECTIVE_PHRASE",
                    '    │   └── ADJECTIVE: "ike"',
                    '    └── PARTICLE: "a"',
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("lape pona"),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    └── NOUN_PHRASE",
                    '        ├── NOUN: "lape"',
                    "        └── ADJECTIVE_PHRASE",
                    '            └── ADJECTIVE: "pona"',
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("kama pona"),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    └── NOUN_PHRASE",
                    '        ├── NOUN: "kama"',
                    "        └── ADJECTIVE_PHRASE",
                    '            └── ADJECTIVE: "pona"',
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("moku pona"),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    └── NOUN_PHRASE",
                    '        ├── NOUN: "moku"',
                    "        └── ADJECTIVE_PHRASE",
                    '            └── ADJECTIVE: "pona"',
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
            GrammarParser.parse_text("sina pilin seme?"),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    ├── NOUN_PHRASE",
                    '    │   └── NOUN: "sina"',
                    "    ├── VERB_PHRASE",
                    "    │   └── NOUN_PHRASE",
                    '    │       ├── NOUN: "pilin"',
                    "    │       └── ADJECTIVE_PHRASE",
                    '    │           └── ADJECTIVE: "seme"',
                    "    └── ?",
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("a a a!"),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    '    ├── PARTICLE: "a"',
                    '    ├── PARTICLE: "a"',
                    '    ├── PARTICLE: "a"',
                    "    └── !",
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("mi kama sona e toki pona"),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    ├── NOUN_PHRASE",
                    '    │   └── NOUN: "mi"',
                    "    └── VERB_PHRASE",
                    '        ├── PREVERB: "kama"',
                    '        ├── VERB: "sona"',
                    '        ├── PARTICLE: "e"',
                    "        └── NOUN_PHRASE",
                    '            ├── NOUN: "toki"',
                    "            └── ADJECTIVE_PHRASE",
                    '                └── ADJECTIVE: "pona"',
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("sina pona"),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    ├── NOUN_PHRASE",
                    '    │   └── NOUN: "sina"',
                    "    └── VERB_PHRASE",
                    "        └── ADJECTIVE_PHRASE",
                    '            └── ADJECTIVE: "pona"',
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("mi olin e sina"),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    ├── NOUN_PHRASE",
                    '    │   └── NOUN: "mi"',
                    "    └── VERB_PHRASE",
                    '        ├── VERB: "olin"',
                    '        ├── PARTICLE: "e"',
                    "        └── NOUN_PHRASE",
                    '            └── NOUN: "sina"',
                ],
            ),
        )
        self.COMPARER.compare_phrases(
            GrammarParser.parse_text("tomo telo li lon seme?"),
            Phrase.from_lines(
                [
                    "TEXT",
                    "└── SENTENCE",
                    "    ├── NOUN_PHRASE",
                    '    │   ├── NOUN: "tomo"',
                    "    │   └── ADJECTIVE_PHRASE",
                    '    │       └── ADJECTIVE: "telo"',
                    '    ├── PARTICLE: "li"',
                    "    ├── VERB_PHRASE",
                    "    │   └── PREPOSITION_PHRASE",
                    '    │       ├── PREPOSITION: "lon"',
                    "    │       └── NOUN_PHRASE",
                    '    │           └── NOUN: "seme"',
                    "    └── ?",
                ],
            ),
        )
