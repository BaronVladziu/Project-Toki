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
            _sentence: _subsentence ((_separator_punct | _separator_whitespace) _subsentence)*
            _separator_punct: WS? PUNCT_OTHER WS?
            _separator_whitespace.-3: WS

            // Define subsentences
            _subsentence: (_subsentence_li | _subsentence_o | _subsentence_mi_sina | _subsentence_quasi | _special_words) (WS _anu_seme_phrase)?
            _subsentence_li: (noun_phrase WS)? PARTICLE__LI WS verb_phrase__verb_second
            _subsentence_o: (noun_phrase WS)? PARTICLE__O WS verb_phrase__verb_first
            _subsentence_mi_sina: noun_phrase__mi_sina WS verb_phrase__verb_second
            _subsentence_quasi: number_phrase__cardinal | number_phrase__ordinal_noun | adjective_phrase__single | preposition_phrase | noun_phrase | _interjections

            // Verb phrases
            verb_phrase__verb_first: (_verb_phrase_high_priority | _verb_phrase | _subsentence_quasi)
            verb_phrase__verb_second: (_verb_phrase_high_priority | _subsentence_quasi | _verb_phrase)
            _verb_phrase_high_priority: _verb_phrase_e | _verb_phrase_preposition
            _verb_phrase: (_verb_phrase_e | _verb_phrase_preposition | preposition_phrase | _verb_phrase_single) (WS preposition_phrase)*
            _verb_phrase_e: _verb_phrase_single WS PARTICLE__E WS noun_phrase
            _verb_phrase_preposition: (_preverb_phrase WS)? _verb_phrase_single (WS preposition_phrase)+ (WS PARTICLE__E WS noun_phrase)*
            _verb_phrase_single: (_preverb_phrase WS)? (_x_ala_x_verb_phrase | VERB) (WS adjective_phrase)?

            // Noun phrases
            noun_phrase__mi_sina: NOUN__MI_SINA
            noun_phrase: _noun_phrase_pi (WS _conjunctions WS _noun_phrase_pi)*
            _noun_phrase_pi: (PARTICLE__PI WS)? _noun_phrase (WS PARTICLE__PI WS _noun_phrase)*
            _noun_phrase: (_x_ala_x_noun_phrase | number_phrase__ordinal_noun | NOUN) (WS adjective_phrase)?

            // Adjective phrases
            adjective_phrase__single: _adjective
            adjective_phrase: _adjective (WS _adjective)*
            _adjective: _x_ala_x_number_phrase | _x_ala_x_adjective_phrase | number_phrase__ordinal_adjective | _adjective_ala | ADJECTIVE
            _adjective_ala.2: ADJECTIVE__ALA

            // Number phrases
            number_phrase__cardinal: _number_phrase
            number_phrase__ordinal_adjective.2: ADJECTIVE__NANPA WS _number_phrase
            number_phrase__ordinal_noun.2: NOUN__NANPA WS _number_phrase
            _number_phrase: _x_ala_x_number_phrase | _number_phrase_100 | _number_phrase_20 | _number_phrase_5 | _number_phrase_2 | _number_phrase_1 | _number_phrase_0
            _number_phrase_100.2: NUMBER__100 (WS NUMBER__100)* (WS (_number_phrase_20 | _number_phrase_5 | _number_phrase_2 | _number_phrase_1))?
            _number_phrase_20.2: NUMBER__20 (WS NUMBER__20)* (WS (_number_phrase_5 | _number_phrase_2 | _number_phrase_1))?
            _number_phrase_5.2: NUMBER__5 (WS NUMBER__5)* (WS (_number_phrase_2 | _number_phrase_1))?
            _number_phrase_2.2: NUMBER__2 (WS NUMBER__2)* (WS _number_phrase_1)?
            _number_phrase_1.2: NUMBER__1 (WS NUMBER__1)*
            _number_phrase_0.2: NUMBER__0

            // Other phrases
            preposition_phrase.3: PREPOSITION WS noun_phrase
            _anu_seme_phrase: PARTICLE__ANU WS PARTICLE__SEME
            _conjunctions: PARTICLE__ANU | PARTICLE__EN
            _interjections.-1: PARTICLE__A | PARTICLE__O | PARTICLE__PAKALA | INTERJECTION
            _preverb_phrase.2: _x_ala_x_preverb_phrase | PREVERB (WS adjective_phrase)?
            _special_words: {" | ".join(Grammar._get_special_parts())}

            // x ala x questions
            _x_ala_x_adjective_phrase.9: ADJECTIVE__X_ALA_X
            _x_ala_x_noun_phrase.9: NOUN__X_ALA_X
            _x_ala_x_verb_phrase.9: VERB__X_ALA_X
            _x_ala_x_number_phrase.9: NUMBER__X_ALA_X
            _x_ala_x_preverb_phrase.9: PREVERB__X_ALA_X

            // Compound terminals
            ADJECTIVE__X_ALA_X: UNKNOWN__X_ALA_X
            NOUN__X_ALA_X: UNKNOWN__X_ALA_X
            VERB__X_ALA_X: UNKNOWN__X_ALA_X
            NUMBER__X_ALA_X: /({"|".join(Dictionary.get_words_for_parts_of_speech(["NUMBER__1", "NUMBER__2", "NUMBER__5", "NUMBER__20", "NUMBER__100"]))}) ala \\1/
            PREVERB__X_ALA_X: /({"|".join(Dictionary.get_words_for_parts_of_speech(["PREVERB"]))}) ala \\1/
            ADJECTIVE: PROPER_NAME | UNKNOWN__WORD
            NOUN: UNKNOWN__WORD
            VERB: UNKNOWN__WORD

            // Simple terminals
            ADJECTIVE__ALA: {Grammar._create_word_list(["ADJECTIVE__ALA"])}
            ADJECTIVE__NANPA: {Grammar._create_word_list(["ADJECTIVE__NANPA"])}
            INTERJECTION: {Grammar._create_word_list(["INTERJECTION"])}
            NOUN__MI_SINA: {Grammar._create_word_list(["NOUN__MI_SINA"])}
            NOUN__NANPA: {Grammar._create_word_list(["NOUN__NANPA"])}
            NUMBER__0: {Grammar._create_word_list(["NUMBER__0"])}  //ala
            NUMBER__1: {Grammar._create_word_list(["NUMBER__1"])}  //wan
            NUMBER__2: {Grammar._create_word_list(["NUMBER__2"])}  //tu
            NUMBER__5: {Grammar._create_word_list(["NUMBER__5"])}  //luka
            NUMBER__20: {Grammar._create_word_list(["NUMBER__20"])}  //mute
            NUMBER__100: {Grammar._create_word_list(["NUMBER__100"])}  //ale
            PARTICLE: {Grammar._create_word_list(["PARTICLE"])}
            PARTICLE__A: {Grammar._create_word_list(["PARTICLE__A"])}
            PARTICLE__ALA: {Grammar._create_word_list(["PARTICLE__ALA"])}
            PARTICLE__ANU: {Grammar._create_word_list(["PARTICLE__ANU"])}
            PARTICLE__E: {Grammar._create_word_list(["PARTICLE__E"])}
            PARTICLE__EN: {Grammar._create_word_list(["PARTICLE__EN"])}
            PARTICLE__LA: {Grammar._create_word_list(["PARTICLE__LA"])}
            PARTICLE__LI: {Grammar._create_word_list(["PARTICLE__LI"])}
            PARTICLE__O: {Grammar._create_word_list(["PARTICLE__O"])}
            PARTICLE__PAKALA: {Grammar._create_word_list(["PARTICLE__PAKALA"])}
            PARTICLE__PI: {Grammar._create_word_list(["PARTICLE__PI"])}
            PARTICLE__SEME: {Grammar._create_word_list(["PARTICLE__SEME"])}
            PREVERB: {Grammar._create_word_list(["PREVERB"])}
            PREPOSITION: {Grammar._create_word_list(["PREPOSITION"])}

            // Non-dictionary terminals
            PROPER_NAME: /\\b[A-Z][a-z]*\\b/
            UNKNOWN__WORD: /(?!\\b{'\\b|\\b'.join(Dictionary.get_words_for_parts_of_speech(Grammar._get_special_parts()))}\\b)(\\b([A-Za-z0-9]+)\\b)/
            UNKNOWN__X_ALA_X: /((?!\\b{'\\b|\\b'.join(Dictionary.get_words_for_parts_of_speech(Grammar._get_special_parts()))}\\b)(\\b([A-Za-z0-9]+)\\b)) ala \\1/

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
        return (
            '"'
            + '" | "'.join(Dictionary.get_words_for_parts_of_speech(parts_of_speech))
            + '"'
        )
