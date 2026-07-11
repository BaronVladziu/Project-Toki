import pytest

from project_toki.dictionary import Dictionary


class TestDictionary:
    def test_extract_parts_of_speech(self):
        assert Dictionary.extract_parts_of_speech(
            word="x",
        ) == {"UNKNOWN"}
        assert Dictionary.extract_parts_of_speech(
            word="toki",
        ) == {
            "ADJECTIVE",
            "NOUN",
            "VERB",
        }

    def test_extract_definition(self):
        with pytest.raises(ValueError):
            Dictionary.extract_definition(
                word="x",
                part_of_speech="NOUN",
            )
        assert (
            Dictionary.extract_definition(
                word="toki",
                part_of_speech="VERB",
            )
            == "to speak, to talk, to use language, to think"
        )

    def test_get_words_for_part_of_speech(self):
        assert Dictionary.get_words_for_part_of_speech(
            part_of_speech="PREVERB",
        ) == {
            "alasa",
            "awen",
            "kama",
            "ken",
            "lukin",
            "open",
            "pini",
            "sona",
            "wile",
        }
