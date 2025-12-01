import unittest

from project_toki.part_of_speech import PartOfSpeech
from project_toki.word import Word


class TestWord(unittest.TestCase):
    def test_from_str(self):
        self.assertEqual(
            Word.from_str(
                text="toki",
                part_of_speech=PartOfSpeech.NOUN,
            ),
            Word(
                text="toki",
                part_of_speech=PartOfSpeech.NOUN,
            ),
        )
        with self.assertRaises(TypeError):
            Word.from_str(
                text=3,
                part_of_speech=PartOfSpeech.NOUN,
            )
        with self.assertRaises(ValueError):
            Word.from_str(
                text="",
                part_of_speech=PartOfSpeech.NOUN,
            )
        with self.assertRaises(TypeError):
            Word.from_str(
                text="toki",
                part_of_speech=3,
            )
