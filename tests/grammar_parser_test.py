import unittest

from project_toki.grammar_parser import GrammarParser
from project_toki.part_of_speech import PartOfSpeech
from project_toki.phrase import Phrase
from project_toki.punctuation import Punctuation
from project_toki.word import Word


class TestGrammarParser(unittest.TestCase):
    def _compare_trees(self, out_tree: Phrase, ref_tree: Phrase) -> None:
        self.assertEqual(out_tree, ref_tree, msg=f"\n{out_tree}\n!={ref_tree}")

    def test_punctuation(self):
        self._compare_trees(
            GrammarParser.parse_text("wile? wile!"),
            Phrase(
                "TEXT",
                children=[
                    Phrase(
                        "SENTENCE",
                        children=[
                            Phrase(Word("wile", PartOfSpeech.ADJECTIVE)),
                            Phrase(Punctuation("?")),
                            Phrase(Punctuation(" ")),
                        ],
                    ),
                    Phrase(
                        "SENTENCE",
                        children=[
                            Phrase(Word("wile", PartOfSpeech.ADJECTIVE)),
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
                            Phrase(Word("sina", PartOfSpeech.ADJECTIVE)),
                            Phrase(Punctuation("...")),
                            Phrase(Punctuation(" ")),
                        ],
                    ),
                    Phrase(
                        "SENTENCE",
                        children=[
                            Phrase(Word("awen", PartOfSpeech.ADJECTIVE)),
                        ],
                    ),
                ],
            ),
        )
