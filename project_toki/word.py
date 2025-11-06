from __future__ import annotations


class Word:
    """
    This class represents a single word in Toki Pona language.
    """

    def __init__(self, text: str):
        Word._check_input(text)
        self.text: str = text

    @staticmethod
    def from_str(text: str) -> Word:
        return Word(text)

    @staticmethod
    def _check_input(text: str) -> None:
        if not isinstance(text, str):
            raise TypeError(
                f'Expected word of type "str" but received "{text}" of type "{type(text)}"!',
            )
        if len(text) <= 0:
            raise ValueError(
                f'Word must have positive length but received text "{text}" of length "{len(text)}"!',
            )

    def __len__(self) -> int:
        return len(self.text)

    def __str__(self) -> str:
        return self.text

    def __repr__(self) -> str:
        return f'Word("{self.text}")'

    def __eq__(self, other) -> bool:
        return (
            type(other) == type(self)
            and self.text == other.text
        )

    def __hash__(self) -> int:
        return hash(repr(self))
