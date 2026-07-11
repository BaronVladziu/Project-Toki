import pytest

from project_toki.part_of_speech import PartOfSpeech
from project_toki.punctuation import Punctuation
from project_toki.text import Text
from project_toki.word import Word


class TestText:
    def test_init(self):
        _ = Text(
            sequences=[],
        )
        _ = Text(
            sequences=[Word("pona", PartOfSpeech.ADJECTIVE)],
        )
        _ = Text(
            sequences=[Punctuation(".")],
        )
        with pytest.raises(TypeError):
            Text(
                sequences=[1],
            )
        _ = Text(
            sequences=[
                Word("pilin", PartOfSpeech.NOUN),
                Word("pona", PartOfSpeech.ADJECTIVE),
                Word("la", PartOfSpeech.PARTICLE),
                Word("mi", PartOfSpeech.NOUN),
                Word("musi", PartOfSpeech.VERB),
            ],
        )
        _ = Text(
            sequences=[
                Word("pilin", PartOfSpeech.NOUN),
                Punctuation(" "),
                Word("pona", PartOfSpeech.ADJECTIVE),
                Punctuation(", "),
                Word("la", PartOfSpeech.PARTICLE),
                Punctuation(" "),
                Word("mi", PartOfSpeech.NOUN),
                Punctuation(" "),
                Word("musi", PartOfSpeech.VERB),
                Punctuation("."),
            ],
        )

    def test_from_str(self):
        assert Text.from_str(text="") == Text(
            sequences=[],
        )
        assert Text.from_str(text="pona") == Text(
            sequences=[
                Word("pona", PartOfSpeech.UNKNOWN),
            ],
        )
        assert Text.from_str(text=".") == Text(
            sequences=[
                Punctuation("."),
            ],
        )
        assert Text.from_str(text="pilin pona, la mi musi.") == Text(
            sequences=[
                Word("pilin", PartOfSpeech.UNKNOWN),
                Punctuation(" "),
                Word("pona", PartOfSpeech.UNKNOWN),
                Punctuation(", "),
                Word("la", PartOfSpeech.UNKNOWN),
                Punctuation(" "),
                Word("mi", PartOfSpeech.UNKNOWN),
                Punctuation(" "),
                Word("musi", PartOfSpeech.UNKNOWN),
                Punctuation("."),
            ],
        )
