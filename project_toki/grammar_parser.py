import lark

from project_toki.grammar import Grammar
from project_toki.part_of_speech import PartOfSpeech
from project_toki.phrase import Phrase
from project_toki.word import Word


class GrammarParser:
    """
    This class represents a parser that uses grammatical rules of toki pona to process any text.
    """

    _PARSER: lark.Lark = lark.Lark(
        Grammar.get_rules(),
        start="text",
        ambiguity="resolve",  # in case of a text fitting multiple grammatical trees, lark will choose the one with the highest priority
    )

    @staticmethod
    def parse_text(text: str) -> Phrase:
        """
        This method parses input text into a grammatical tree.
        """
        return GrammarParser._tree_to_phrases(GrammarParser._PARSER.parse(text))

    @staticmethod
    def _tree_to_phrases(tree: lark.lexer.Token | lark.tree.Tree) -> Phrase:
        """
        This method recursively converts lark tree to phrases and words
        """
        if isinstance(tree, lark.lexer.Token):
            return Phrase(
                name=Word(
                    text=tree.value,
                    part_of_speech=PartOfSpeech(tree.type),
                ),
            )
        elif isinstance(tree, lark.tree.Tree):
            return Phrase(
                name=tree.data.upper(),
                children=[GrammarParser._tree_to_phrases(x) for x in tree.children],
            )
        else:
            raise TypeError(
                f'Expected tree of type "Token" or "Tree" but encountered "{tree}" of type "{type(tree)}"!',
            )
