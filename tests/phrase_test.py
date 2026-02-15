import unittest

from project_toki.part_of_speech import PartOfSpeech
from project_toki.phrase import Phrase
from project_toki.punctuation import Punctuation
from project_toki.word import Word


class TestPhrase(unittest.TestCase):
    def _compare_trees(self, out_tree: Phrase, ref_tree: Phrase) -> None:
        self.assertEqual(out_tree, ref_tree, msg=f"\n{out_tree}\n!={ref_tree}")

    def test_constructors(self):
        phrase_as_str: str = str(
            """
TEXT
└── SENTENCE
    ├── NOUN_PHRASE
    │   ├── NOUN: "toki"
    │   └── ADJECTIVE_PHRASE
    │       └── ADJECTIVE: "pona"
    ├── PARTICLE: "li"
    ├── VERB_PHRASE
    │   └── ADJECTIVE_PHRASE
    │       └── ADJECTIVE: "pona"
    ├── PARTICLE: "a"
    └── !
        """,
        )
        phrase: Phrase = Phrase(
            "TEXT",
            children=[
                Phrase(
                    "SENTENCE",
                    children=[
                        Phrase(
                            "NOUN_PHRASE",
                            children=[
                                Phrase(Word("toki", PartOfSpeech.NOUN)),
                                Phrase(
                                    "ADJECTIVE_PHRASE",
                                    children=[
                                        Phrase(Word("pona", PartOfSpeech.ADJECTIVE)),
                                    ],
                                ),
                            ],
                        ),
                        Phrase(Word("li", PartOfSpeech.PARTICLE)),
                        Phrase(
                            "VERB_PHRASE",
                            children=[
                                Phrase(
                                    "ADJECTIVE_PHRASE",
                                    children=[
                                        Phrase(Word("pona", PartOfSpeech.ADJECTIVE)),
                                    ],
                                ),
                            ],
                        ),
                        Phrase(Word("a", PartOfSpeech.PARTICLE)),
                        Phrase(Punctuation("!")),
                    ],
                ),
            ],
        )
        self.assertEqual(
            str(phrase),
            phrase_as_str.strip(),
        )
        self._compare_trees(
            Phrase.from_str(phrase_as_str),
            phrase,
        )
        self._compare_trees(
            Phrase.from_lines(phrase_as_str.splitlines()),
            phrase,
        )

    def test_from_lines(self):
        self._compare_trees(
            Phrase.from_lines(
                [
                    "X",
                ],
            ),
            Phrase("X"),
        )
        self.assertRaises(
            ValueError,
            Phrase.from_lines,
            [
                "X",
                "X",
            ],
        )
        self._compare_trees(
            Phrase.from_lines(
                [
                    "X",
                    "└── X",
                ],
            ),
            Phrase(
                "X",
                children=[
                    Phrase("X"),
                ],
            ),
        )
        self.assertRaises(
            ValueError,
            Phrase.from_lines,
            [
                "X",
                "├── X",
            ],
        )
        self._compare_trees(
            Phrase.from_lines(
                [
                    "X",
                    "└── X",
                    "    └── X",
                ],
            ),
            Phrase(
                "X",
                children=[
                    Phrase(
                        "X",
                        children=[
                            Phrase("X"),
                        ],
                    ),
                ],
            ),
        )
        self.assertRaises(
            ValueError,
            Phrase.from_lines,
            [
                "X",
                "├── X",
                "│   └── X",
            ],
        )
        self.assertRaises(
            ValueError,
            Phrase.from_lines,
            [
                "X",
                "└── X",
                "    ├── X",
            ],
        )
        self.assertRaises(
            ValueError,
            Phrase.from_lines,
            [
                "X",
                "└── X",
                "│   └── X",
            ],
        )

    def test_diff(self):
        phrase1: Phrase = Phrase(
            "TEXT",
            children=[
                Phrase(
                    "SENTENCE",
                    children=[
                        Phrase(
                            "NOUN_PHRASE",
                            children=[
                                Phrase(Word("toki", PartOfSpeech.NOUN)),
                                Phrase(
                                    "ADJECTIVE_PHRASE",
                                    children=[
                                        Phrase(Word("pona", PartOfSpeech.ADJECTIVE)),
                                    ],
                                ),
                            ],
                        ),
                        Phrase(Word("li", PartOfSpeech.PARTICLE)),
                        Phrase(
                            "VERB_PHRASE",
                            children=[
                                Phrase(
                                    "ADJECTIVE_PHRASE",
                                    children=[
                                        Phrase(Word("pona", PartOfSpeech.ADJECTIVE)),
                                    ],
                                ),
                            ],
                        ),
                        Phrase(Word("a", PartOfSpeech.PARTICLE)),
                        Phrase(Punctuation("!")),
                    ],
                ),
            ],
        )
        phrase2: Phrase = Phrase(
            "TEXT",
            children=[
                Phrase(
                    "SENTENCE",
                    children=[
                        Phrase(
                            "NOUN_PHRASE",
                            children=[
                                Phrase(Word("toki", PartOfSpeech.NOUN)),
                                Phrase(
                                    "ADJECTIVE_PHRASE",
                                    children=[
                                        Phrase(Word("pona", PartOfSpeech.ADJECTIVE)),
                                    ],
                                ),
                            ],
                        ),
                        Phrase(Word("li", PartOfSpeech.PARTICLE)),
                        Phrase(
                            "VERB_PHRASE",
                            children=[
                                Phrase(
                                    "ADJECTIVE_PHRASE",
                                    children=[
                                        Phrase(Word("ike", PartOfSpeech.ADJECTIVE)),
                                    ],
                                ),
                            ],
                        ),
                        Phrase(Punctuation("!")),
                    ],
                ),
            ],
        )
        self.assertEqual(
            phrase1.get_diff(phrase2).rstrip(),
            """
  TEXT                              TEXT
  └── SENTENCE                      └── SENTENCE
      ├── NOUN_PHRASE                   ├── NOUN_PHRASE
      │   ├── NOUN: "toki"              │   ├── NOUN: "toki"
      │   └── ADJECTIVE_PHRASE          │   └── ADJECTIVE_PHRASE
      │       └── ADJECTIVE: "pona"     │       └── ADJECTIVE: "pona"
      ├── PARTICLE: "li"                ├── PARTICLE: "li"
      ├── VERB_PHRASE                   ├── VERB_PHRASE
      │   └── ADJECTIVE_PHRASE          │   └── ADJECTIVE_PHRASE
X     │       └── ADJECTIVE: "pona"     │       └── ADJECTIVE: "ike"
X     ├── PARTICLE: "a"                 └── !
X     └── !
            """.rstrip(),
        )
