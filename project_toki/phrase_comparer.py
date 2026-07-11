from project_toki.phrase import Phrase


class PhraseComparer:
    """
    This is a support class for comparing phrases.
    """

    def compare_phrases(self, out_phrase: Phrase, ref_phrase: Phrase) -> None:
        assert out_phrase == ref_phrase, out_phrase.get_diff(ref_phrase)
