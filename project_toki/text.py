from project_toki.word import Word
from project_toki.punctuation import Punctuation


class Text:
    """
    This class represents a sequence of
    words and punctuation in Toki Pona language.
    """

    def __init__(self, sequences: list[Word | Punctuation]):
        Text._check_input(sequences)
        self.sequences: list[Word | Punctuation] = sequences

    @staticmethod
    def _check_input(sequences: list[Word | Punctuation]) -> None:
        # Check for unsupported types
        for sequence in sequences:
            if not isinstance(sequence, Word) and not isinstance(sequence, Punctuation):
                raise TypeError(
                    f'Expected sequences of type "Word" or "Punctuation" but received "{sequence}" of type "{type(sequence)}"!',
                )

    @staticmethod
    def from_str(text: str) -> Text:
        sequences: list[Word | Punctuation] = []
        if len(text) > 0:
            sequences = Text._split_to_sequences(
                text=text,
                is_punctuation=not text[0].isalpha(),
            )
        return Text(sequences)

    @staticmethod
    def _split_to_sequences(
        text: str,
        is_punctuation: bool,
    ) -> list[Word | Punctuation]:
        next_sequence: str = ""
        while len(text) > 0 and text[0].isalpha() != is_punctuation:
            next_sequence += text[0]
            text = text[1:]
        typed_sequence: Word | Punctuation = (
            Punctuation(next_sequence)
            if is_punctuation
            else Word(
                next_sequence,
            )
        )
        if len(text) == 0:
            return [typed_sequence]
        else:
            return [typed_sequence] + Text._split_to_sequences(
                text=text,
                is_punctuation=not is_punctuation,
            )

    def to_sequences(self) -> list[Word | Punctuation]:
        return self.sequences

    def get_words(self) -> list[Word]:
        return [x for x in self.sequences if isinstance(x, Word)]

    def get_punctuation(self) -> list[Punctuation]:
        return [x for x in self.sequences if isinstance(x, Punctuation)]

    def __len__(self) -> int:
        return len(self.sequences)

    def __str__(self) -> str:
        return "|".join(str(x) for x in self.sequences)

    def __repr__(self) -> str:
        return f'Text("{self.sequences}")'

    def __eq__(self, other) -> bool:
        return type(other) == type(self) and self.sequences == other.sequences

    def __hash__(self) -> int:
        return hash(repr(self))
