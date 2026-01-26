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
            _sentence: _subsentence ((_separator_conj | _separator_punct | _separator_whitespace) _subsentence)*
            _separator_conj: WS? PUNCT_OTHER? WS _conjunctions WS? PUNCT_OTHER? WS
            _separator_punct: WS? PUNCT_OTHER WS?
            _separator_whitespace.-1: WS

            // Define subsentences
            _subsentence: _subsentence_imperative | _subsentence_declarative_mi_sina | _subsentence_declarative_other | _subsentence_quasi | _special_words
            _subsentence_declarative_mi_sina: noun_phrase__mi_sina WS verb_phrase__verb_second
            _subsentence_declarative_other: noun_phrase WS PARTICLE__LI WS verb_phrase__verb_second
            _subsentence_imperative: (noun_phrase WS)? PARTICLE__O (WS verb_phrase__verb_first)?
            _subsentence_quasi: PARTICLE__SEME | number_phrase | adjective_phrase__single | preposition_phrase | noun_phrase | _interjections

            // Noun phrases
            noun_phrase__mi_sina: NOUN__MI_SINA
            noun_phrase: (PARTICLE__PI WS)? _noun_phrase (WS PARTICLE__PI WS _noun_phrase)*
            _noun_phrase: (_x_ala_x_noun_phrase | NOUN) (WS adjective_phrase)?

            // Adjective phrases
            adjective_phrase: ADJECTIVE (WS ADJECTIVE)*
            adjective_phrase__single: _x_ala_x_adjective_phrase | ADJECTIVE

            // Number phrases
            number_phrase: NUMBER (WS NUMBER)*

            // Verb phrases
            verb_phrase__verb_first: _verb_phrase | _subsentence_quasi
            verb_phrase__verb_second: _subsentence_quasi | _verb_phrase
            _verb_phrase: (_verb_phrase_e | preposition_phrase | _verb_phrase_single) (WS preposition_phrase)*
            _verb_phrase_e: _verb_phrase_single WS PARTICLE__E WS noun_phrase
            _verb_phrase_single: (_x_ala_x_verb_phrase | VERB) (WS adjective_phrase)?

            // Other phrases
            preposition_phrase.2: PREPOSITION WS noun_phrase
            _conjunctions: PARTICLE__ANU | PARTICLE__EN | PARTICLE__LA
            _interjections: PARTICLE__A | PARTICLE__O | PARTICLE__PAKALA | INTERJECTION
            _special_words: {" | ".join(Grammar._get_special_parts())}

            // x ala x questions
            _x_ala_x_adjective_phrase.9: ADJECTIVE__X_ALA_X
            _x_ala_x_noun_phrase.9: NOUN__X_ALA_X
            _x_ala_x_verb_phrase.9: VERB__X_ALA_X

            // Compound terminals
            ADJECTIVE__X_ALA_X: UNKNOWN__X_ALA_X
            NOUN__X_ALA_X: UNKNOWN__X_ALA_X
            VERB__X_ALA_X: UNKNOWN__X_ALA_X
            ADJECTIVE: PROPER_NAME | UNKNOWN__WORD
            NOUN: UNKNOWN__WORD
            VERB: UNKNOWN__WORD

            // Simple terminals
            INTERJECTION: {Grammar._create_word_list(["INTERJECTION"])}
            NOUN__MI_SINA: {Grammar._create_word_list(["NOUN__MI_SINA"])}
            NUMBER: {Grammar._create_word_list(["NUMBER"])}
            PARTICLE: {Grammar._create_word_list(["PARTICLE"])}
            PARTICLE__A: {Grammar._create_word_list(["PARTICLE__A"])}
            PARTICLE__ALA: {Grammar._create_word_list(["PARTICLE__ALA"])}
            PARTICLE__ANU: {Grammar._create_word_list(["PARTICLE__ANU"])}
            PARTICLE__LA: {Grammar._create_word_list(["PARTICLE__LA"])}
            PARTICLE__LI: {Grammar._create_word_list(["PARTICLE__LI"])}
            PARTICLE__E: {Grammar._create_word_list(["PARTICLE__E"])}
            PARTICLE__EN: {Grammar._create_word_list(["PARTICLE__EN"])}
            PARTICLE__O: {Grammar._create_word_list(["PARTICLE__O"])}
            PARTICLE__PAKALA: {Grammar._create_word_list(["PARTICLE__PAKALA"])}
            PARTICLE__PI: {Grammar._create_word_list(["PARTICLE__PI"])}
            PARTICLE__SEME: {Grammar._create_word_list(["PARTICLE__SEME"])}
            PREVERB: {Grammar._create_word_list(["PREVERB"])}
            PREPOSITION: {Grammar._create_word_list(["PREPOSITION"])}

            // Non-dictionary terminals
            PROPER_NAME: /\\b[A-Z][a-z]*\\b/
            UNKNOWN__WORD: /(?!\\b{'\\b|\\b'.join(Grammar._extract_words(Grammar._get_special_parts()))}\\b)(\\b([A-Za-z0-9]+)\\b)/
            UNKNOWN__X_ALA_X: /((?!\\b{'\\b|\\b'.join(Grammar._extract_words(Grammar._get_special_parts()))}\\b)(\\b([A-Za-z0-9]+)\\b)) ala \\1/

            // Punctuation
            WS: (" ")+
            PUNCT_END: ("!" | "?" | "..." | ".")
            PUNCT_OTHER: /[^A-Za-z .?!]+/
        """

    @staticmethod
    def _get_special_parts() -> list[str]:
        return [
            "PARTICLE__A",
            "PARTICLE__ANU",
            "PARTICLE__E",
            "PARTICLE__EN",
            "PARTICLE__LA",
            "PARTICLE__LI",
            "PARTICLE__O",
            "PARTICLE__PI",
        ]

    @staticmethod
    def _create_word_list(parts_of_speech: list[str]) -> str:
        return '"' + '" | "'.join(Grammar._extract_words(parts_of_speech)) + '"'

    @staticmethod
    def _create_x_ala_x_phrase_definition(
        phrase_part_of_speech: str,
        parts_of_speech: list[str],
    ) -> str:
        output_lines: list[str] = [
            " | ".join(
                [
                    f"{phrase_part_of_speech.upper()}__{word.upper()}_XALAX WS PARTICLE__ALA WS {phrase_part_of_speech.upper()}__{word.upper()}_XALAX"
                    for word in Grammar._extract_words(parts_of_speech)
                ],
            ),
        ]
        output_lines += [
            f'{phrase_part_of_speech.upper()}__{word.upper()}_XALAX: "{word}"'
            for word in Grammar._extract_words(parts_of_speech)
        ]
        return "\n".join(output_lines)

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
