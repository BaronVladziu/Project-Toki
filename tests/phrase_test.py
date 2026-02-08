import unittest

from project_toki.part_of_speech import PartOfSpeech
from project_toki.phrase import Phrase
from project_toki.punctuation import Punctuation
from project_toki.word import Word


class TestPhrase(unittest.TestCase):
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
            """[
                1:
            ].rstrip(),
        )
