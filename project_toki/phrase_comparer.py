import unittest

from project_toki.phrase import Phrase


class PhraseComparer(unittest.TestCase):
    """
    This is a support class for comparing phrases.
    """

    def compare_phrases(self, out_phrase: Phrase, ref_phrase: Phrase) -> None:
        self.assertEqual(out_phrase, ref_phrase, msg=out_phrase.get_diff(ref_phrase))
