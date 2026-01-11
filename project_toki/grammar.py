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
            _subsentence: _subsentence_declarative_mi_sina | _subsentence_declarative_other | _subsentence_quasi

            // Define subsentences
            _subsentence_declarative_mi_sina: noun_phrase__mi_sina WS verb_phrase
            _subsentence_declarative_other: noun_phrase__other WS PARTICLE__LI WS verb_phrase
            _subsentence_quasi: number_phrase | adjective_phrase__single | noun_phrase__other

            // Noun phrases
            noun_phrase__mi_sina: NOUN__MI_SINA
            noun_phrase__other: NOUN (WS adjective_phrase)?

            // Adjective phrases
            adjective_phrase: ADJECTIVE (WS ADJECTIVE)*
            adjective_phrase__single: ADJECTIVE

            // Number phrases
            number_phrase: NUMBER (WS NUMBER)*

            // Verb phrases
            verb_phrase: _subsentence_quasi | _verb_phrase
            _verb_phrase: VERB (WS adjective_phrase)? (WS PARTICLE__E WS noun_phrase__other)?

            // Punctuation
            WS: (" ")+
            PUNCT_END: ("!" | "..." | "." | "?")
            PUNCT_OTHER: ("," | "-" | ":" | ";")

            // Compound terminals
            ADJECTIVE: {Grammar._create_word_list(["ADJECTIVE", "NOUN", "NOUN__MI_SINA", "VERB", "VERB__WITH_OBJECT", "VERB__WITHOUT_OBJECT", "OTHER"])} | UNKNOWN
            NOUN: {Grammar._create_word_list(["NOUN", "NOUN__MI_SINA", "ADJECTIVE", "VERB", "VERB__WITH_OBJECT", "VERB__WITHOUT_OBJECT", "OTHER"])} | UNKNOWN
            VERB: {Grammar._create_word_list(["VERB", "VERB__WITH_OBJECT", "VERB__WITHOUT_OBJECT", "ADJECTIVE", "NOUN", "NOUN__MI_SINA", "OTHER"])} | UNKNOWN

            // Simple terminals
            INTERJECTION: {Grammar._create_word_list(["INTERJECTION"])}
            NOUN__MI_SINA: {Grammar._create_word_list(["NOUN__MI_SINA"])}
            NUMBER: {Grammar._create_word_list(["NUMBER"])}
            PARTICLE: {Grammar._create_word_list(["PARTICLE"])}
            PARTICLE__LI: {Grammar._create_word_list(["PARTICLE__LI"])}
            PARTICLE__E: {Grammar._create_word_list(["PARTICLE__E"])}
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
