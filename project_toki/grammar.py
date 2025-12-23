from project_toki.dictionary import Dictionary


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
            _subsentence: _subsentence_declarative | _subsentence_quasi

            // Define subsentences
            _subsentence_declarative: noun_phrase WS PARTICLE__LI WS verb_phrase
            _subsentence_quasi: adjective_phrase__single | noun_phrase | adjective_phrase

            // Noun phrases
            noun_phrase: NOUN (WS adjective_phrase)?

            // Adjective phrases
            adjective_phrase: ADJECTIVE (WS ADJECTIVE)*
            adjective_phrase__single: ADJECTIVE

            // Verb phrases
            verb_phrase: adjective_phrase

            // Punctuation
            WS: (" ")+
            PUNCT_END: ("!" | "..." | "." | "?")
            PUNCT_OTHER: ("," | "-" | ":" | ";")

            // Compound terminals
            ADJECTIVE: {Grammar._create_word_list(["ADJECTIVE", "NOUN", "VERB", "VERB__WITH_OBJECT", "VERB__WITHOUT_OBJECT", "OTHER"])} | UNKNOWN
            NOUN: {Grammar._create_word_list(["NOUN", "ADJECTIVE", "VERB", "VERB__WITH_OBJECT", "VERB__WITHOUT_OBJECT", "OTHER"])} | UNKNOWN

            // Simple terminals
            INTERJECTION: {Grammar._create_word_list(["INTERJECTION"])}
            NUMBER: {Grammar._create_word_list(["NUMBER"])}
            PARTICLE: {Grammar._create_word_list(["PARTICLE"])}
            PARTICLE__LI: {Grammar._create_word_list(["PARTICLE__LI"])}
            PREVERB: {Grammar._create_word_list(["PREVERB"])}
            PREPOSITION: {Grammar._create_word_list(["PREPOSITION"])}

            // Non-dictionary terminals
            UNKNOWN: /(?!{'|'.join(Dictionary.get_all_words())})([a-z]+)/
        """

    @staticmethod
    def _create_word_list(parts_of_speech: list[str]) -> str:
        return '"' + '" | "'.join(Grammar._extract_words(parts_of_speech)) + '"'

    @staticmethod
    def _extract_words(parts_of_speech: list[str]) -> list[str]:
        words: list[str] = []
        word_set: set[str] = set()
        for pos in parts_of_speech:
            pos_words: list[str] = sorted(Dictionary.get_words_for_part_of_speech(pos))
            if len(pos_words) < 1:
                raise ValueError(
                    f'There are no items in a dictionary for part of speech "{pos}"!',
                )
            for word in pos_words:
                if word not in word_set:
                    words.append(word)
                    word_set.add(word)
        return words
