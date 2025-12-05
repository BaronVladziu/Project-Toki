import unittest

from project_toki.grammar_parser import GrammarParser
from project_toki.part_of_speech import PartOfSpeech
from project_toki.phrase import Phrase
from project_toki.word import Word


class TestGrammarParser(unittest.TestCase):
    def _compare_trees(self, out_tree: Phrase, ref_tree: Phrase) -> None:
        self.assertEqual(out_tree, ref_tree, msg=f"\n{out_tree}\n!={ref_tree}")

    def test_dummy(self):
        self._compare_trees(
            GrammarParser.parse_text("pona"),
            Phrase(
                "TEXT",
                children=[
                    Phrase(Word("pona", PartOfSpeech.ADJECTIVE)),
                ],
            ),
        )
        self._compare_trees(
            GrammarParser.parse_text("ike"),
            Phrase(
                "TEXT",
                children=[
                    Phrase(Word("ike", PartOfSpeech.ADJECTIVE)),
                ],
            ),
        )
        self._compare_trees(
            GrammarParser.parse_text("pona ike"),
            Phrase(
                "TEXT",
                children=[
                    Phrase(Word("pona", PartOfSpeech.ADJECTIVE)),
                    Phrase(Word("ike", PartOfSpeech.ADJECTIVE)),
                ],
            ),
        )
