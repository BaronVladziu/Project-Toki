import unittest

from project_toki.dictionary import Dictionary


class TestDictionary(unittest.TestCase):
    def test_extract_parts_of_speech(self):
        self.assertEqual(
            Dictionary.extract_parts_of_speech(
                word="x",
            ),
            {"UNKNOWN"},
        )
        self.assertEqual(
            Dictionary.extract_parts_of_speech(
                word="toki",
            ),
            {
                "ADJECTIVE",
                "NOUN",
                "VERB",
            },
        )

    def test_extract_definition(self):
        with self.assertRaises(ValueError):
            Dictionary.extract_definition(
                word="x",
                part_of_speech="NOUN",
            )
        self.assertEqual(
            Dictionary.extract_definition(
                word="toki",
                part_of_speech="VERB",
            ),
            "to speak, to talk, to use language, to think",
        )

    def test_get_words_for_part_of_speech(self):
        self.assertEqual(
            Dictionary.get_words_for_part_of_speech(
                part_of_speech="NUMBER",
            ),
            {
                "ala",
                "ale",
                "ali",
                "luka",
                "mute",
                "tu",
                "wan",
            },
        )
