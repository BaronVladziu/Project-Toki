import enum


class PartOfSpeech(enum.Enum):
    """
    This class represents a part of speech of a word.
    """

    ADJECTIVE = "ADJECTIVE"
    INTERJECTION = "INTERJECTION"
    NOUN = "NOUN"
    NUMBER = "NUMBER"
    PARTICLE = "PARTICLE"
    PREPOSITION = "PREPOSITION"
    PRE_VERB = "PRE_VERB"
    VERB = "VERB"
    OTHER = "OTHER"
    UNKNOWN = "UNKNOWN"
