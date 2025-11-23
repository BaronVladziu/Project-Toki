from project_toki.part_of_speech import PartOfSpeech


class Word:
    """
    This class represents a single word in Toki Pona language.
    """

    def __init__(self, text: str, part_of_speech: PartOfSpeech):
        Word._check_input(text, part_of_speech)
        self.text: str = text
        self.part_of_speech: PartOfSpeech = part_of_speech

    @staticmethod
    def _check_input(text: str, part_of_speech: PartOfSpeech) -> None:
        if not isinstance(text, str):
            raise TypeError(
                f'Expected word of type "str" but received "{text}" of type "{type(text)}"!',
            )
        if len(text) <= 0:
            raise ValueError(
                f'Word must have positive length but received text "{text}" of length "{len(text)}"!',
            )
        if not isinstance(part_of_speech, PartOfSpeech):
            raise TypeError(
                f'Expected part of speech of type "PartOfSpeech" but received "{part_of_speech}" of type "{type(part_of_speech)}"!',
            )

    @staticmethod
    def from_str(text: str, part_of_speech: PartOfSpeech) -> Word:
        return Word(text, part_of_speech)

    def __len__(self) -> int:
        return len(self.text)

    def __str__(self) -> str:
        return f'{self.part_of_speech.value}: "{self.text}"'

    def __repr__(self) -> str:
        return f'Word({self.part_of_speech}: "{self.text}")'

    def __eq__(self, other) -> bool:
        return (
            type(other) == type(self)
            and self.text == other.text
            and self.part_of_speech == other.part_of_speech
        )

    def __hash__(self) -> int:
        return hash(repr(self))
