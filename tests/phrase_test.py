import pytest

from project_toki.part_of_speech import PartOfSpeech
from project_toki.phrase import Phrase
from project_toki.phrase_comparer import PhraseComparer
from project_toki.punctuation import Punctuation
from project_toki.word import Word


class TestPhrase:
    COMPARER: PhraseComparer = PhraseComparer()

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
        assert str(phrase) == phrase_as_str.strip()
        self.COMPARER.compare_phrases(
            Phrase.from_str(phrase_as_str),
            phrase,
        )
        self.COMPARER.compare_phrases(
            Phrase.from_lines(phrase_as_str.splitlines()),
            phrase,
        )

    def test_from_lines(self):
        self.COMPARER.compare_phrases(
            Phrase.from_lines(
                [
                    "X",
                ],
            ),
            Phrase("X"),
        )
        with pytest.raises(ValueError):
            Phrase.from_lines(
                [
                    "X",
                    "X",
                ],
            )
        self.COMPARER.compare_phrases(
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
        with pytest.raises(ValueError):
            Phrase.from_lines(
                [
                    "X",
                    "├── X",
                ],
            )
        self.COMPARER.compare_phrases(
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
        with pytest.raises(ValueError):
            Phrase.from_lines(
                [
                    "X",
                    "├── X",
                    "│   └── X",
                ],
            )
        with pytest.raises(ValueError):
            Phrase.from_lines(
                [
                    "X",
                    "└── X",
                    "    ├── X",
                ],
            )
        with pytest.raises(ValueError):
            Phrase.from_lines(
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
        assert (
            phrase1.get_diff(phrase2).rstrip()
            == """
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
            """.rstrip()
        )
