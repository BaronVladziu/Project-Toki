import unittest

from project_toki.text import Text
from project_toki.word import Word
from project_toki.punctuation import Punctuation


class TestText(unittest.TestCase):
    def test_init(self):
        _ = Text(
            sequences=[],
        )
        _ = Text(
            sequences=[Word("pona")],
        )
        _ = Text(
            sequences=[Punctuation(".")],
        )
        self.assertRaises(
            TypeError,
            Text,
            sequences=[1],
        )
        _ = Text(
            sequences=[
                Word("pilin"),
                Word("pona"),
                Word("la"),
                Word("mi"),
                Word("musi"),
            ],
        )
        _ = Text(
            sequences=[
                Word("pilin"),
                Punctuation(" "),
                Word("pona"),
                Punctuation(", "),
                Word("la"),
                Punctuation(" "),
                Word("mi"),
                Punctuation(" "),
                Word("musi"),
                Punctuation("."),
            ],
        )

    def test_from_str(self):
        self.assertEqual(
            Text.from_str(text=""),
            Text(
                sequences=[],
            ),
        )
        self.assertEqual(
            Text.from_str(text="pona"),
            Text(
                sequences=[
                    Word("pona"),
                ],
            ),
        )
        self.assertEqual(
            Text.from_str(text="."),
            Text(
                sequences=[
                    Punctuation("."),
                ],
            ),
        )
        self.assertEqual(
            Text.from_str(text="pilin pona, la mi musi."),
            Text(
                sequences=[
                    Word("pilin"),
                    Punctuation(" "),
                    Word("pona"),
                    Punctuation(", "),
                    Word("la"),
                    Punctuation(" "),
                    Word("mi"),
                    Punctuation(" "),
                    Word("musi"),
                    Punctuation("."),
                ],
            ),
        )
