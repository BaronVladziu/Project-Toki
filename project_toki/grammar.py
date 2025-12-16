class Grammar:
    """
    This class represents the whole grammar of toki pona.
    """

    @staticmethod
    def get_rules() -> str:
        return f"""
            // Split to sentences
            text: WS? (sentence__with_punctuation+ | sentence__with_punctuation* sentence__without_punctuation) WS?
            sentence__with_punctuation: _sentence WS? PUNCT_END WS?
            sentence__without_punctuation: _sentence

            // Split to subsentences
            _sentence: _subsentence (WS? PUNCT_OTHER WS? _subsentence)*
            _subsentence: adjective_phrase

            // Adjective phrases
            adjective_phrase: ADJECTIVE (WS ADJECTIVE)*

            // Punctuation
            WS: (" ")+
            PUNCT_END: ("!" | "..." | "." | "?")
            PUNCT_OTHER: ("," | "-" | ":" | ";")

            // Terminals
            ADJECTIVE: UNKNOWN
            UNKNOWN: /[A-Za-z]+/
        """
