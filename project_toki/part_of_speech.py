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
    PREVERB = "PREVERB"
    VERB = "VERB"
    OTHER = "OTHER"
    UNKNOWN = "UNKNOWN"
