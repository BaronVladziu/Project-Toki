import json
from pathlib import Path


class Dictionary:
    """
    This class represents an toki pona dictionary
    and provides useful to extract information from itself.
    """

    with open(Path(__file__).parent / "dictionary_data.json") as f:
        DATA = json.load(f)

    @staticmethod
    def extract_parts_of_speech(word: str) -> set[str]:
        """
        This method returnes all parts of speech that fit given word.
        """
        output: set[str] = set()
        if word in Dictionary.DATA["words"]:
            if "definition" in Dictionary.DATA["words"][word]:
                output |= {x for x in Dictionary.DATA["words"][word]["definition"]}
        if output:
            return output
        else:
            return {"UNKNOWN"}

    @staticmethod
    def extract_definition(word: str, part_of_speech: str) -> str:
        """
        This method returnes a definition of a given word
        when used as a given part of speech.
        """
        if word in Dictionary.DATA["words"]:
            if "definition" in Dictionary.DATA["words"][word]:
                if part_of_speech in Dictionary.DATA["words"][word]["definition"]:
                    return Dictionary.DATA["words"][word]["definition"][part_of_speech]
        raise ValueError(
            f'There is no database entry for "{word}" as a "{part_of_speech}"!',
        )

    @staticmethod
    def get_words_for_part_of_speech(part_of_speech: str) -> set[str]:
        """
        This method returnes all words that may be used as a gived part of speech.
        """
        output: set[str] = set()
        for word in Dictionary.DATA["words"]:
            if "definition" in Dictionary.DATA["words"][word]:
                if part_of_speech in Dictionary.DATA["words"][word]["definition"]:
                    output.add(word)
        return output
