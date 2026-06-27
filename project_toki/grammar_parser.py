import lark

from project_toki.grammar import Grammar
from project_toki.part_of_speech import PartOfSpeech
from project_toki.phrase import Phrase
from project_toki.punctuation import Punctuation
from project_toki.word import Word


class GrammarParser:
    """
    This class represents a parser that uses grammatical rules of toki pona to process any text.

    It has following features:
    - leaf "WS" and leaves with name starting with "PUNCT_" will be treated as punctuation
    - leaves of the grammar tree that are not punctuation must be named after a PartOfSpeech
    - when node name contains "__" then only the part before the leftmost "__" will appear in the output tree
    - when node name starts with "_" then this node will be removed and its parent will adopt its children
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
        return GrammarParser._split_x_ala_x(
            GrammarParser._tree_to_phrases(
                GrammarParser._remove_whitespaces(
                    GrammarParser._PARSER.parse(GrammarParser._preprocess_text(text)),
                ),
            ),
        )

    @staticmethod
    def _preprocess_text(text: str) -> str:
        """
        This method preprocesses input text to prevent some parsing errors.
        """
        if text == "":
            text = " "  # because lark fails on empty input
        return text

    @staticmethod
    def _tree_to_phrases(tree: lark.lexer.Token | lark.tree.Tree) -> Phrase:
        """
        This method recursively converts lark tree to phrases and words.
        """
        if isinstance(tree, lark.lexer.Token):
            if tree.type.startswith("PUNCT_"):
                return Phrase(
                    name=Punctuation(
                        text=tree.value,
                    ),
                )
            else:
                return Phrase(
                    name=Word(
                        text=tree.value.split("__")[0],
                        part_of_speech=PartOfSpeech(tree.type.split("__")[0]),
                    ),
                )
        elif isinstance(tree, lark.tree.Tree):
            return Phrase(
                name=tree.data.split("__")[0].upper(),
                children=[GrammarParser._tree_to_phrases(x) for x in tree.children],
            )
        else:
            raise TypeError(
                f'Expected tree of type "Token" or "Tree" but encountered "{tree}" of type "{type(tree)}"!',
            )

    @staticmethod
    def _split_x_ala_x(
        tree: Phrase,
    ) -> Phrase:
        """
        This method splits all "X ala X" phrases in the tree.
        """
        if tree.children is not None:
            new_children: list[Phrase] = []
            for child in tree.children:
                if isinstance(child.name, Word) and " ala " in child.name.text:
                    word1, word2 = child.name.text.split(" ala ")
                    new_children.append(
                        Phrase(
                            name=Word(
                                text=word1,
                                part_of_speech=child.name.part_of_speech,
                            ),
                        ),
                    )
                    new_children.append(
                        Phrase(
                            name=Word(
                                text="ala",
                                part_of_speech=PartOfSpeech.PARTICLE,
                            ),
                        ),
                    )
                    new_children.append(
                        Phrase(
                            name=Word(
                                text=word2,
                                part_of_speech=child.name.part_of_speech,
                            ),
                        ),
                    )
                else:
                    new_children.append(GrammarParser._split_x_ala_x(child))
            return Phrase(
                name=tree.name,
                children=new_children,
            )
        else:
            return tree

    @staticmethod
    def _remove_whitespaces(
        tree: lark.lexer.Token | lark.tree.Tree,
    ) -> lark.lexer.Token | lark.tree.Tree:
        """
        This method removes whitespaces from the tree.
        """
        if isinstance(tree, lark.lexer.Token):
            return tree
        else:
            new_children: list[lark.lexer.Token | lark.tree.Tree] = []
            for child in tree.children:
                if isinstance(child, lark.lexer.Token):
                    if not child.type.startswith("WS"):
                        new_children.append(child)
                else:
                    new_children.append(GrammarParser._remove_whitespaces(child))
            tree.children = new_children
            return tree
