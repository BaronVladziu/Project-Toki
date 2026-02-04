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
            GrammarParser.parse_text("masimelo pona"),
            Phrase(
                "TEXT",
                children=[
                    Phrase(
                        "SENTENCE",
                        children=[
                            Phrase(
                                "NOUN_PHRASE",
                                children=[
                                    Phrase(Word("masimelo", PartOfSpeech.NOUN)),
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

    def test_lesson_4(self):
        self._compare_trees(
            GrammarParser.parse_text("mi mije."),
            Phrase(
                "TEXT",
                children=[
                    Phrase(
                        "SENTENCE",
                        children=[
                            Phrase(
                                "NOUN_PHRASE",
                                children=[
                                    Phrase(Word("mi", PartOfSpeech.NOUN)),
                                ],
                            ),
                            Phrase(
                                "VERB_PHRASE",
                                children=[
                                    Phrase(
                                        "ADJECTIVE_PHRASE",
                                        children=[
                                            Phrase(
                                                Word("mije", PartOfSpeech.ADJECTIVE),
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
            GrammarParser.parse_text("sina sin."),
            Phrase(
                "TEXT",
                children=[
                    Phrase(
                        "SENTENCE",
                        children=[
                            Phrase(
                                "NOUN_PHRASE",
                                children=[
                                    Phrase(Word("sina", PartOfSpeech.NOUN)),
                                ],
                            ),
                            Phrase(
                                "VERB_PHRASE",
                                children=[
                                    Phrase(
                                        "ADJECTIVE_PHRASE",
                                        children=[
                                            Phrase(Word("sin", PartOfSpeech.ADJECTIVE)),
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
            GrammarParser.parse_text("tomo mi"),
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
                                            Phrase(Word("mi", PartOfSpeech.ADJECTIVE)),
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
            GrammarParser.parse_text("kulupu sina"),
            Phrase(
                "TEXT",
                children=[
                    Phrase(
                        "SENTENCE",
                        children=[
                            Phrase(
                                "NOUN_PHRASE",
                                children=[
                                    Phrase(Word("kulupu", PartOfSpeech.NOUN)),
                                    Phrase(
                                        "ADJECTIVE_PHRASE",
                                        children=[
                                            Phrase(
                                                Word("sina", PartOfSpeech.ADJECTIVE),
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
            GrammarParser.parse_text("tomo sina li sin."),
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
                                                Word("sina", PartOfSpeech.ADJECTIVE),
                                            ),
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
                                            Phrase(Word("sin", PartOfSpeech.ADJECTIVE)),
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
            GrammarParser.parse_text("mije li jan pona."),
            Phrase(
                "TEXT",
                children=[
                    Phrase(
                        "SENTENCE",
                        children=[
                            Phrase(
                                "NOUN_PHRASE",
                                children=[
                                    Phrase(Word("mije", PartOfSpeech.NOUN)),
                                ],
                            ),
                            Phrase(Word("li", PartOfSpeech.PARTICLE)),
                            Phrase(
                                "VERB_PHRASE",
                                children=[
                                    Phrase(
                                        "NOUN_PHRASE",
                                        children=[
                                            Phrase(Word("jan", PartOfSpeech.NOUN)),
                                            Phrase(
                                                "ADJECTIVE_PHRASE",
                                                children=[
                                                    Phrase(
                                                        Word(
                                                            "pona",
                                                            PartOfSpeech.ADJECTIVE,
                                                        ),
                                                    ),
                                                ],
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
            GrammarParser.parse_text("tomo soweli li lili."),
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
                                                Word("soweli", PartOfSpeech.ADJECTIVE),
                                            ),
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
                                            Phrase(
                                                Word("lili", PartOfSpeech.ADJECTIVE),
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
            GrammarParser.parse_text("sina mije wawa."),
            Phrase(
                "TEXT",
                children=[
                    Phrase(
                        "SENTENCE",
                        children=[
                            Phrase(
                                "NOUN_PHRASE",
                                children=[
                                    Phrase(Word("sina", PartOfSpeech.NOUN)),
                                ],
                            ),
                            Phrase(
                                "VERB_PHRASE",
                                children=[
                                    Phrase(
                                        "NOUN_PHRASE",
                                        children=[
                                            Phrase(Word("mije", PartOfSpeech.NOUN)),
                                            Phrase(
                                                "ADJECTIVE_PHRASE",
                                                children=[
                                                    Phrase(
                                                        Word(
                                                            "wawa",
                                                            PartOfSpeech.ADJECTIVE,
                                                        ),
                                                    ),
                                                ],
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
            GrammarParser.parse_text("kulupu sin li wawa."),
            Phrase(
                "TEXT",
                children=[
                    Phrase(
                        "SENTENCE",
                        children=[
                            Phrase(
                                "NOUN_PHRASE",
                                children=[
                                    Phrase(Word("kulupu", PartOfSpeech.NOUN)),
                                    Phrase(
                                        "ADJECTIVE_PHRASE",
                                        children=[
                                            Phrase(Word("sin", PartOfSpeech.ADJECTIVE)),
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
                                            Phrase(
                                                Word("wawa", PartOfSpeech.ADJECTIVE),
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
            GrammarParser.parse_text("ni li lipu sina."),
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
                                        "NOUN_PHRASE",
                                        children=[
                                            Phrase(Word("lipu", PartOfSpeech.NOUN)),
                                            Phrase(
                                                "ADJECTIVE_PHRASE",
                                                children=[
                                                    Phrase(
                                                        Word(
                                                            "sina",
                                                            PartOfSpeech.ADJECTIVE,
                                                        ),
                                                    ),
                                                ],
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

    def test_lesson_5(self):
        self._compare_trees(
            GrammarParser.parse_text("ijo li pali e ijo."),
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
                                    Phrase(Word("pali", PartOfSpeech.VERB)),
                                    Phrase(Word("e", PartOfSpeech.PARTICLE)),
                                    Phrase(
                                        "NOUN_PHRASE",
                                        children=[
                                            Phrase(Word("ijo", PartOfSpeech.NOUN)),
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
            GrammarParser.parse_text("mi moku e telo."),
            Phrase(
                "TEXT",
                children=[
                    Phrase(
                        "SENTENCE",
                        children=[
                            Phrase(
                                "NOUN_PHRASE",
                                children=[
                                    Phrase(Word("mi", PartOfSpeech.NOUN)),
                                ],
                            ),
                            Phrase(
                                "VERB_PHRASE",
                                children=[
                                    Phrase(Word("moku", PartOfSpeech.VERB)),
                                    Phrase(Word("e", PartOfSpeech.PARTICLE)),
                                    Phrase(
                                        "NOUN_PHRASE",
                                        children=[
                                            Phrase(Word("telo", PartOfSpeech.NOUN)),
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
            GrammarParser.parse_text("mije li sona."),
            Phrase(
                "TEXT",
                children=[
                    Phrase(
                        "SENTENCE",
                        children=[
                            Phrase(
                                "NOUN_PHRASE",
                                children=[
                                    Phrase(Word("mije", PartOfSpeech.NOUN)),
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
                                                Word("sona", PartOfSpeech.ADJECTIVE),
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
            GrammarParser.parse_text("mije li sona e ijo."),
            Phrase(
                "TEXT",
                children=[
                    Phrase(
                        "SENTENCE",
                        children=[
                            Phrase(
                                "NOUN_PHRASE",
                                children=[
                                    Phrase(Word("mije", PartOfSpeech.NOUN)),
                                ],
                            ),
                            Phrase(Word("li", PartOfSpeech.PARTICLE)),
                            Phrase(
                                "VERB_PHRASE",
                                children=[
                                    Phrase(Word("sona", PartOfSpeech.VERB)),
                                    Phrase(Word("e", PartOfSpeech.PARTICLE)),
                                    Phrase(
                                        "NOUN_PHRASE",
                                        children=[
                                            Phrase(Word("ijo", PartOfSpeech.NOUN)),
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
            GrammarParser.parse_text("mi sona e toki pona."),
            Phrase(
                "TEXT",
                children=[
                    Phrase(
                        "SENTENCE",
                        children=[
                            Phrase(
                                "NOUN_PHRASE",
                                children=[
                                    Phrase(Word("mi", PartOfSpeech.NOUN)),
                                ],
                            ),
                            Phrase(
                                "VERB_PHRASE",
                                children=[
                                    Phrase(Word("sona", PartOfSpeech.VERB)),
                                    Phrase(Word("e", PartOfSpeech.PARTICLE)),
                                    Phrase(
                                        "NOUN_PHRASE",
                                        children=[
                                            Phrase(Word("toki", PartOfSpeech.NOUN)),
                                            Phrase(
                                                "ADJECTIVE_PHRASE",
                                                children=[
                                                    Phrase(
                                                        Word(
                                                            "pona",
                                                            PartOfSpeech.ADJECTIVE,
                                                        ),
                                                    ),
                                                ],
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
            GrammarParser.parse_text("mije ni li jan toki."),
            Phrase(
                "TEXT",
                children=[
                    Phrase(
                        "SENTENCE",
                        children=[
                            Phrase(
                                "NOUN_PHRASE",
                                children=[
                                    Phrase(Word("mije", PartOfSpeech.NOUN)),
                                    Phrase(
                                        "ADJECTIVE_PHRASE",
                                        children=[
                                            Phrase(Word("ni", PartOfSpeech.ADJECTIVE)),
                                        ],
                                    ),
                                ],
                            ),
                            Phrase(Word("li", PartOfSpeech.PARTICLE)),
                            Phrase(
                                "VERB_PHRASE",
                                children=[
                                    Phrase(
                                        "NOUN_PHRASE",
                                        children=[
                                            Phrase(Word("jan", PartOfSpeech.NOUN)),
                                            Phrase(
                                                "ADJECTIVE_PHRASE",
                                                children=[
                                                    Phrase(
                                                        Word(
                                                            "toki",
                                                            PartOfSpeech.ADJECTIVE,
                                                        ),
                                                    ),
                                                ],
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
            GrammarParser.parse_text("soweli suli li moku e sina."),
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
                            Phrase(Word("li", PartOfSpeech.PARTICLE)),
                            Phrase(
                                "VERB_PHRASE",
                                children=[
                                    Phrase(Word("moku", PartOfSpeech.VERB)),
                                    Phrase(Word("e", PartOfSpeech.PARTICLE)),
                                    Phrase(
                                        "NOUN_PHRASE",
                                        children=[
                                            Phrase(Word("sina", PartOfSpeech.NOUN)),
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
            GrammarParser.parse_text("lipu kulupu li wawa."),
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
                                                Word("kulupu", PartOfSpeech.ADJECTIVE),
                                            ),
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
                                            Phrase(
                                                Word("wawa", PartOfSpeech.ADJECTIVE),
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
            GrammarParser.parse_text("sina pali e moku sin."),
            Phrase(
                "TEXT",
                children=[
                    Phrase(
                        "SENTENCE",
                        children=[
                            Phrase(
                                "NOUN_PHRASE",
                                children=[
                                    Phrase(Word("sina", PartOfSpeech.NOUN)),
                                ],
                            ),
                            Phrase(
                                "VERB_PHRASE",
                                children=[
                                    Phrase(Word("pali", PartOfSpeech.VERB)),
                                    Phrase(Word("e", PartOfSpeech.PARTICLE)),
                                    Phrase(
                                        "NOUN_PHRASE",
                                        children=[
                                            Phrase(Word("moku", PartOfSpeech.NOUN)),
                                            Phrase(
                                                "ADJECTIVE_PHRASE",
                                                children=[
                                                    Phrase(
                                                        Word(
                                                            "sin",
                                                            PartOfSpeech.ADJECTIVE,
                                                        ),
                                                    ),
                                                ],
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
            GrammarParser.parse_text("jan sona li kute."),
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
                                                Word("sona", PartOfSpeech.ADJECTIVE),
                                            ),
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
                                            Phrase(
                                                Word("kute", PartOfSpeech.ADJECTIVE),
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
            GrammarParser.parse_text("tomo sona li jo e lipu."),
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
                                                Word("sona", PartOfSpeech.ADJECTIVE),
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            Phrase(Word("li", PartOfSpeech.PARTICLE)),
                            Phrase(
                                "VERB_PHRASE",
                                children=[
                                    Phrase(Word("jo", PartOfSpeech.VERB)),
                                    Phrase(Word("e", PartOfSpeech.PARTICLE)),
                                    Phrase(
                                        "NOUN_PHRASE",
                                        children=[
                                            Phrase(Word("lipu", PartOfSpeech.NOUN)),
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

    def test_lesson_6(self):
        self._compare_trees(
            GrammarParser.parse_text("mi moku ala e soweli."),
            Phrase(
                "TEXT",
                children=[
                    Phrase(
                        "SENTENCE",
                        children=[
                            Phrase(
                                "NOUN_PHRASE",
                                children=[
                                    Phrase(Word("mi", PartOfSpeech.NOUN)),
                                ],
                            ),
                            Phrase(
                                "VERB_PHRASE",
                                children=[
                                    Phrase(Word("moku", PartOfSpeech.VERB)),
                                    Phrase(
                                        "ADJECTIVE_PHRASE",
                                        children=[
                                            Phrase(Word("ala", PartOfSpeech.ADJECTIVE)),
                                        ],
                                    ),
                                    Phrase(Word("e", PartOfSpeech.PARTICLE)),
                                    Phrase(
                                        "NOUN_PHRASE",
                                        children=[
                                            Phrase(Word("soweli", PartOfSpeech.NOUN)),
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
            GrammarParser.parse_text("mi toki pona e ijo."),
            Phrase(
                "TEXT",
                children=[
                    Phrase(
                        "SENTENCE",
                        children=[
                            Phrase(
                                "NOUN_PHRASE",
                                children=[
                                    Phrase(Word("mi", PartOfSpeech.NOUN)),
                                ],
                            ),
                            Phrase(
                                "VERB_PHRASE",
                                children=[
                                    Phrase(Word("toki", PartOfSpeech.VERB)),
                                    Phrase(
                                        "ADJECTIVE_PHRASE",
                                        children=[
                                            Phrase(
                                                Word("pona", PartOfSpeech.ADJECTIVE),
                                            ),
                                        ],
                                    ),
                                    Phrase(Word("e", PartOfSpeech.PARTICLE)),
                                    Phrase(
                                        "NOUN_PHRASE",
                                        children=[
                                            Phrase(Word("ijo", PartOfSpeech.NOUN)),
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
            GrammarParser.parse_text("pona mute"),
            Phrase(
                "TEXT",
                children=[
                    Phrase(
                        "SENTENCE",
                        children=[
                            Phrase(
                                "NOUN_PHRASE",
                                children=[
                                    Phrase(Word("pona", PartOfSpeech.NOUN)),
                                    Phrase(
                                        "ADJECTIVE_PHRASE",
                                        children=[
                                            Phrase(
                                                Word("mute", PartOfSpeech.ADJECTIVE),
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
            GrammarParser.parse_text("wawa lili"),
            Phrase(
                "TEXT",
                children=[
                    Phrase(
                        "SENTENCE",
                        children=[
                            Phrase(
                                "NOUN_PHRASE",
                                children=[
                                    Phrase(Word("wawa", PartOfSpeech.NOUN)),
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
            GrammarParser.parse_text("pali sina li pona mute."),
            Phrase(
                "TEXT",
                children=[
                    Phrase(
                        "SENTENCE",
                        children=[
                            Phrase(
                                "NOUN_PHRASE",
                                children=[
                                    Phrase(Word("pali", PartOfSpeech.NOUN)),
                                    Phrase(
                                        "ADJECTIVE_PHRASE",
                                        children=[
                                            Phrase(
                                                Word("sina", PartOfSpeech.ADJECTIVE),
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            Phrase(Word("li", PartOfSpeech.PARTICLE)),
                            Phrase(
                                "VERB_PHRASE",
                                children=[
                                    Phrase(
                                        "NOUN_PHRASE",
                                        children=[
                                            Phrase(Word("pona", PartOfSpeech.NOUN)),
                                            Phrase(
                                                "ADJECTIVE_PHRASE",
                                                children=[
                                                    Phrase(
                                                        Word(
                                                            "mute",
                                                            PartOfSpeech.ADJECTIVE,
                                                        ),
                                                    ),
                                                ],
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
            GrammarParser.parse_text("telo li wawa e mi."),
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
                                ],
                            ),
                            Phrase(Word("li", PartOfSpeech.PARTICLE)),
                            Phrase(
                                "VERB_PHRASE",
                                children=[
                                    Phrase(Word("wawa", PartOfSpeech.VERB)),
                                    Phrase(Word("e", PartOfSpeech.PARTICLE)),
                                    Phrase(
                                        "NOUN_PHRASE",
                                        children=[
                                            Phrase(Word("mi", PartOfSpeech.NOUN)),
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
            GrammarParser.parse_text("jan sona li pu."),
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
                                                Word("sona", PartOfSpeech.ADJECTIVE),
                                            ),
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
                                            Phrase(Word("pu", PartOfSpeech.ADJECTIVE)),
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
            GrammarParser.parse_text("meli lili li kute ike e mama."),
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
                            Phrase(Word("li", PartOfSpeech.PARTICLE)),
                            Phrase(
                                "VERB_PHRASE",
                                children=[
                                    Phrase(Word("kute", PartOfSpeech.VERB)),
                                    Phrase(
                                        "ADJECTIVE_PHRASE",
                                        children=[
                                            Phrase(Word("ike", PartOfSpeech.ADJECTIVE)),
                                        ],
                                    ),
                                    Phrase(Word("e", PartOfSpeech.PARTICLE)),
                                    Phrase(
                                        "NOUN_PHRASE",
                                        children=[
                                            Phrase(Word("mama", PartOfSpeech.NOUN)),
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
            GrammarParser.parse_text("sewi li wan."),
            Phrase(
                "TEXT",
                children=[
                    Phrase(
                        "SENTENCE",
                        children=[
                            Phrase(
                                "NOUN_PHRASE",
                                children=[
                                    Phrase(Word("sewi", PartOfSpeech.NOUN)),
                                ],
                            ),
                            Phrase(Word("li", PartOfSpeech.PARTICLE)),
                            Phrase(
                                "VERB_PHRASE",
                                children=[
                                    Phrase(
                                        "NUMBER_PHRASE",
                                        children=[
                                            Phrase(Word("wan", PartOfSpeech.NUMBER)),
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
            GrammarParser.parse_text("jan ala li ike."),
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
                                            Phrase(Word("ala", PartOfSpeech.ADJECTIVE)),
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
                            Phrase(Punctuation(".")),
                        ],
                    ),
                ],
            ),
        )
        self._compare_trees(
            GrammarParser.parse_text("mama mije li pu mute."),
            Phrase(
                "TEXT",
                children=[
                    Phrase(
                        "SENTENCE",
                        children=[
                            Phrase(
                                "NOUN_PHRASE",
                                children=[
                                    Phrase(Word("mama", PartOfSpeech.NOUN)),
                                    Phrase(
                                        "ADJECTIVE_PHRASE",
                                        children=[
                                            Phrase(
                                                Word("mije", PartOfSpeech.ADJECTIVE),
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            Phrase(Word("li", PartOfSpeech.PARTICLE)),
                            Phrase(
                                "VERB_PHRASE",
                                children=[
                                    Phrase(
                                        "NOUN_PHRASE",
                                        children=[
                                            Phrase(Word("pu", PartOfSpeech.NOUN)),
                                            Phrase(
                                                "ADJECTIVE_PHRASE",
                                                children=[
                                                    Phrase(
                                                        Word(
                                                            "mute",
                                                            PartOfSpeech.ADJECTIVE,
                                                        ),
                                                    ),
                                                ],
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

    def test_lesson_7(self):
        self._compare_trees(
            GrammarParser.parse_text("seme li sin?"),
            Phrase(
                "TEXT",
                children=[
                    Phrase(
                        "SENTENCE",
                        children=[
                            Phrase(
                                "NOUN_PHRASE",
                                children=[
                                    Phrase(Word("seme", PartOfSpeech.NOUN)),
                                ],
                            ),
                            Phrase(Word("li", PartOfSpeech.PARTICLE)),
                            Phrase(
                                "VERB_PHRASE",
                                children=[
                                    Phrase(
                                        "ADJECTIVE_PHRASE",
                                        children=[
                                            Phrase(Word("sin", PartOfSpeech.ADJECTIVE)),
                                        ],
                                    ),
                                ],
                            ),
                            Phrase(Punctuation("?")),
                        ],
                    ),
                ],
            ),
        )
        self._compare_trees(
            GrammarParser.parse_text("jan seme li toki?"),
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
                                                Word("seme", PartOfSpeech.ADJECTIVE),
                                            ),
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
                                            Phrase(
                                                Word("toki", PartOfSpeech.ADJECTIVE),
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            Phrase(Punctuation("?")),
                        ],
                    ),
                ],
            ),
        )
        self._compare_trees(
            GrammarParser.parse_text("sina pu anu seme?"),
            Phrase(
                "TEXT",
                children=[
                    Phrase(
                        "SENTENCE",
                        children=[
                            Phrase(
                                "NOUN_PHRASE",
                                children=[
                                    Phrase(Word("sina", PartOfSpeech.NOUN)),
                                ],
                            ),
                            Phrase(
                                "VERB_PHRASE",
                                children=[
                                    Phrase(
                                        "ADJECTIVE_PHRASE",
                                        children=[
                                            Phrase(Word("pu", PartOfSpeech.ADJECTIVE)),
                                        ],
                                    ),
                                ],
                            ),
                            Phrase(Word("anu", PartOfSpeech.PARTICLE)),
                            Phrase(Word("seme", PartOfSpeech.PARTICLE)),
                            Phrase(Punctuation("?")),
                        ],
                    ),
                ],
            ),
        )
        self._compare_trees(
            GrammarParser.parse_text("ona li mama ala mama?"),
            Phrase(
                "TEXT",
                children=[
                    Phrase(
                        "SENTENCE",
                        children=[
                            Phrase(
                                "NOUN_PHRASE",
                                children=[
                                    Phrase(Word("ona", PartOfSpeech.NOUN)),
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
                                                Word("mama", PartOfSpeech.ADJECTIVE),
                                            ),
                                            Phrase(Word("ala", PartOfSpeech.PARTICLE)),
                                            Phrase(
                                                Word("mama", PartOfSpeech.ADJECTIVE),
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            Phrase(Punctuation("?")),
                        ],
                    ),
                ],
            ),
        )
        self._compare_trees(
            GrammarParser.parse_text("mama."),
            Phrase(
                "TEXT",
                children=[
                    Phrase(
                        "SENTENCE",
                        children=[
                            Phrase(
                                "ADJECTIVE_PHRASE",
                                children=[
                                    Phrase(Word("mama", PartOfSpeech.ADJECTIVE)),
                                ],
                            ),
                            Phrase(Punctuation(".")),
                        ],
                    ),
                ],
            ),
        )
        self._compare_trees(
            GrammarParser.parse_text("mama ala."),
            Phrase(
                "TEXT",
                children=[
                    Phrase(
                        "SENTENCE",
                        children=[
                            Phrase(
                                "NOUN_PHRASE",
                                children=[
                                    Phrase(Word("mama", PartOfSpeech.NOUN)),
                                    Phrase(
                                        "ADJECTIVE_PHRASE",
                                        children=[
                                            Phrase(Word("ala", PartOfSpeech.ADJECTIVE)),
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
            GrammarParser.parse_text("ala."),
            Phrase(
                "TEXT",
                children=[
                    Phrase(
                        "SENTENCE",
                        children=[
                            Phrase(
                                "NUMBER_PHRASE",
                                children=[
                                    Phrase(Word("ala", PartOfSpeech.NUMBER)),
                                ],
                            ),
                            Phrase(Punctuation(".")),
                        ],
                    ),
                ],
            ),
        )
        self._compare_trees(
            GrammarParser.parse_text("ona li jo ala jo e kili mute?"),
            Phrase(
                "TEXT",
                children=[
                    Phrase(
                        "SENTENCE",
                        children=[
                            Phrase(
                                "NOUN_PHRASE",
                                children=[
                                    Phrase(Word("ona", PartOfSpeech.NOUN)),
                                ],
                            ),
                            Phrase(Word("li", PartOfSpeech.PARTICLE)),
                            Phrase(
                                "VERB_PHRASE",
                                children=[
                                    Phrase(Word("jo", PartOfSpeech.VERB)),
                                    Phrase(Word("ala", PartOfSpeech.PARTICLE)),
                                    Phrase(Word("jo", PartOfSpeech.VERB)),
                                    Phrase(Word("e", PartOfSpeech.PARTICLE)),
                                    Phrase(
                                        "NOUN_PHRASE",
                                        children=[
                                            Phrase(Word("kili", PartOfSpeech.NOUN)),
                                            Phrase(
                                                "ADJECTIVE_PHRASE",
                                                children=[
                                                    Phrase(
                                                        Word(
                                                            "mute",
                                                            PartOfSpeech.ADJECTIVE,
                                                        ),
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            Phrase(Punctuation("?")),
                        ],
                    ),
                ],
            ),
        )
        self._compare_trees(
            GrammarParser.parse_text("jo."),
            Phrase(
                "TEXT",
                children=[
                    Phrase(
                        "SENTENCE",
                        children=[
                            Phrase(
                                "ADJECTIVE_PHRASE",
                                children=[
                                    Phrase(Word("jo", PartOfSpeech.ADJECTIVE)),
                                ],
                            ),
                            Phrase(Punctuation(".")),
                        ],
                    ),
                ],
            ),
        )
        self._compare_trees(
            GrammarParser.parse_text("mije sona li jo e kala anu seme?"),
            Phrase(
                "TEXT",
                children=[
                    Phrase(
                        "SENTENCE",
                        children=[
                            Phrase(
                                "NOUN_PHRASE",
                                children=[
                                    Phrase(Word("mije", PartOfSpeech.NOUN)),
                                    Phrase(
                                        "ADJECTIVE_PHRASE",
                                        children=[
                                            Phrase(
                                                Word("sona", PartOfSpeech.ADJECTIVE),
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            Phrase(Word("li", PartOfSpeech.PARTICLE)),
                            Phrase(
                                "VERB_PHRASE",
                                children=[
                                    Phrase(Word("jo", PartOfSpeech.VERB)),
                                    Phrase(Word("e", PartOfSpeech.PARTICLE)),
                                    Phrase(
                                        "NOUN_PHRASE",
                                        children=[
                                            Phrase(Word("kala", PartOfSpeech.NOUN)),
                                        ],
                                    ),
                                ],
                            ),
                            Phrase(Word("anu", PartOfSpeech.PARTICLE)),
                            Phrase(Word("seme", PartOfSpeech.PARTICLE)),
                            Phrase(Punctuation("?")),
                        ],
                    ),
                ],
            ),
        )
        self._compare_trees(
            GrammarParser.parse_text("sina seme e ona?"),
            Phrase(
                "TEXT",
                children=[
                    Phrase(
                        "SENTENCE",
                        children=[
                            Phrase(
                                "NOUN_PHRASE",
                                children=[
                                    Phrase(Word("sina", PartOfSpeech.NOUN)),
                                ],
                            ),
                            Phrase(
                                "VERB_PHRASE",
                                children=[
                                    Phrase(Word("seme", PartOfSpeech.VERB)),
                                    Phrase(Word("e", PartOfSpeech.PARTICLE)),
                                    Phrase(
                                        "NOUN_PHRASE",
                                        children=[
                                            Phrase(Word("ona", PartOfSpeech.NOUN)),
                                        ],
                                    ),
                                ],
                            ),
                            Phrase(Punctuation("?")),
                        ],
                    ),
                ],
            ),
        )
        self._compare_trees(
            GrammarParser.parse_text("tomo li jo e ilo toki."),
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
                                ],
                            ),
                            Phrase(Word("li", PartOfSpeech.PARTICLE)),
                            Phrase(
                                "VERB_PHRASE",
                                children=[
                                    Phrase(Word("jo", PartOfSpeech.VERB)),
                                    Phrase(Word("e", PartOfSpeech.PARTICLE)),
                                    Phrase(
                                        "NOUN_PHRASE",
                                        children=[
                                            Phrase(Word("ilo", PartOfSpeech.NOUN)),
                                            Phrase(
                                                "ADJECTIVE_PHRASE",
                                                children=[
                                                    Phrase(
                                                        Word(
                                                            "toki",
                                                            PartOfSpeech.ADJECTIVE,
                                                        ),
                                                    ),
                                                ],
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
            GrammarParser.parse_text("sina kute ala kute e mama sina?"),
            Phrase(
                "TEXT",
                children=[
                    Phrase(
                        "SENTENCE",
                        children=[
                            Phrase(
                                "NOUN_PHRASE",
                                children=[
                                    Phrase(Word("sina", PartOfSpeech.NOUN)),
                                ],
                            ),
                            Phrase(
                                "VERB_PHRASE",
                                children=[
                                    Phrase(Word("kute", PartOfSpeech.VERB)),
                                    Phrase(Word("ala", PartOfSpeech.PARTICLE)),
                                    Phrase(Word("kute", PartOfSpeech.VERB)),
                                    Phrase(Word("e", PartOfSpeech.PARTICLE)),
                                    Phrase(
                                        "NOUN_PHRASE",
                                        children=[
                                            Phrase(Word("mama", PartOfSpeech.NOUN)),
                                            Phrase(
                                                "ADJECTIVE_PHRASE",
                                                children=[
                                                    Phrase(
                                                        Word(
                                                            "sina",
                                                            PartOfSpeech.ADJECTIVE,
                                                        ),
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            Phrase(Punctuation("?")),
                        ],
                    ),
                ],
            ),
        )
        self._compare_trees(
            GrammarParser.parse_text("kala wawa li moku e seme?"),
            Phrase(
                "TEXT",
                children=[
                    Phrase(
                        "SENTENCE",
                        children=[
                            Phrase(
                                "NOUN_PHRASE",
                                children=[
                                    Phrase(Word("kala", PartOfSpeech.NOUN)),
                                    Phrase(
                                        "ADJECTIVE_PHRASE",
                                        children=[
                                            Phrase(
                                                Word("wawa", PartOfSpeech.ADJECTIVE),
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            Phrase(Word("li", PartOfSpeech.PARTICLE)),
                            Phrase(
                                "VERB_PHRASE",
                                children=[
                                    Phrase(Word("moku", PartOfSpeech.VERB)),
                                    Phrase(Word("e", PartOfSpeech.PARTICLE)),
                                    Phrase(
                                        "NOUN_PHRASE",
                                        children=[
                                            Phrase(Word("seme", PartOfSpeech.NOUN)),
                                        ],
                                    ),
                                ],
                            ),
                            Phrase(Punctuation("?")),
                        ],
                    ),
                ],
            ),
        )

    def test_lesson_8(self):
        self._compare_trees(
            GrammarParser.parse_text("mi pana e kala tawa ona."),
            Phrase(
                "TEXT",
                children=[
                    Phrase(
                        "SENTENCE",
                        children=[
                            Phrase(
                                "NOUN_PHRASE",
                                children=[
                                    Phrase(Word("mi", PartOfSpeech.NOUN)),
                                ],
                            ),
                            Phrase(
                                "VERB_PHRASE",
                                children=[
                                    Phrase(Word("pana", PartOfSpeech.VERB)),
                                    Phrase(Word("e", PartOfSpeech.PARTICLE)),
                                    Phrase(
                                        "NOUN_PHRASE",
                                        children=[
                                            Phrase(Word("kala", PartOfSpeech.NOUN)),
                                        ],
                                    ),
                                    Phrase(
                                        "PREPOSITION_PHRASE",
                                        children=[
                                            Phrase(
                                                Word("tawa", PartOfSpeech.PREPOSITION),
                                            ),
                                            Phrase(
                                                "NOUN_PHRASE",
                                                children=[
                                                    Phrase(
                                                        Word("ona", PartOfSpeech.NOUN),
                                                    ),
                                                ],
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
            GrammarParser.parse_text("mi pana e kala lon tomo."),
            Phrase(
                "TEXT",
                children=[
                    Phrase(
                        "SENTENCE",
                        children=[
                            Phrase(
                                "NOUN_PHRASE",
                                children=[
                                    Phrase(Word("mi", PartOfSpeech.NOUN)),
                                ],
                            ),
                            Phrase(
                                "VERB_PHRASE",
                                children=[
                                    Phrase(Word("pana", PartOfSpeech.VERB)),
                                    Phrase(Word("e", PartOfSpeech.PARTICLE)),
                                    Phrase(
                                        "NOUN_PHRASE",
                                        children=[
                                            Phrase(Word("kala", PartOfSpeech.NOUN)),
                                        ],
                                    ),
                                    Phrase(
                                        "PREPOSITION_PHRASE",
                                        children=[
                                            Phrase(
                                                Word("lon", PartOfSpeech.PREPOSITION),
                                            ),
                                            Phrase(
                                                "NOUN_PHRASE",
                                                children=[
                                                    Phrase(
                                                        Word("tomo", PartOfSpeech.NOUN),
                                                    ),
                                                ],
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
            GrammarParser.parse_text("mi pana e kala tawa ona lon tomo."),
            Phrase(
                "TEXT",
                children=[
                    Phrase(
                        "SENTENCE",
                        children=[
                            Phrase(
                                "NOUN_PHRASE",
                                children=[
                                    Phrase(Word("mi", PartOfSpeech.NOUN)),
                                ],
                            ),
                            Phrase(
                                "VERB_PHRASE",
                                children=[
                                    Phrase(Word("pana", PartOfSpeech.VERB)),
                                    Phrase(Word("e", PartOfSpeech.PARTICLE)),
                                    Phrase(
                                        "NOUN_PHRASE",
                                        children=[
                                            Phrase(Word("kala", PartOfSpeech.NOUN)),
                                        ],
                                    ),
                                    Phrase(
                                        "PREPOSITION_PHRASE",
                                        children=[
                                            Phrase(
                                                Word("tawa", PartOfSpeech.PREPOSITION),
                                            ),
                                            Phrase(
                                                "NOUN_PHRASE",
                                                children=[
                                                    Phrase(
                                                        Word("ona", PartOfSpeech.NOUN),
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                    Phrase(
                                        "PREPOSITION_PHRASE",
                                        children=[
                                            Phrase(
                                                Word("lon", PartOfSpeech.PREPOSITION),
                                            ),
                                            Phrase(
                                                "NOUN_PHRASE",
                                                children=[
                                                    Phrase(
                                                        Word("tomo", PartOfSpeech.NOUN),
                                                    ),
                                                ],
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
            GrammarParser.parse_text("mi lon tomo."),
            Phrase(
                "TEXT",
                children=[
                    Phrase(
                        "SENTENCE",
                        children=[
                            Phrase(
                                "NOUN_PHRASE",
                                children=[
                                    Phrase(Word("mi", PartOfSpeech.NOUN)),
                                ],
                            ),
                            Phrase(
                                "VERB_PHRASE",
                                children=[
                                    Phrase(
                                        "PREPOSITION_PHRASE",
                                        children=[
                                            Phrase(
                                                Word("lon", PartOfSpeech.PREPOSITION),
                                            ),
                                            Phrase(
                                                "NOUN_PHRASE",
                                                children=[
                                                    Phrase(
                                                        Word("tomo", PartOfSpeech.NOUN),
                                                    ),
                                                ],
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
            GrammarParser.parse_text("mi tawa sina."),
            Phrase(
                "TEXT",
                children=[
                    Phrase(
                        "SENTENCE",
                        children=[
                            Phrase(
                                "NOUN_PHRASE",
                                children=[
                                    Phrase(Word("mi", PartOfSpeech.NOUN)),
                                ],
                            ),
                            Phrase(
                                "VERB_PHRASE",
                                children=[
                                    Phrase(
                                        "PREPOSITION_PHRASE",
                                        children=[
                                            Phrase(
                                                Word("tawa", PartOfSpeech.PREPOSITION),
                                            ),
                                            Phrase(
                                                "NOUN_PHRASE",
                                                children=[
                                                    Phrase(
                                                        Word("sina", PartOfSpeech.NOUN),
                                                    ),
                                                ],
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
            GrammarParser.parse_text("mama mi li tawa telo suli."),
            Phrase(
                "TEXT",
                children=[
                    Phrase(
                        "SENTENCE",
                        children=[
                            Phrase(
                                "NOUN_PHRASE",
                                children=[
                                    Phrase(Word("mama", PartOfSpeech.NOUN)),
                                    Phrase(
                                        "ADJECTIVE_PHRASE",
                                        children=[
                                            Phrase(Word("mi", PartOfSpeech.ADJECTIVE)),
                                        ],
                                    ),
                                ],
                            ),
                            Phrase(Word("li", PartOfSpeech.PARTICLE)),
                            Phrase(
                                "VERB_PHRASE",
                                children=[
                                    Phrase(
                                        "PREPOSITION_PHRASE",
                                        children=[
                                            Phrase(
                                                Word("tawa", PartOfSpeech.PREPOSITION),
                                            ),
                                            Phrase(
                                                "NOUN_PHRASE",
                                                children=[
                                                    Phrase(
                                                        Word("telo", PartOfSpeech.NOUN),
                                                    ),
                                                    Phrase(
                                                        "ADJECTIVE_PHRASE",
                                                        children=[
                                                            Phrase(
                                                                Word(
                                                                    "suli",
                                                                    PartOfSpeech.ADJECTIVE,
                                                                ),
                                                            ),
                                                        ],
                                                    ),
                                                ],
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
            GrammarParser.parse_text("mi pali mute tan ni."),
            Phrase(
                "TEXT",
                children=[
                    Phrase(
                        "SENTENCE",
                        children=[
                            Phrase(
                                "NOUN_PHRASE",
                                children=[
                                    Phrase(Word("mi", PartOfSpeech.NOUN)),
                                ],
                            ),
                            Phrase(
                                "VERB_PHRASE",
                                children=[
                                    Phrase(Word("pali", PartOfSpeech.VERB)),
                                    Phrase(
                                        "ADJECTIVE_PHRASE",
                                        children=[
                                            Phrase(
                                                Word("mute", PartOfSpeech.ADJECTIVE),
                                            ),
                                        ],
                                    ),
                                    Phrase(
                                        "PREPOSITION_PHRASE",
                                        children=[
                                            Phrase(
                                                Word("tan", PartOfSpeech.PREPOSITION),
                                            ),
                                            Phrase(
                                                "NOUN_PHRASE",
                                                children=[
                                                    Phrase(
                                                        Word("ni", PartOfSpeech.NOUN),
                                                    ),
                                                ],
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
            GrammarParser.parse_text("mi toki lon toki pona."),
            Phrase(
                "TEXT",
                children=[
                    Phrase(
                        "SENTENCE",
                        children=[
                            Phrase(
                                "NOUN_PHRASE",
                                children=[
                                    Phrase(Word("mi", PartOfSpeech.NOUN)),
                                ],
                            ),
                            Phrase(
                                "VERB_PHRASE",
                                children=[
                                    Phrase(Word("toki", PartOfSpeech.VERB)),
                                    Phrase(
                                        "PREPOSITION_PHRASE",
                                        children=[
                                            Phrase(
                                                Word("lon", PartOfSpeech.PREPOSITION),
                                            ),
                                            Phrase(
                                                "NOUN_PHRASE",
                                                children=[
                                                    Phrase(
                                                        Word("toki", PartOfSpeech.NOUN),
                                                    ),
                                                    Phrase(
                                                        "ADJECTIVE_PHRASE",
                                                        children=[
                                                            Phrase(
                                                                Word(
                                                                    "pona",
                                                                    PartOfSpeech.ADJECTIVE,
                                                                ),
                                                            ),
                                                        ],
                                                    ),
                                                ],
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
            GrammarParser.parse_text("soweli lili li pona tawa mi."),
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
                            Phrase(Word("li", PartOfSpeech.PARTICLE)),
                            Phrase(
                                "VERB_PHRASE",
                                children=[
                                    Phrase(Word("pona", PartOfSpeech.VERB)),
                                    Phrase(
                                        "PREPOSITION_PHRASE",
                                        children=[
                                            Phrase(
                                                Word("tawa", PartOfSpeech.PREPOSITION),
                                            ),
                                            Phrase(
                                                "NOUN_PHRASE",
                                                children=[
                                                    Phrase(
                                                        Word("mi", PartOfSpeech.NOUN),
                                                    ),
                                                ],
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
            GrammarParser.parse_text("kulupu pali li kepeken seme?"),
            Phrase(
                "TEXT",
                children=[
                    Phrase(
                        "SENTENCE",
                        children=[
                            Phrase(
                                "NOUN_PHRASE",
                                children=[
                                    Phrase(Word("kulupu", PartOfSpeech.NOUN)),
                                    Phrase(
                                        "ADJECTIVE_PHRASE",
                                        children=[
                                            Phrase(
                                                Word("pali", PartOfSpeech.ADJECTIVE),
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            Phrase(Word("li", PartOfSpeech.PARTICLE)),
                            Phrase(
                                "VERB_PHRASE",
                                children=[
                                    Phrase(
                                        "PREPOSITION_PHRASE",
                                        children=[
                                            Phrase(
                                                Word(
                                                    "kepeken",
                                                    PartOfSpeech.PREPOSITION,
                                                ),
                                            ),
                                            Phrase(
                                                "NOUN_PHRASE",
                                                children=[
                                                    Phrase(
                                                        Word("seme", PartOfSpeech.NOUN),
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            Phrase(Punctuation("?")),
                        ],
                    ),
                ],
            ),
        )
        self._compare_trees(
            GrammarParser.parse_text("mi sona e toki mute tan meli ni."),
            Phrase(
                "TEXT",
                children=[
                    Phrase(
                        "SENTENCE",
                        children=[
                            Phrase(
                                "NOUN_PHRASE",
                                children=[
                                    Phrase(Word("mi", PartOfSpeech.NOUN)),
                                ],
                            ),
                            Phrase(
                                "VERB_PHRASE",
                                children=[
                                    Phrase(Word("sona", PartOfSpeech.VERB)),
                                    Phrase(Word("e", PartOfSpeech.PARTICLE)),
                                    Phrase(
                                        "NOUN_PHRASE",
                                        children=[
                                            Phrase(Word("toki", PartOfSpeech.NOUN)),
                                            Phrase(
                                                "ADJECTIVE_PHRASE",
                                                children=[
                                                    Phrase(
                                                        Word(
                                                            "mute",
                                                            PartOfSpeech.ADJECTIVE,
                                                        ),
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                    Phrase(
                                        "PREPOSITION_PHRASE",
                                        children=[
                                            Phrase(
                                                Word("tan", PartOfSpeech.PREPOSITION),
                                            ),
                                            Phrase(
                                                "NOUN_PHRASE",
                                                children=[
                                                    Phrase(
                                                        Word("meli", PartOfSpeech.NOUN),
                                                    ),
                                                    Phrase(
                                                        "ADJECTIVE_PHRASE",
                                                        children=[
                                                            Phrase(
                                                                Word(
                                                                    "ni",
                                                                    PartOfSpeech.ADJECTIVE,
                                                                ),
                                                            ),
                                                        ],
                                                    ),
                                                ],
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
            GrammarParser.parse_text("mije sin li lon tomo telo anu seme?"),
            Phrase(
                "TEXT",
                children=[
                    Phrase(
                        "SENTENCE",
                        children=[
                            Phrase(
                                "NOUN_PHRASE",
                                children=[
                                    Phrase(Word("mije", PartOfSpeech.NOUN)),
                                    Phrase(
                                        "ADJECTIVE_PHRASE",
                                        children=[
                                            Phrase(Word("sin", PartOfSpeech.ADJECTIVE)),
                                        ],
                                    ),
                                ],
                            ),
                            Phrase(Word("li", PartOfSpeech.PARTICLE)),
                            Phrase(
                                "VERB_PHRASE",
                                children=[
                                    Phrase(
                                        "PREPOSITION_PHRASE",
                                        children=[
                                            Phrase(
                                                Word("lon", PartOfSpeech.PREPOSITION),
                                            ),
                                            Phrase(
                                                "NOUN_PHRASE",
                                                children=[
                                                    Phrase(
                                                        Word("tomo", PartOfSpeech.NOUN),
                                                    ),
                                                    Phrase(
                                                        "ADJECTIVE_PHRASE",
                                                        children=[
                                                            Phrase(
                                                                Word(
                                                                    "telo",
                                                                    PartOfSpeech.ADJECTIVE,
                                                                ),
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            Phrase(Word("anu", PartOfSpeech.PARTICLE)),
                            Phrase(Word("seme", PartOfSpeech.PARTICLE)),
                            Phrase(Punctuation("?")),
                        ],
                    ),
                ],
            ),
        )

    def test_lesson_9(self):
        self._compare_trees(
            GrammarParser.parse_text("ma tomo"),
            Phrase(
                "TEXT",
                children=[
                    Phrase(
                        "SENTENCE",
                        children=[
                            Phrase(
                                "NOUN_PHRASE",
                                children=[
                                    Phrase(Word("ma", PartOfSpeech.NOUN)),
                                    Phrase(
                                        "ADJECTIVE_PHRASE",
                                        children=[
                                            Phrase(
                                                Word("tomo", PartOfSpeech.ADJECTIVE),
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
            GrammarParser.parse_text("ma tomo Isanpu"),
            Phrase(
                "TEXT",
                children=[
                    Phrase(
                        "SENTENCE",
                        children=[
                            Phrase(
                                "NOUN_PHRASE",
                                children=[
                                    Phrase(Word("ma", PartOfSpeech.NOUN)),
                                    Phrase(
                                        "ADJECTIVE_PHRASE",
                                        children=[
                                            Phrase(
                                                Word("tomo", PartOfSpeech.ADJECTIVE),
                                            ),
                                            Phrase(
                                                Word("Isanpu", PartOfSpeech.ADJECTIVE),
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
            GrammarParser.parse_text("nimi mi li Apu."),
            Phrase(
                "TEXT",
                children=[
                    Phrase(
                        "SENTENCE",
                        children=[
                            Phrase(
                                "NOUN_PHRASE",
                                children=[
                                    Phrase(Word("nimi", PartOfSpeech.NOUN)),
                                    Phrase(
                                        "ADJECTIVE_PHRASE",
                                        children=[
                                            Phrase(Word("mi", PartOfSpeech.ADJECTIVE)),
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
                                            Phrase(Word("Apu", PartOfSpeech.ADJECTIVE)),
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
            GrammarParser.parse_text("ma Apika li jo e jan mute."),
            Phrase(
                "TEXT",
                children=[
                    Phrase(
                        "SENTENCE",
                        children=[
                            Phrase(
                                "NOUN_PHRASE",
                                children=[
                                    Phrase(Word("ma", PartOfSpeech.NOUN)),
                                    Phrase(
                                        "ADJECTIVE_PHRASE",
                                        children=[
                                            Phrase(
                                                Word("Apika", PartOfSpeech.ADJECTIVE),
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            Phrase(Word("li", PartOfSpeech.PARTICLE)),
                            Phrase(
                                "VERB_PHRASE",
                                children=[
                                    Phrase(Word("jo", PartOfSpeech.VERB)),
                                    Phrase(Word("e", PartOfSpeech.PARTICLE)),
                                    Phrase(
                                        "NOUN_PHRASE",
                                        children=[
                                            Phrase(Word("jan", PartOfSpeech.NOUN)),
                                            Phrase(
                                                "ADJECTIVE_PHRASE",
                                                children=[
                                                    Phrase(
                                                        Word(
                                                            "mute",
                                                            PartOfSpeech.ADJECTIVE,
                                                        ),
                                                    ),
                                                ],
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
            GrammarParser.parse_text("meli Sonko li tawa nasin Kuwin."),
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
                                                Word("Sonko", PartOfSpeech.ADJECTIVE),
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            Phrase(Word("li", PartOfSpeech.PARTICLE)),
                            Phrase(
                                "VERB_PHRASE",
                                children=[
                                    Phrase(
                                        "PREPOSITION_PHRASE",
                                        children=[
                                            Phrase(
                                                Word("tawa", PartOfSpeech.PREPOSITION),
                                            ),
                                            Phrase(
                                                "NOUN_PHRASE",
                                                children=[
                                                    Phrase(
                                                        Word(
                                                            "nasin",
                                                            PartOfSpeech.NOUN,
                                                        ),
                                                    ),
                                                    Phrase(
                                                        "ADJECTIVE_PHRASE",
                                                        children=[
                                                            Phrase(
                                                                Word(
                                                                    "Kuwin",
                                                                    PartOfSpeech.ADJECTIVE,
                                                                ),
                                                            ),
                                                        ],
                                                    ),
                                                ],
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
            GrammarParser.parse_text("jan Epawam Linkan li tan ma Mewika."),
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
                                                Word("Epawam", PartOfSpeech.ADJECTIVE),
                                            ),
                                            Phrase(
                                                Word("Linkan", PartOfSpeech.ADJECTIVE),
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            Phrase(Word("li", PartOfSpeech.PARTICLE)),
                            Phrase(
                                "VERB_PHRASE",
                                children=[
                                    Phrase(
                                        "PREPOSITION_PHRASE",
                                        children=[
                                            Phrase(
                                                Word("tan", PartOfSpeech.PREPOSITION),
                                            ),
                                            Phrase(
                                                "NOUN_PHRASE",
                                                children=[
                                                    Phrase(
                                                        Word("ma", PartOfSpeech.NOUN),
                                                    ),
                                                    Phrase(
                                                        "ADJECTIVE_PHRASE",
                                                        children=[
                                                            Phrase(
                                                                Word(
                                                                    "Mewika",
                                                                    PartOfSpeech.ADJECTIVE,
                                                                ),
                                                            ),
                                                        ],
                                                    ),
                                                ],
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
            GrammarParser.parse_text("ma tomo Pelin li lon ma Tosi."),
            Phrase(
                "TEXT",
                children=[
                    Phrase(
                        "SENTENCE",
                        children=[
                            Phrase(
                                "NOUN_PHRASE",
                                children=[
                                    Phrase(Word("ma", PartOfSpeech.NOUN)),
                                    Phrase(
                                        "ADJECTIVE_PHRASE",
                                        children=[
                                            Phrase(
                                                Word("tomo", PartOfSpeech.ADJECTIVE),
                                            ),
                                            Phrase(
                                                Word("Pelin", PartOfSpeech.ADJECTIVE),
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            Phrase(Word("li", PartOfSpeech.PARTICLE)),
                            Phrase(
                                "VERB_PHRASE",
                                children=[
                                    Phrase(
                                        "PREPOSITION_PHRASE",
                                        children=[
                                            Phrase(
                                                Word("lon", PartOfSpeech.PREPOSITION),
                                            ),
                                            Phrase(
                                                "NOUN_PHRASE",
                                                children=[
                                                    Phrase(
                                                        Word("ma", PartOfSpeech.NOUN),
                                                    ),
                                                    Phrase(
                                                        "ADJECTIVE_PHRASE",
                                                        children=[
                                                            Phrase(
                                                                Word(
                                                                    "Tosi",
                                                                    PartOfSpeech.ADJECTIVE,
                                                                ),
                                                            ),
                                                        ],
                                                    ),
                                                ],
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
            GrammarParser.parse_text("sina sona ala sona e toki Inli?"),
            Phrase(
                "TEXT",
                children=[
                    Phrase(
                        "SENTENCE",
                        children=[
                            Phrase(
                                "NOUN_PHRASE",
                                children=[
                                    Phrase(Word("sina", PartOfSpeech.NOUN)),
                                ],
                            ),
                            Phrase(
                                "VERB_PHRASE",
                                children=[
                                    Phrase(Word("sona", PartOfSpeech.VERB)),
                                    Phrase(Word("ala", PartOfSpeech.PARTICLE)),
                                    Phrase(Word("sona", PartOfSpeech.VERB)),
                                    Phrase(Word("e", PartOfSpeech.PARTICLE)),
                                    Phrase(
                                        "NOUN_PHRASE",
                                        children=[
                                            Phrase(Word("toki", PartOfSpeech.NOUN)),
                                            Phrase(
                                                "ADJECTIVE_PHRASE",
                                                children=[
                                                    Phrase(
                                                        Word(
                                                            "Inli",
                                                            PartOfSpeech.ADJECTIVE,
                                                        ),
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            Phrase(Punctuation("?")),
                        ],
                    ),
                ],
            ),
        )
        self._compare_trees(
            GrammarParser.parse_text("nena sewi Kepelitepe li lon ma Tuki."),
            Phrase(
                "TEXT",
                children=[
                    Phrase(
                        "SENTENCE",
                        children=[
                            Phrase(
                                "NOUN_PHRASE",
                                children=[
                                    Phrase(Word("nena", PartOfSpeech.NOUN)),
                                    Phrase(
                                        "ADJECTIVE_PHRASE",
                                        children=[
                                            Phrase(
                                                Word("sewi", PartOfSpeech.ADJECTIVE),
                                            ),
                                            Phrase(
                                                Word(
                                                    "Kepelitepe",
                                                    PartOfSpeech.ADJECTIVE,
                                                ),
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            Phrase(Word("li", PartOfSpeech.PARTICLE)),
                            Phrase(
                                "VERB_PHRASE",
                                children=[
                                    Phrase(
                                        "PREPOSITION_PHRASE",
                                        children=[
                                            Phrase(
                                                Word("lon", PartOfSpeech.PREPOSITION),
                                            ),
                                            Phrase(
                                                "NOUN_PHRASE",
                                                children=[
                                                    Phrase(
                                                        Word("ma", PartOfSpeech.NOUN),
                                                    ),
                                                    Phrase(
                                                        "ADJECTIVE_PHRASE",
                                                        children=[
                                                            Phrase(
                                                                Word(
                                                                    "Tuki",
                                                                    PartOfSpeech.ADJECTIVE,
                                                                ),
                                                            ),
                                                        ],
                                                    ),
                                                ],
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

    def test_lesson_10(self):
        self._compare_trees(
            GrammarParser.parse_text("toki!"),
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
                            Phrase(Punctuation("!")),
                        ],
                    ),
                ],
            ),
        )
        self._compare_trees(
            GrammarParser.parse_text("pona tawa sina!"),
            Phrase(
                "TEXT",
                children=[
                    Phrase(
                        "SENTENCE",
                        children=[
                            Phrase(
                                "ADJECTIVE_PHRASE",
                                children=[
                                    Phrase(Word("pona", PartOfSpeech.ADJECTIVE)),
                                ],
                            ),
                            Phrase(
                                "PREPOSITION_PHRASE",
                                children=[
                                    Phrase(Word("tawa", PartOfSpeech.PREPOSITION)),
                                    Phrase(
                                        "NOUN_PHRASE",
                                        children=[
                                            Phrase(Word("sina", PartOfSpeech.NOUN)),
                                        ],
                                    ),
                                ],
                            ),
                            Phrase(Punctuation("!")),
                        ],
                    ),
                ],
            ),
        )
        self._compare_trees(
            GrammarParser.parse_text("kama pona!"),
            Phrase(
                "TEXT",
                children=[
                    Phrase(
                        "SENTENCE",
                        children=[
                            Phrase(
                                "NOUN_PHRASE",
                                children=[
                                    Phrase(Word("kama", PartOfSpeech.NOUN)),
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
                            Phrase(Punctuation("!")),
                        ],
                    ),
                ],
            ),
        )
        self._compare_trees(
            GrammarParser.parse_text("seme li sin?"),
            Phrase(
                "TEXT",
                children=[
                    Phrase(
                        "SENTENCE",
                        children=[
                            Phrase(
                                "NOUN_PHRASE",
                                children=[
                                    Phrase(Word("seme", PartOfSpeech.NOUN)),
                                ],
                            ),
                            Phrase(Word("li", PartOfSpeech.PARTICLE)),
                            Phrase(
                                "VERB_PHRASE",
                                children=[
                                    Phrase(
                                        "ADJECTIVE_PHRASE",
                                        children=[
                                            Phrase(Word("sin", PartOfSpeech.ADJECTIVE)),
                                        ],
                                    ),
                                ],
                            ),
                            Phrase(Punctuation("?")),
                        ],
                    ),
                ],
            ),
        )
        self._compare_trees(
            GrammarParser.parse_text("mi tawa."),
            Phrase(
                "TEXT",
                children=[
                    Phrase(
                        "SENTENCE",
                        children=[
                            Phrase(
                                "NOUN_PHRASE",
                                children=[
                                    Phrase(Word("mi", PartOfSpeech.NOUN)),
                                ],
                            ),
                            Phrase(
                                "VERB_PHRASE",
                                children=[
                                    Phrase(
                                        "ADJECTIVE_PHRASE",
                                        children=[
                                            Phrase(
                                                Word("tawa", PartOfSpeech.ADJECTIVE),
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
            GrammarParser.parse_text("tawa pona."),
            Phrase(
                "TEXT",
                children=[
                    Phrase(
                        "SENTENCE",
                        children=[
                            Phrase(
                                "PREPOSITION_PHRASE",
                                children=[
                                    Phrase(Word("tawa", PartOfSpeech.PREPOSITION)),
                                    Phrase(
                                        "NOUN_PHRASE",
                                        children=[
                                            Phrase(Word("pona", PartOfSpeech.NOUN)),
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
            GrammarParser.parse_text("o toki ala. o pali."),
            Phrase(
                "TEXT",
                children=[
                    Phrase(
                        "SENTENCE",
                        children=[
                            Phrase(Word("o", PartOfSpeech.PARTICLE)),
                            Phrase(
                                "VERB_PHRASE",
                                children=[
                                    Phrase(Word("toki", PartOfSpeech.VERB)),
                                    Phrase(
                                        "ADJECTIVE_PHRASE",
                                        children=[
                                            Phrase(Word("ala", PartOfSpeech.ADJECTIVE)),
                                        ],
                                    ),
                                ],
                            ),
                            Phrase(Punctuation(".")),
                        ],
                    ),
                    Phrase(
                        "SENTENCE",
                        children=[
                            Phrase(Word("o", PartOfSpeech.PARTICLE)),
                            Phrase(
                                "VERB_PHRASE",
                                children=[
                                    Phrase(Word("pali", PartOfSpeech.VERB)),
                                ],
                            ),
                            Phrase(Punctuation(".")),
                        ],
                    ),
                ],
            ),
        )
        self._compare_trees(
            GrammarParser.parse_text("jan Mosima o, ni li soweli sina anu seme?"),
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
                                                Word("Mosima", PartOfSpeech.ADJECTIVE),
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            Phrase(Word("o", PartOfSpeech.PARTICLE)),
                            Phrase(Punctuation(",")),
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
                                        "NOUN_PHRASE",
                                        children=[
                                            Phrase(Word("soweli", PartOfSpeech.NOUN)),
                                            Phrase(
                                                "ADJECTIVE_PHRASE",
                                                children=[
                                                    Phrase(
                                                        Word(
                                                            "sina",
                                                            PartOfSpeech.ADJECTIVE,
                                                        ),
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            Phrase(Word("anu", PartOfSpeech.PARTICLE)),
                            Phrase(Word("seme", PartOfSpeech.PARTICLE)),
                            Phrase(Punctuation("?")),
                        ],
                    ),
                ],
            ),
        )
        self._compare_trees(
            GrammarParser.parse_text("o moku ala e kili mi."),
            Phrase(
                "TEXT",
                children=[
                    Phrase(
                        "SENTENCE",
                        children=[
                            Phrase(Word("o", PartOfSpeech.PARTICLE)),
                            Phrase(
                                "VERB_PHRASE",
                                children=[
                                    Phrase(Word("moku", PartOfSpeech.VERB)),
                                    Phrase(
                                        "ADJECTIVE_PHRASE",
                                        children=[
                                            Phrase(Word("ala", PartOfSpeech.ADJECTIVE)),
                                        ],
                                    ),
                                    Phrase(Word("e", PartOfSpeech.PARTICLE)),
                                    Phrase(
                                        "NOUN_PHRASE",
                                        children=[
                                            Phrase(Word("kili", PartOfSpeech.NOUN)),
                                            Phrase(
                                                "ADJECTIVE_PHRASE",
                                                children=[
                                                    Phrase(
                                                        Word(
                                                            "mi",
                                                            PartOfSpeech.ADJECTIVE,
                                                        ),
                                                    ),
                                                ],
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
            GrammarParser.parse_text("sina pilin ike tan seme?"),
            Phrase(
                "TEXT",
                children=[
                    Phrase(
                        "SENTENCE",
                        children=[
                            Phrase(
                                "NOUN_PHRASE",
                                children=[
                                    Phrase(Word("sina", PartOfSpeech.NOUN)),
                                ],
                            ),
                            Phrase(
                                "VERB_PHRASE",
                                children=[
                                    Phrase(Word("pilin", PartOfSpeech.VERB)),
                                    Phrase(
                                        "ADJECTIVE_PHRASE",
                                        children=[
                                            Phrase(Word("ike", PartOfSpeech.ADJECTIVE)),
                                        ],
                                    ),
                                    Phrase(
                                        "PREPOSITION_PHRASE",
                                        children=[
                                            Phrase(
                                                Word("tan", PartOfSpeech.PREPOSITION),
                                            ),
                                            Phrase(
                                                "NOUN_PHRASE",
                                                children=[
                                                    Phrase(
                                                        Word("seme", PartOfSpeech.NOUN),
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            Phrase(Punctuation("?")),
                        ],
                    ),
                ],
            ),
        )
        self._compare_trees(
            GrammarParser.parse_text("sewi o pana e pona tawa mi."),
            Phrase(
                "TEXT",
                children=[
                    Phrase(
                        "SENTENCE",
                        children=[
                            Phrase(
                                "NOUN_PHRASE",
                                children=[
                                    Phrase(Word("sewi", PartOfSpeech.NOUN)),
                                ],
                            ),
                            Phrase(Word("o", PartOfSpeech.PARTICLE)),
                            Phrase(
                                "VERB_PHRASE",
                                children=[
                                    Phrase(Word("pana", PartOfSpeech.VERB)),
                                    Phrase(Word("e", PartOfSpeech.PARTICLE)),
                                    Phrase(
                                        "NOUN_PHRASE",
                                        children=[
                                            Phrase(Word("pona", PartOfSpeech.NOUN)),
                                        ],
                                    ),
                                    Phrase(
                                        "PREPOSITION_PHRASE",
                                        children=[
                                            Phrase(
                                                Word("tawa", PartOfSpeech.PREPOSITION),
                                            ),
                                            Phrase(
                                                "NOUN_PHRASE",
                                                children=[
                                                    Phrase(
                                                        Word("mi", PartOfSpeech.NOUN),
                                                    ),
                                                ],
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
            GrammarParser.parse_text("o kute e mama sina."),
            Phrase(
                "TEXT",
                children=[
                    Phrase(
                        "SENTENCE",
                        children=[
                            Phrase(Word("o", PartOfSpeech.PARTICLE)),
                            Phrase(
                                "VERB_PHRASE",
                                children=[
                                    Phrase(Word("kute", PartOfSpeech.VERB)),
                                    Phrase(Word("e", PartOfSpeech.PARTICLE)),
                                    Phrase(
                                        "NOUN_PHRASE",
                                        children=[
                                            Phrase(Word("mama", PartOfSpeech.NOUN)),
                                            Phrase(
                                                "ADJECTIVE_PHRASE",
                                                children=[
                                                    Phrase(
                                                        Word(
                                                            "sina",
                                                            PartOfSpeech.ADJECTIVE,
                                                        ),
                                                    ),
                                                ],
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
            GrammarParser.parse_text("sina suli a!"),
            Phrase(
                "TEXT",
                children=[
                    Phrase(
                        "SENTENCE",
                        children=[
                            Phrase(
                                "NOUN_PHRASE",
                                children=[
                                    Phrase(Word("sina", PartOfSpeech.NOUN)),
                                ],
                            ),
                            Phrase(
                                "VERB_PHRASE",
                                children=[
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
                            Phrase(Word("a", PartOfSpeech.PARTICLE)),
                            Phrase(Punctuation("!")),
                        ],
                    ),
                ],
            ),
        )
        self._compare_trees(
            GrammarParser.parse_text("pona!"),
            Phrase(
                "TEXT",
                children=[
                    Phrase(
                        "SENTENCE",
                        children=[
                            Phrase(
                                "ADJECTIVE_PHRASE",
                                children=[
                                    Phrase(Word("pona", PartOfSpeech.ADJECTIVE)),
                                ],
                            ),
                            Phrase(Punctuation("!")),
                        ],
                    ),
                ],
            ),
        )
        self._compare_trees(
            GrammarParser.parse_text("mi o moku e ijo pona."),
            Phrase(
                "TEXT",
                children=[
                    Phrase(
                        "SENTENCE",
                        children=[
                            Phrase(
                                "NOUN_PHRASE",
                                children=[
                                    Phrase(Word("mi", PartOfSpeech.NOUN)),
                                ],
                            ),
                            Phrase(Word("o", PartOfSpeech.PARTICLE)),
                            Phrase(
                                "VERB_PHRASE",
                                children=[
                                    Phrase(Word("moku", PartOfSpeech.VERB)),
                                    Phrase(Word("e", PartOfSpeech.PARTICLE)),
                                    Phrase(
                                        "NOUN_PHRASE",
                                        children=[
                                            Phrase(Word("ijo", PartOfSpeech.NOUN)),
                                            Phrase(
                                                "ADJECTIVE_PHRASE",
                                                children=[
                                                    Phrase(
                                                        Word(
                                                            "pona",
                                                            PartOfSpeech.ADJECTIVE,
                                                        ),
                                                    ),
                                                ],
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

    def test_lesson_11(self):
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
            GrammarParser.parse_text("mije sona"),
            Phrase(
                "TEXT",
                children=[
                    Phrase(
                        "SENTENCE",
                        children=[
                            Phrase(
                                "NOUN_PHRASE",
                                children=[
                                    Phrase(Word("mije", PartOfSpeech.NOUN)),
                                    Phrase(
                                        "ADJECTIVE_PHRASE",
                                        children=[
                                            Phrase(
                                                Word("sona", PartOfSpeech.ADJECTIVE),
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
            GrammarParser.parse_text("jan pona mute"),
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
                                            Phrase(
                                                Word("mute", PartOfSpeech.ADJECTIVE),
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
            GrammarParser.parse_text("mije sona lili"),
            Phrase(
                "TEXT",
                children=[
                    Phrase(
                        "SENTENCE",
                        children=[
                            Phrase(
                                "NOUN_PHRASE",
                                children=[
                                    Phrase(Word("mije", PartOfSpeech.NOUN)),
                                    Phrase(
                                        "ADJECTIVE_PHRASE",
                                        children=[
                                            Phrase(
                                                Word("sona", PartOfSpeech.ADJECTIVE),
                                            ),
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
            GrammarParser.parse_text("jan pi pona mute"),
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
                                    Phrase(Word("pi", PartOfSpeech.PARTICLE)),
                                    Phrase(Word("pona", PartOfSpeech.NOUN)),
                                    Phrase(
                                        "ADJECTIVE_PHRASE",
                                        children=[
                                            Phrase(
                                                Word("mute", PartOfSpeech.ADJECTIVE),
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
            GrammarParser.parse_text("mije pi sona lili"),
            Phrase(
                "TEXT",
                children=[
                    Phrase(
                        "SENTENCE",
                        children=[
                            Phrase(
                                "NOUN_PHRASE",
                                children=[
                                    Phrase(Word("mije", PartOfSpeech.NOUN)),
                                    Phrase(Word("pi", PartOfSpeech.PARTICLE)),
                                    Phrase(Word("sona", PartOfSpeech.NOUN)),
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
            GrammarParser.parse_text("tenpo suno ni li pona mute tawa mi."),
            Phrase(
                "TEXT",
                children=[
                    Phrase(
                        "SENTENCE",
                        children=[
                            Phrase(
                                "NOUN_PHRASE",
                                children=[
                                    Phrase(Word("tenpo", PartOfSpeech.NOUN)),
                                    Phrase(
                                        "ADJECTIVE_PHRASE",
                                        children=[
                                            Phrase(
                                                Word("suno", PartOfSpeech.ADJECTIVE),
                                            ),
                                            Phrase(Word("ni", PartOfSpeech.ADJECTIVE)),
                                        ],
                                    ),
                                ],
                            ),
                            Phrase(Word("li", PartOfSpeech.PARTICLE)),
                            Phrase(
                                "VERB_PHRASE",
                                children=[
                                    Phrase(Word("pona", PartOfSpeech.VERB)),
                                    Phrase(
                                        "ADJECTIVE_PHRASE",
                                        children=[
                                            Phrase(
                                                Word("mute", PartOfSpeech.ADJECTIVE),
                                            ),
                                        ],
                                    ),
                                    Phrase(
                                        "PREPOSITION_PHRASE",
                                        children=[
                                            Phrase(
                                                Word("tawa", PartOfSpeech.PREPOSITION),
                                            ),
                                            Phrase(
                                                "NOUN_PHRASE",
                                                children=[
                                                    Phrase(
                                                        Word("mi", PartOfSpeech.NOUN),
                                                    ),
                                                ],
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
            GrammarParser.parse_text("meli lili pi sijelo pona li telo e kasi."),
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
                                    Phrase(Word("pi", PartOfSpeech.PARTICLE)),
                                    Phrase(Word("sijelo", PartOfSpeech.NOUN)),
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
                            Phrase(Word("li", PartOfSpeech.PARTICLE)),
                            Phrase(
                                "VERB_PHRASE",
                                children=[
                                    Phrase(Word("telo", PartOfSpeech.VERB)),
                                    Phrase(Word("e", PartOfSpeech.PARTICLE)),
                                    Phrase(
                                        "NOUN_PHRASE",
                                        children=[
                                            Phrase(Word("kasi", PartOfSpeech.NOUN)),
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
            GrammarParser.parse_text("mije pi pilin pona li pali e ilo tenpo suno."),
            Phrase(
                "TEXT",
                children=[
                    Phrase(
                        "SENTENCE",
                        children=[
                            Phrase(
                                "NOUN_PHRASE",
                                children=[
                                    Phrase(Word("mije", PartOfSpeech.NOUN)),
                                    Phrase(Word("pi", PartOfSpeech.PARTICLE)),
                                    Phrase(Word("pilin", PartOfSpeech.NOUN)),
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
                            Phrase(Word("li", PartOfSpeech.PARTICLE)),
                            Phrase(
                                "VERB_PHRASE",
                                children=[
                                    Phrase(Word("pali", PartOfSpeech.VERB)),
                                    Phrase(Word("e", PartOfSpeech.PARTICLE)),
                                    Phrase(
                                        "NOUN_PHRASE",
                                        children=[
                                            Phrase(Word("ilo", PartOfSpeech.NOUN)),
                                            Phrase(
                                                "ADJECTIVE_PHRASE",
                                                children=[
                                                    Phrase(
                                                        Word(
                                                            "tenpo",
                                                            PartOfSpeech.ADJECTIVE,
                                                        ),
                                                    ),
                                                    Phrase(
                                                        Word(
                                                            "suno",
                                                            PartOfSpeech.ADJECTIVE,
                                                        ),
                                                    ),
                                                ],
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
            GrammarParser.parse_text("mama mama mi li lili."),
            Phrase(
                "TEXT",
                children=[
                    Phrase(
                        "SENTENCE",
                        children=[
                            Phrase(
                                "NOUN_PHRASE",
                                children=[
                                    Phrase(Word("mama", PartOfSpeech.NOUN)),
                                    Phrase(
                                        "ADJECTIVE_PHRASE",
                                        children=[
                                            Phrase(
                                                Word("mama", PartOfSpeech.ADJECTIVE),
                                            ),
                                            Phrase(Word("mi", PartOfSpeech.ADJECTIVE)),
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
                                            Phrase(
                                                Word("lili", PartOfSpeech.ADJECTIVE),
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
            GrammarParser.parse_text("sina mute li jo ala jo e tomo tawa?"),
            Phrase(
                "TEXT",
                children=[
                    Phrase(
                        "SENTENCE",
                        children=[
                            Phrase(
                                "NOUN_PHRASE",
                                children=[
                                    Phrase(Word("sina", PartOfSpeech.NOUN)),
                                    Phrase(
                                        "ADJECTIVE_PHRASE",
                                        children=[
                                            Phrase(
                                                Word("mute", PartOfSpeech.ADJECTIVE),
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            Phrase(Word("li", PartOfSpeech.PARTICLE)),
                            Phrase(
                                "VERB_PHRASE",
                                children=[
                                    Phrase(Word("jo", PartOfSpeech.VERB)),
                                    Phrase(Word("ala", PartOfSpeech.PARTICLE)),
                                    Phrase(Word("jo", PartOfSpeech.VERB)),
                                    Phrase(Word("e", PartOfSpeech.PARTICLE)),
                                    Phrase(
                                        "NOUN_PHRASE",
                                        children=[
                                            Phrase(Word("tomo", PartOfSpeech.NOUN)),
                                            Phrase(
                                                "ADJECTIVE_PHRASE",
                                                children=[
                                                    Phrase(
                                                        Word(
                                                            "tawa",
                                                            PartOfSpeech.ADJECTIVE,
                                                        ),
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            Phrase(Punctuation("?")),
                        ],
                    ),
                ],
            ),
        )
        self._compare_trees(
            GrammarParser.parse_text("o awen lon tenpo pi suli mute."),
            Phrase(
                "TEXT",
                children=[
                    Phrase(
                        "SENTENCE",
                        children=[
                            Phrase(Word("o", PartOfSpeech.PARTICLE)),
                            Phrase(
                                "VERB_PHRASE",
                                children=[
                                    Phrase(Word("awen", PartOfSpeech.VERB)),
                                    Phrase(
                                        "PREPOSITION_PHRASE",
                                        children=[
                                            Phrase(
                                                Word("lon", PartOfSpeech.PREPOSITION),
                                            ),
                                            Phrase(
                                                "NOUN_PHRASE",
                                                children=[
                                                    Phrase(
                                                        Word(
                                                            "tenpo",
                                                            PartOfSpeech.NOUN,
                                                        ),
                                                    ),
                                                    Phrase(
                                                        Word(
                                                            "pi",
                                                            PartOfSpeech.PARTICLE,
                                                        ),
                                                    ),
                                                    Phrase(
                                                        Word("suli", PartOfSpeech.NOUN),
                                                    ),
                                                    Phrase(
                                                        "ADJECTIVE_PHRASE",
                                                        children=[
                                                            Phrase(
                                                                Word(
                                                                    "mute",
                                                                    PartOfSpeech.ADJECTIVE,
                                                                ),
                                                            ),
                                                        ],
                                                    ),
                                                ],
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
            GrammarParser.parse_text("jan sona pi toki pona li pu lon tenpo mute."),
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
                                                Word("sona", PartOfSpeech.ADJECTIVE),
                                            ),
                                        ],
                                    ),
                                    Phrase(Word("pi", PartOfSpeech.PARTICLE)),
                                    Phrase(Word("toki", PartOfSpeech.NOUN)),
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
                            Phrase(Word("li", PartOfSpeech.PARTICLE)),
                            Phrase(
                                "VERB_PHRASE",
                                children=[
                                    Phrase(Word("pu", PartOfSpeech.VERB)),
                                    Phrase(
                                        "PREPOSITION_PHRASE",
                                        children=[
                                            Phrase(
                                                Word("lon", PartOfSpeech.PREPOSITION),
                                            ),
                                            Phrase(
                                                "NOUN_PHRASE",
                                                children=[
                                                    Phrase(
                                                        Word(
                                                            "tenpo",
                                                            PartOfSpeech.NOUN,
                                                        ),
                                                    ),
                                                    Phrase(
                                                        "ADJECTIVE_PHRASE",
                                                        children=[
                                                            Phrase(
                                                                Word(
                                                                    "mute",
                                                                    PartOfSpeech.ADJECTIVE,
                                                                ),
                                                            ),
                                                        ],
                                                    ),
                                                ],
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

    def test_lesson_12(self):
        self._compare_trees(
            GrammarParser.parse_text("kili ala"),
            Phrase(
                "TEXT",
                children=[
                    Phrase(
                        "SENTENCE",
                        children=[
                            Phrase(
                                "NOUN_PHRASE",
                                children=[
                                    Phrase(Word("kili", PartOfSpeech.NOUN)),
                                    Phrase(
                                        "ADJECTIVE_PHRASE",
                                        children=[
                                            Phrase(Word("ala", PartOfSpeech.ADJECTIVE)),
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
            GrammarParser.parse_text("mije wan"),
            Phrase(
                "TEXT",
                children=[
                    Phrase(
                        "SENTENCE",
                        children=[
                            Phrase(
                                "NOUN_PHRASE",
                                children=[
                                    Phrase(Word("mije", PartOfSpeech.NOUN)),
                                    Phrase(
                                        "ADJECTIVE_PHRASE",
                                        children=[
                                            Phrase(Word("wan", PartOfSpeech.ADJECTIVE)),
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
            GrammarParser.parse_text("tomo tu"),
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
                                            Phrase(Word("tu", PartOfSpeech.ADJECTIVE)),
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
            GrammarParser.parse_text("soweli mute"),
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
                                    Phrase(
                                        "ADJECTIVE_PHRASE",
                                        children=[
                                            Phrase(
                                                Word("mute", PartOfSpeech.ADJECTIVE),
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
            GrammarParser.parse_text("jan ale"),
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
                                            Phrase(Word("ale", PartOfSpeech.ADJECTIVE)),
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
            GrammarParser.parse_text("wan"),
            Phrase(
                "TEXT",
                children=[
                    Phrase(
                        "SENTENCE",
                        children=[
                            Phrase(
                                "NUMBER_PHRASE",
                                children=[
                                    Phrase(Word("wan", PartOfSpeech.NUMBER)),
                                ],
                            ),
                        ],
                    ),
                ],
            ),
        )
        self._compare_trees(
            GrammarParser.parse_text("tu"),
            Phrase(
                "TEXT",
                children=[
                    Phrase(
                        "SENTENCE",
                        children=[
                            Phrase(
                                "NUMBER_PHRASE",
                                children=[
                                    Phrase(Word("tu", PartOfSpeech.NUMBER)),
                                ],
                            ),
                        ],
                    ),
                ],
            ),
        )
        self._compare_trees(
            GrammarParser.parse_text("luka"),
            Phrase(
                "TEXT",
                children=[
                    Phrase(
                        "SENTENCE",
                        children=[
                            Phrase(
                                "NUMBER_PHRASE",
                                children=[
                                    Phrase(Word("luka", PartOfSpeech.NUMBER)),
                                ],
                            ),
                        ],
                    ),
                ],
            ),
        )
        self._compare_trees(
            GrammarParser.parse_text("mute"),
            Phrase(
                "TEXT",
                children=[
                    Phrase(
                        "SENTENCE",
                        children=[
                            Phrase(
                                "NUMBER_PHRASE",
                                children=[
                                    Phrase(Word("mute", PartOfSpeech.NUMBER)),
                                ],
                            ),
                        ],
                    ),
                ],
            ),
        )
        self._compare_trees(
            GrammarParser.parse_text("ale"),
            Phrase(
                "TEXT",
                children=[
                    Phrase(
                        "SENTENCE",
                        children=[
                            Phrase(
                                "NUMBER_PHRASE",
                                children=[
                                    Phrase(Word("ale", PartOfSpeech.NUMBER)),
                                ],
                            ),
                        ],
                    ),
                ],
            ),
        )
        self._compare_trees(
            GrammarParser.parse_text("tu wan"),
            Phrase(
                "TEXT",
                children=[
                    Phrase(
                        "SENTENCE",
                        children=[
                            Phrase(
                                "NUMBER_PHRASE",
                                children=[
                                    Phrase(Word("tu", PartOfSpeech.NUMBER)),
                                    Phrase(Word("wan", PartOfSpeech.NUMBER)),
                                ],
                            ),
                        ],
                    ),
                ],
            ),
        )
        self._compare_trees(
            GrammarParser.parse_text("tu tu"),
            Phrase(
                "TEXT",
                children=[
                    Phrase(
                        "SENTENCE",
                        children=[
                            Phrase(
                                "NUMBER_PHRASE",
                                children=[
                                    Phrase(Word("tu", PartOfSpeech.NUMBER)),
                                    Phrase(Word("tu", PartOfSpeech.NUMBER)),
                                ],
                            ),
                        ],
                    ),
                ],
            ),
        )
        self._compare_trees(
            GrammarParser.parse_text("luka wan"),
            Phrase(
                "TEXT",
                children=[
                    Phrase(
                        "SENTENCE",
                        children=[
                            Phrase(
                                "NUMBER_PHRASE",
                                children=[
                                    Phrase(Word("luka", PartOfSpeech.NUMBER)),
                                    Phrase(Word("wan", PartOfSpeech.NUMBER)),
                                ],
                            ),
                        ],
                    ),
                ],
            ),
        )
        self._compare_trees(
            GrammarParser.parse_text("luka tu"),
            Phrase(
                "TEXT",
                children=[
                    Phrase(
                        "SENTENCE",
                        children=[
                            Phrase(
                                "NUMBER_PHRASE",
                                children=[
                                    Phrase(Word("luka", PartOfSpeech.NUMBER)),
                                    Phrase(Word("tu", PartOfSpeech.NUMBER)),
                                ],
                            ),
                        ],
                    ),
                ],
            ),
        )
        self._compare_trees(
            GrammarParser.parse_text("luka tu wan"),
            Phrase(
                "TEXT",
                children=[
                    Phrase(
                        "SENTENCE",
                        children=[
                            Phrase(
                                "NUMBER_PHRASE",
                                children=[
                                    Phrase(Word("luka", PartOfSpeech.NUMBER)),
                                    Phrase(Word("tu", PartOfSpeech.NUMBER)),
                                    Phrase(Word("wan", PartOfSpeech.NUMBER)),
                                ],
                            ),
                        ],
                    ),
                ],
            ),
        )
        self._compare_trees(
            GrammarParser.parse_text("luka tu tu"),
            Phrase(
                "TEXT",
                children=[
                    Phrase(
                        "SENTENCE",
                        children=[
                            Phrase(
                                "NUMBER_PHRASE",
                                children=[
                                    Phrase(Word("luka", PartOfSpeech.NUMBER)),
                                    Phrase(Word("tu", PartOfSpeech.NUMBER)),
                                    Phrase(Word("tu", PartOfSpeech.NUMBER)),
                                ],
                            ),
                        ],
                    ),
                ],
            ),
        )
        self._compare_trees(
            GrammarParser.parse_text("luka luka"),
            Phrase(
                "TEXT",
                children=[
                    Phrase(
                        "SENTENCE",
                        children=[
                            Phrase(
                                "NUMBER_PHRASE",
                                children=[
                                    Phrase(Word("luka", PartOfSpeech.NUMBER)),
                                    Phrase(Word("luka", PartOfSpeech.NUMBER)),
                                ],
                            ),
                        ],
                    ),
                ],
            ),
        )
        self._compare_trees(
            GrammarParser.parse_text("luka luka tu wan"),
            Phrase(
                "TEXT",
                children=[
                    Phrase(
                        "SENTENCE",
                        children=[
                            Phrase(
                                "NUMBER_PHRASE",
                                children=[
                                    Phrase(Word("luka", PartOfSpeech.NUMBER)),
                                    Phrase(Word("luka", PartOfSpeech.NUMBER)),
                                    Phrase(Word("tu", PartOfSpeech.NUMBER)),
                                    Phrase(Word("wan", PartOfSpeech.NUMBER)),
                                ],
                            ),
                        ],
                    ),
                ],
            ),
        )
        self._compare_trees(
            GrammarParser.parse_text("mute mute mute luka luka luka tu wan"),
            Phrase(
                "TEXT",
                children=[
                    Phrase(
                        "SENTENCE",
                        children=[
                            Phrase(
                                "NUMBER_PHRASE",
                                children=[
                                    Phrase(Word("mute", PartOfSpeech.NUMBER)),
                                    Phrase(Word("mute", PartOfSpeech.NUMBER)),
                                    Phrase(Word("mute", PartOfSpeech.NUMBER)),
                                    Phrase(Word("luka", PartOfSpeech.NUMBER)),
                                    Phrase(Word("luka", PartOfSpeech.NUMBER)),
                                    Phrase(Word("luka", PartOfSpeech.NUMBER)),
                                    Phrase(Word("tu", PartOfSpeech.NUMBER)),
                                    Phrase(Word("wan", PartOfSpeech.NUMBER)),
                                ],
                            ),
                        ],
                    ),
                ],
            ),
        )
        self._compare_trees(
            GrammarParser.parse_text("ale tu"),
            Phrase(
                "TEXT",
                children=[
                    Phrase(
                        "SENTENCE",
                        children=[
                            Phrase(
                                "NUMBER_PHRASE",
                                children=[
                                    Phrase(Word("ale", PartOfSpeech.NUMBER)),
                                    Phrase(Word("tu", PartOfSpeech.NUMBER)),
                                ],
                            ),
                        ],
                    ),
                ],
            ),
        )
        self._compare_trees(
            GrammarParser.parse_text("toki nanpa wan"),
            Phrase(
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
                                            Phrase(
                                                "NUMBER_PHRASE",
                                                children=[
                                                    Phrase(
                                                        Word(
                                                            "nanpa",
                                                            PartOfSpeech.ADJECTIVE,
                                                        ),
                                                    ),
                                                    Phrase(
                                                        Word(
                                                            "wan",
                                                            PartOfSpeech.NUMBER,
                                                        ),
                                                    ),
                                                ],
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
            GrammarParser.parse_text("tomo nanpa mute tu wan"),
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
                                                "NUMBER_PHRASE",
                                                children=[
                                                    Phrase(
                                                        Word(
                                                            "nanpa",
                                                            PartOfSpeech.ADJECTIVE,
                                                        ),
                                                    ),
                                                    Phrase(
                                                        Word(
                                                            "mute",
                                                            PartOfSpeech.NUMBER,
                                                        ),
                                                    ),
                                                    Phrase(
                                                        Word("tu", PartOfSpeech.NUMBER),
                                                    ),
                                                    Phrase(
                                                        Word(
                                                            "wan",
                                                            PartOfSpeech.NUMBER,
                                                        ),
                                                    ),
                                                ],
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

    def test_lesson_13(self):
        self._compare_trees(
            GrammarParser.parse_text("jan li wile pali..."),
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
                                    Phrase(Word("wile", PartOfSpeech.PREVERB)),
                                    Phrase(Word("pali", PartOfSpeech.VERB)),
                                ],
                            ),
                            Phrase(Punctuation("...")),
                        ],
                    ),
                ],
            ),
        )
        self._compare_trees(
            GrammarParser.parse_text("kama"),
            Phrase(
                "TEXT",
                children=[
                    Phrase(
                        "SENTENCE",
                        children=[
                            Phrase(
                                "ADJECTIVE_PHRASE",
                                children=[
                                    Phrase(Word("kama", PartOfSpeech.ADJECTIVE)),
                                ],
                            ),
                        ],
                    ),
                ],
            ),
        )
        self._compare_trees(
            GrammarParser.parse_text("lukin"),
            Phrase(
                "TEXT",
                children=[
                    Phrase(
                        "SENTENCE",
                        children=[
                            Phrase(
                                "ADJECTIVE_PHRASE",
                                children=[
                                    Phrase(Word("lukin", PartOfSpeech.ADJECTIVE)),
                                ],
                            ),
                        ],
                    ),
                ],
            ),
        )
        self._compare_trees(
            GrammarParser.parse_text("ma tomo li kama suli."),
            Phrase(
                "TEXT",
                children=[
                    Phrase(
                        "SENTENCE",
                        children=[
                            Phrase(
                                "NOUN_PHRASE",
                                children=[
                                    Phrase(Word("ma", PartOfSpeech.NOUN)),
                                    Phrase(
                                        "ADJECTIVE_PHRASE",
                                        children=[
                                            Phrase(
                                                Word("tomo", PartOfSpeech.ADJECTIVE),
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            Phrase(Word("li", PartOfSpeech.PARTICLE)),
                            Phrase(
                                "VERB_PHRASE",
                                children=[
                                    Phrase(Word("kama", PartOfSpeech.PREVERB)),
                                    Phrase(Word("suli", PartOfSpeech.VERB)),
                                ],
                            ),
                            Phrase(Punctuation(".")),
                        ],
                    ),
                ],
            ),
        )
        self._compare_trees(
            GrammarParser.parse_text("mi kama sona e toki pona."),
            Phrase(
                "TEXT",
                children=[
                    Phrase(
                        "SENTENCE",
                        children=[
                            Phrase(
                                "NOUN_PHRASE",
                                children=[
                                    Phrase(Word("mi", PartOfSpeech.NOUN)),
                                ],
                            ),
                            Phrase(
                                "VERB_PHRASE",
                                children=[
                                    Phrase(Word("kama", PartOfSpeech.PREVERB)),
                                    Phrase(Word("sona", PartOfSpeech.VERB)),
                                    Phrase(Word("e", PartOfSpeech.PARTICLE)),
                                    Phrase(
                                        "NOUN_PHRASE",
                                        children=[
                                            Phrase(Word("toki", PartOfSpeech.NOUN)),
                                            Phrase(
                                                "ADJECTIVE_PHRASE",
                                                children=[
                                                    Phrase(
                                                        Word(
                                                            "pona",
                                                            PartOfSpeech.ADJECTIVE,
                                                        ),
                                                    ),
                                                ],
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
            GrammarParser.parse_text("mije wawa li lukin jo e meli pona."),
            Phrase(
                "TEXT",
                children=[
                    Phrase(
                        "SENTENCE",
                        children=[
                            Phrase(
                                "NOUN_PHRASE",
                                children=[
                                    Phrase(Word("mije", PartOfSpeech.NOUN)),
                                    Phrase(
                                        "ADJECTIVE_PHRASE",
                                        children=[
                                            Phrase(
                                                Word("wawa", PartOfSpeech.ADJECTIVE),
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            Phrase(Word("li", PartOfSpeech.PARTICLE)),
                            Phrase(
                                "VERB_PHRASE",
                                children=[
                                    Phrase(Word("lukin", PartOfSpeech.PREVERB)),
                                    Phrase(Word("jo", PartOfSpeech.VERB)),
                                    Phrase(Word("e", PartOfSpeech.PARTICLE)),
                                    Phrase(
                                        "NOUN_PHRASE",
                                        children=[
                                            Phrase(Word("meli", PartOfSpeech.NOUN)),
                                            Phrase(
                                                "ADJECTIVE_PHRASE",
                                                children=[
                                                    Phrase(
                                                        Word(
                                                            "pona",
                                                            PartOfSpeech.ADJECTIVE,
                                                        ),
                                                    ),
                                                ],
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
            GrammarParser.parse_text("mi mute li kama awen lon ma tomo Towano."),
            Phrase(
                "TEXT",
                children=[
                    Phrase(
                        "SENTENCE",
                        children=[
                            Phrase(
                                "NOUN_PHRASE",
                                children=[
                                    Phrase(Word("mi", PartOfSpeech.NOUN)),
                                    Phrase(
                                        "ADJECTIVE_PHRASE",
                                        children=[
                                            Phrase(
                                                Word("mute", PartOfSpeech.ADJECTIVE),
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            Phrase(Word("li", PartOfSpeech.PARTICLE)),
                            Phrase(
                                "VERB_PHRASE",
                                children=[
                                    Phrase(Word("kama", PartOfSpeech.PREVERB)),
                                    Phrase(Word("awen", PartOfSpeech.VERB)),
                                    Phrase(
                                        "PREPOSITION_PHRASE",
                                        children=[
                                            Phrase(
                                                Word("lon", PartOfSpeech.PREPOSITION),
                                            ),
                                            Phrase(
                                                "NOUN_PHRASE",
                                                children=[
                                                    Phrase(
                                                        Word("ma", PartOfSpeech.NOUN),
                                                    ),
                                                    Phrase(
                                                        "ADJECTIVE_PHRASE",
                                                        children=[
                                                            Phrase(
                                                                Word(
                                                                    "tomo",
                                                                    PartOfSpeech.ADJECTIVE,
                                                                ),
                                                            ),
                                                            Phrase(
                                                                Word(
                                                                    "Towano",
                                                                    PartOfSpeech.ADJECTIVE,
                                                                ),
                                                            ),
                                                        ],
                                                    ),
                                                ],
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
            GrammarParser.parse_text("jan lili mi o, sina wile moku e kala anu seme?"),
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
                                                Word("lili", PartOfSpeech.ADJECTIVE),
                                            ),
                                            Phrase(Word("mi", PartOfSpeech.ADJECTIVE)),
                                        ],
                                    ),
                                ],
                            ),
                            Phrase(Word("o", PartOfSpeech.PARTICLE)),
                            Phrase(Punctuation(",")),
                            Phrase(
                                "NOUN_PHRASE",
                                children=[
                                    Phrase(Word("sina", PartOfSpeech.NOUN)),
                                ],
                            ),
                            Phrase(
                                "VERB_PHRASE",
                                children=[
                                    Phrase(Word("wile", PartOfSpeech.PREVERB)),
                                    Phrase(Word("moku", PartOfSpeech.VERB)),
                                    Phrase(Word("e", PartOfSpeech.PARTICLE)),
                                    Phrase(
                                        "NOUN_PHRASE",
                                        children=[
                                            Phrase(Word("kala", PartOfSpeech.NOUN)),
                                        ],
                                    ),
                                ],
                            ),
                            Phrase(Word("anu", PartOfSpeech.PARTICLE)),
                            Phrase(Word("seme", PartOfSpeech.PARTICLE)),
                            Phrase(Punctuation("?")),
                        ],
                    ),
                ],
            ),
        )
        self._compare_trees(
            GrammarParser.parse_text("jan mute li sona ala tawa lon telo."),
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
                                                Word("mute", PartOfSpeech.ADJECTIVE),
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            Phrase(Word("li", PartOfSpeech.PARTICLE)),
                            Phrase(
                                "VERB_PHRASE",
                                children=[
                                    Phrase(Word("sona", PartOfSpeech.PREVERB)),
                                    Phrase(
                                        "ADJECTIVE_PHRASE",
                                        children=[
                                            Phrase(Word("ala", PartOfSpeech.ADJECTIVE)),
                                        ],
                                    ),
                                    Phrase(Word("tawa", PartOfSpeech.VERB)),
                                    Phrase(
                                        "PREPOSITION_PHRASE",
                                        children=[
                                            Phrase(
                                                Word("lon", PartOfSpeech.PREPOSITION),
                                            ),
                                            Phrase(
                                                "NOUN_PHRASE",
                                                children=[
                                                    Phrase(
                                                        Word("telo", PartOfSpeech.NOUN),
                                                    ),
                                                ],
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
            GrammarParser.parse_text("sina ken ala ken kama?"),
            Phrase(
                "TEXT",
                children=[
                    Phrase(
                        "SENTENCE",
                        children=[
                            Phrase(
                                "NOUN_PHRASE",
                                children=[
                                    Phrase(Word("sina", PartOfSpeech.NOUN)),
                                ],
                            ),
                            Phrase(
                                "VERB_PHRASE",
                                children=[
                                    Phrase(Word("ken", PartOfSpeech.PREVERB)),
                                    Phrase(Word("ala", PartOfSpeech.PARTICLE)),
                                    Phrase(Word("ken", PartOfSpeech.PREVERB)),
                                    Phrase(Word("kama", PartOfSpeech.VERB)),
                                ],
                            ),
                            Phrase(Punctuation("?")),
                        ],
                    ),
                ],
            ),
        )
