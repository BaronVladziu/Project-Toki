class Grammar:
    """
    This class represents the whole grammar of toki pona.
    """

    @staticmethod
    def get_rules() -> str:
        return f"""
            text: WS? (sentence__with_punctuation+ | sentence__with_punctuation* sentence__without_punctuation) WS?
            sentence__with_punctuation: _sentence WS? PUNCT_END WS?
            sentence__without_punctuation: _sentence

            _sentence: ADJECTIVE

            WS: (" ")+
            PUNCT_END: ("..." | "." | "?" | "!")

            ADJECTIVE: UNKNOWN
            UNKNOWN: /[A-Za-z]+/
        """
