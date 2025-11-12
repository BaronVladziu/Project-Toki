class Punctuation:
    """
    This class represents a sequence of punctuation symbols.
    """

    def __init__(self, text: str):
        Punctuation._check_input(text)
        self.text: str = text

    @staticmethod
    def _check_input(text: str) -> None:
        if not isinstance(text, str):
            raise TypeError(
                f'Expected punctuation of type "str" but received "{text}" of type "{type(text)}"!',
            )

    @staticmethod
    def from_str(text: str) -> Punctuation:
        return Punctuation(text)

    def __len__(self) -> int:
        return len(self.text)

    def __str__(self) -> str:
        return self.text

    def __repr__(self) -> str:
        return f'Punctuation("{self.text}")'

    def __eq__(self, other) -> bool:
        return type(other) == type(self) and self.text == other.text

    def __hash__(self) -> int:
        return hash(repr(self))
