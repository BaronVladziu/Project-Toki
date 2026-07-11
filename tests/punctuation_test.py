import pytest

from project_toki.punctuation import Punctuation


class TestPunctuation:
    def test_from_str(self):
        assert Punctuation.from_str(
            text='. "',
        ) == Punctuation(
            text='. "',
        )
        with pytest.raises(TypeError):
            Punctuation.from_str(
                text=3,
            )
