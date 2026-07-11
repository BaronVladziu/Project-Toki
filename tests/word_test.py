import pytest

from project_toki.part_of_speech import PartOfSpeech
from project_toki.word import Word


class TestWord:
    def test_from_str(self):
        assert Word.from_str(
            text="toki",
            part_of_speech=PartOfSpeech.NOUN,
        ) == Word(
            text="toki",
            part_of_speech=PartOfSpeech.NOUN,
        )
        with pytest.raises(TypeError):
            Word.from_str(
                text=3,
                part_of_speech=PartOfSpeech.NOUN,
            )
        with pytest.raises(ValueError):
            Word.from_str(
                text="",
                part_of_speech=PartOfSpeech.NOUN,
            )
        with pytest.raises(TypeError):
            Word.from_str(
                text="toki",
                part_of_speech=3,
            )
