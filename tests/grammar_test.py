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
