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
    PRE_VERB = "PRE_VERB"
    PREPOSITION = "PREPOSITION"
    PRONOUN_SPECIAL = "PRONOUN_SPECIAL"  # pronoun without "li"
    VERB_WITH_OBJECT = "VERB_WITH_OBJECT"
    VERB_WITHOUT_OBJECT = "VERB_WITHOUT_OBJECT"
    OTHER = "OTHER"
    UNKNOWN = "UNKNOWN"
