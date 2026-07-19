import enum


class WordStatus(enum.Enum):
    """
    This class represents a status of a word.
    """

    PU = "PU"  # word has been introduced in pu (Toki Pona: Language of Good book)
    KU_SULI = (
        "KU_SULI"  # word has been marked in ku (Toki Pona Dictionary) as "essential"
    )
    KU_LILI = "KU_LILI"  # word has been marked in ku (Toki Pona Dictionary) with a frequency index of 2 or higher
    OTHER = "OTHER"
