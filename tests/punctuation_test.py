import unittest

from project_toki.punctuation import Punctuation


class TestPunctuation(unittest.TestCase):
    def test_from_str(self):
        self.assertEqual(
            Punctuation.from_str(
                text='. "',
            ),
            Punctuation(
                text='. "',
            ),
        )
        self.assertRaises(
            TypeError,
            Punctuation.from_str,
            text=3,
        )
