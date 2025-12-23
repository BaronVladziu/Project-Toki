import unittest

from project_toki.grammar_parser import GrammarParser
from project_toki.part_of_speech import PartOfSpeech
from project_toki.phrase import Phrase
from project_toki.punctuation import Punctuation
from project_toki.word import Word


class TestGrammarParser(unittest.TestCase):
    def _compare_trees(self, out_tree: Phrase, ref_tree: Phrase) -> None:
        self.assertEqual(out_tree, ref_tree, msg=f"\n{out_tree}\n!={ref_tree}")

    def test_unknown_words(self):
        self._compare_trees(
            GrammarParser.parse_text("bleble pona"),
            Phrase(
                "TEXT",
                children=[
                    Phrase(
                        "SENTENCE",
                        children=[
                            Phrase(
                                "NOUN_PHRASE",
                                children=[
                                    Phrase(Word("bleble", PartOfSpeech.NOUN)),
                                    Phrase(
                                        "ADJECTIVE_PHRASE",
                                        children=[
                                            Phrase(
                                                Word("pona", PartOfSpeech.ADJECTIVE),
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                        ],
                    ),
                ],
            ),
        )

    def test_punctuation(self):
        self._compare_trees(
            GrammarParser.parse_text("mi, sina, ona."),
            Phrase(
                "TEXT",
                children=[
                    Phrase(
                        "SENTENCE",
                        children=[
                            Phrase(
                                "ADJECTIVE_PHRASE",
                                children=[
                                    Phrase(Word("mi", PartOfSpeech.ADJECTIVE)),
                                ],
                            ),
                            Phrase(Punctuation(",")),
                            Phrase(
                                "ADJECTIVE_PHRASE",
                                children=[
                                    Phrase(Word("sina", PartOfSpeech.ADJECTIVE)),
                                ],
                            ),
                            Phrase(Punctuation(",")),
                            Phrase(
                                "ADJECTIVE_PHRASE",
                                children=[
                                    Phrase(Word("ona", PartOfSpeech.ADJECTIVE)),
                                ],
                            ),
                            Phrase(Punctuation(".")),
                        ],
                    ),
                ],
            ),
        )
        self._compare_trees(
            GrammarParser.parse_text("kala - moku"),
            Phrase(
                "TEXT",
                children=[
                    Phrase(
                        "SENTENCE",
                        children=[
                            Phrase(
                                "ADJECTIVE_PHRASE",
                                children=[
                                    Phrase(Word("kala", PartOfSpeech.ADJECTIVE)),
                                ],
                            ),
                            Phrase(Punctuation("-")),
                            Phrase(
                                "ADJECTIVE_PHRASE",
                                children=[
                                    Phrase(Word("moku", PartOfSpeech.ADJECTIVE)),
                                ],
                            ),
                        ],
                    ),
                ],
            ),
        )
        self._compare_trees(
            GrammarParser.parse_text("wile? wile!"),
            Phrase(
                "TEXT",
                children=[
                    Phrase(
                        "SENTENCE",
                        children=[
                            Phrase(
                                "ADJECTIVE_PHRASE",
                                children=[
                                    Phrase(Word("wile", PartOfSpeech.ADJECTIVE)),
                                ],
                            ),
                            Phrase(Punctuation("?")),
                        ],
                    ),
                    Phrase(
                        "SENTENCE",
                        children=[
                            Phrase(
                                "ADJECTIVE_PHRASE",
                                children=[
                                    Phrase(Word("wile", PartOfSpeech.ADJECTIVE)),
                                ],
                            ),
                            Phrase(Punctuation("!")),
                        ],
                    ),
                ],
            ),
        )
        self._compare_trees(
            GrammarParser.parse_text("sina... awen"),
            Phrase(
                "TEXT",
                children=[
                    Phrase(
                        "SENTENCE",
                        children=[
                            Phrase(
                                "ADJECTIVE_PHRASE",
                                children=[
                                    Phrase(Word("sina", PartOfSpeech.ADJECTIVE)),
                                ],
                            ),
                            Phrase(Punctuation("...")),
                        ],
                    ),
                    Phrase(
                        "SENTENCE",
                        children=[
                            Phrase(
                                "ADJECTIVE_PHRASE",
                                children=[
                                    Phrase(Word("awen", PartOfSpeech.ADJECTIVE)),
                                ],
                            ),
                        ],
                    ),
                ],
            ),
        )

    def test_lesson_1(self):
        self._compare_trees(
            GrammarParser.parse_text("jelo"),
            Phrase(
                "TEXT",
                children=[
                    Phrase(
                        "SENTENCE",
                        children=[
                            Phrase(
                                "ADJECTIVE_PHRASE",
                                children=[
                                    Phrase(Word("jelo", PartOfSpeech.ADJECTIVE)),
                                ],
                            ),
                        ],
                    ),
                ],
            ),
        )
        self._compare_trees(
            GrammarParser.parse_text("toki"),
            Phrase(
                "TEXT",
                children=[
                    Phrase(
                        "SENTENCE",
                        children=[
                            Phrase(
                                "ADJECTIVE_PHRASE",
                                children=[
                                    Phrase(Word("toki", PartOfSpeech.ADJECTIVE)),
                                ],
                            ),
                        ],
                    ),
                ],
            ),
        )

    def test_lesson_2(self):
        self._compare_trees(
            GrammarParser.parse_text("ijo li ijo."),
            Phrase(
                "TEXT",
                children=[
                    Phrase(
                        "SENTENCE",
                        children=[
                            Phrase(
                                "NOUN_PHRASE",
                                children=[
                                    Phrase(Word("ijo", PartOfSpeech.NOUN)),
                                ],
                            ),
                            Phrase(Word("li", PartOfSpeech.PARTICLE)),
                            Phrase(
                                "VERB_PHRASE",
                                children=[
                                    Phrase(
                                        "ADJECTIVE_PHRASE",
                                        children=[
                                            Phrase(Word("ijo", PartOfSpeech.ADJECTIVE)),
                                        ],
                                    ),
                                ],
                            ),
                            Phrase(Punctuation(".")),
                        ],
                    ),
                ],
            ),
        )
        self._compare_trees(
            GrammarParser.parse_text("ni li jan."),
            Phrase(
                "TEXT",
                children=[
                    Phrase(
                        "SENTENCE",
                        children=[
                            Phrase(
                                "NOUN_PHRASE",
                                children=[
                                    Phrase(Word("ni", PartOfSpeech.NOUN)),
                                ],
                            ),
                            Phrase(Word("li", PartOfSpeech.PARTICLE)),
                            Phrase(
                                "VERB_PHRASE",
                                children=[
                                    Phrase(
                                        "ADJECTIVE_PHRASE",
                                        children=[
                                            Phrase(Word("jan", PartOfSpeech.ADJECTIVE)),
                                        ],
                                    ),
                                ],
                            ),
                            Phrase(Punctuation(".")),
                        ],
                    ),
                ],
            ),
        )
        self._compare_trees(
            GrammarParser.parse_text("ni li kili."),
            Phrase(
                "TEXT",
                children=[
                    Phrase(
                        "SENTENCE",
                        children=[
                            Phrase(
                                "NOUN_PHRASE",
                                children=[
                                    Phrase(Word("ni", PartOfSpeech.NOUN)),
                                ],
                            ),
                            Phrase(Word("li", PartOfSpeech.PARTICLE)),
                            Phrase(
                                "VERB_PHRASE",
                                children=[
                                    Phrase(
                                        "ADJECTIVE_PHRASE",
                                        children=[
                                            Phrase(
                                                Word("kili", PartOfSpeech.ADJECTIVE),
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            Phrase(Punctuation(".")),
                        ],
                    ),
                ],
            ),
        )
        self._compare_trees(
            GrammarParser.parse_text("lipu li ijo."),
            Phrase(
                "TEXT",
                children=[
                    Phrase(
                        "SENTENCE",
                        children=[
                            Phrase(
                                "NOUN_PHRASE",
                                children=[
                                    Phrase(Word("lipu", PartOfSpeech.NOUN)),
                                ],
                            ),
                            Phrase(Word("li", PartOfSpeech.PARTICLE)),
                            Phrase(
                                "VERB_PHRASE",
                                children=[
                                    Phrase(
                                        "ADJECTIVE_PHRASE",
                                        children=[
                                            Phrase(Word("ijo", PartOfSpeech.ADJECTIVE)),
                                        ],
                                    ),
                                ],
                            ),
                            Phrase(Punctuation(".")),
                        ],
                    ),
                ],
            ),
        )
        self._compare_trees(
            GrammarParser.parse_text("jan li meli."),
            Phrase(
                "TEXT",
                children=[
                    Phrase(
                        "SENTENCE",
                        children=[
                            Phrase(
                                "NOUN_PHRASE",
                                children=[
                                    Phrase(Word("jan", PartOfSpeech.NOUN)),
                                ],
                            ),
                            Phrase(Word("li", PartOfSpeech.PARTICLE)),
                            Phrase(
                                "VERB_PHRASE",
                                children=[
                                    Phrase(
                                        "ADJECTIVE_PHRASE",
                                        children=[
                                            Phrase(
                                                Word("meli", PartOfSpeech.ADJECTIVE),
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            Phrase(Punctuation(".")),
                        ],
                    ),
                ],
            ),
        )
        self._compare_trees(
            GrammarParser.parse_text("soweli li ijo."),
            Phrase(
                "TEXT",
                children=[
                    Phrase(
                        "SENTENCE",
                        children=[
                            Phrase(
                                "NOUN_PHRASE",
                                children=[
                                    Phrase(Word("soweli", PartOfSpeech.NOUN)),
                                ],
                            ),
                            Phrase(Word("li", PartOfSpeech.PARTICLE)),
                            Phrase(
                                "VERB_PHRASE",
                                children=[
                                    Phrase(
                                        "ADJECTIVE_PHRASE",
                                        children=[
                                            Phrase(Word("ijo", PartOfSpeech.ADJECTIVE)),
                                        ],
                                    ),
                                ],
                            ),
                            Phrase(Punctuation(".")),
                        ],
                    ),
                ],
            ),
        )
        self._compare_trees(
            GrammarParser.parse_text("meli li jan."),
            Phrase(
                "TEXT",
                children=[
                    Phrase(
                        "SENTENCE",
                        children=[
                            Phrase(
                                "NOUN_PHRASE",
                                children=[
                                    Phrase(Word("meli", PartOfSpeech.NOUN)),
                                ],
                            ),
                            Phrase(Word("li", PartOfSpeech.PARTICLE)),
                            Phrase(
                                "VERB_PHRASE",
                                children=[
                                    Phrase(
                                        "ADJECTIVE_PHRASE",
                                        children=[
                                            Phrase(Word("jan", PartOfSpeech.ADJECTIVE)),
                                        ],
                                    ),
                                ],
                            ),
                            Phrase(Punctuation(".")),
                        ],
                    ),
                ],
            ),
        )

    def test_lesson_3(self):
        self._compare_trees(
            GrammarParser.parse_text("ijo li pona."),
            Phrase(
                "TEXT",
                children=[
                    Phrase(
                        "SENTENCE",
                        children=[
                            Phrase(
                                "NOUN_PHRASE",
                                children=[
                                    Phrase(Word("ijo", PartOfSpeech.NOUN)),
                                ],
                            ),
                            Phrase(Word("li", PartOfSpeech.PARTICLE)),
                            Phrase(
                                "VERB_PHRASE",
                                children=[
                                    Phrase(
                                        "ADJECTIVE_PHRASE",
                                        children=[
                                            Phrase(
                                                Word("pona", PartOfSpeech.ADJECTIVE),
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            Phrase(Punctuation(".")),
                        ],
                    ),
                ],
            ),
        )
        self._compare_trees(
            GrammarParser.parse_text("tomo suli"),
            Phrase(
                "TEXT",
                children=[
                    Phrase(
                        "SENTENCE",
                        children=[
                            Phrase(
                                "NOUN_PHRASE",
                                children=[
                                    Phrase(Word("tomo", PartOfSpeech.NOUN)),
                                    Phrase(
                                        "ADJECTIVE_PHRASE",
                                        children=[
                                            Phrase(
                                                Word("suli", PartOfSpeech.ADJECTIVE),
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                        ],
                    ),
                ],
            ),
        )
        self._compare_trees(
            GrammarParser.parse_text("jan pona"),
            Phrase(
                "TEXT",
                children=[
                    Phrase(
                        "SENTENCE",
                        children=[
                            Phrase(
                                "NOUN_PHRASE",
                                children=[
                                    Phrase(Word("jan", PartOfSpeech.NOUN)),
                                    Phrase(
                                        "ADJECTIVE_PHRASE",
                                        children=[
                                            Phrase(
                                                Word("pona", PartOfSpeech.ADJECTIVE),
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                        ],
                    ),
                ],
            ),
        )
        self._compare_trees(
            GrammarParser.parse_text("meli lili"),
            Phrase(
                "TEXT",
                children=[
                    Phrase(
                        "SENTENCE",
                        children=[
                            Phrase(
                                "NOUN_PHRASE",
                                children=[
                                    Phrase(Word("meli", PartOfSpeech.NOUN)),
                                    Phrase(
                                        "ADJECTIVE_PHRASE",
                                        children=[
                                            Phrase(
                                                Word("lili", PartOfSpeech.ADJECTIVE),
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                        ],
                    ),
                ],
            ),
        )
        self._compare_trees(
            GrammarParser.parse_text("telo suli"),
            Phrase(
                "TEXT",
                children=[
                    Phrase(
                        "SENTENCE",
                        children=[
                            Phrase(
                                "NOUN_PHRASE",
                                children=[
                                    Phrase(Word("telo", PartOfSpeech.NOUN)),
                                    Phrase(
                                        "ADJECTIVE_PHRASE",
                                        children=[
                                            Phrase(
                                                Word("suli", PartOfSpeech.ADJECTIVE),
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                        ],
                    ),
                ],
            ),
        )
        self._compare_trees(
            GrammarParser.parse_text("lipu soweli"),
            Phrase(
                "TEXT",
                children=[
                    Phrase(
                        "SENTENCE",
                        children=[
                            Phrase(
                                "NOUN_PHRASE",
                                children=[
                                    Phrase(Word("lipu", PartOfSpeech.NOUN)),
                                    Phrase(
                                        "ADJECTIVE_PHRASE",
                                        children=[
                                            Phrase(
                                                Word("soweli", PartOfSpeech.ADJECTIVE),
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                        ],
                    ),
                ],
            ),
        )
        self._compare_trees(
            GrammarParser.parse_text("tomo meli"),
            Phrase(
                "TEXT",
                children=[
                    Phrase(
                        "SENTENCE",
                        children=[
                            Phrase(
                                "NOUN_PHRASE",
                                children=[
                                    Phrase(Word("tomo", PartOfSpeech.NOUN)),
                                    Phrase(
                                        "ADJECTIVE_PHRASE",
                                        children=[
                                            Phrase(
                                                Word("meli", PartOfSpeech.ADJECTIVE),
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                        ],
                    ),
                ],
            ),
        )
