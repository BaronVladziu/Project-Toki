from typing import List

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
    - when node name contains "__" then only the part before "__" will appear in the output tree
    - when node name starts with "p_" then this node will be removed and its parent will adopt its children
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
        return GrammarParser._tree_to_phrases(
            GrammarParser._squash_private_nodes(GrammarParser._PARSER.parse(text)),
        )

    @staticmethod
    def _tree_to_phrases(tree: lark.lexer.Token | lark.tree.Tree) -> Phrase:
        """
        This method recursively converts lark tree to phrases and words.
        """
        if isinstance(tree, lark.lexer.Token):
            if tree.type.startswith("PUNCT_") or tree.type == "WS":
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
    def _squash_private_nodes(
        tree: lark.lexer.Token | lark.tree.Tree,
    ) -> lark.lexer.Token | lark.tree.Tree:
        """
        This method recursively removes private nodes while retaining its children.
        """
        if isinstance(tree, lark.lexer.Token):
            return tree
        else:
            new_children: list[lark.lexer.Token | lark.tree.Tree] = []
            found_any_private_nodes: bool = False
            for child in tree.children:
                if isinstance(child, lark.lexer.Token):
                    new_children.append(child)
                elif child.data.startswith("p_"):
                    new_children += [
                        GrammarParser._squash_private_nodes(x) for x in child.children
                    ]
                    found_any_private_nodes = True
                else:
                    new_children.append(GrammarParser._squash_private_nodes(child))
            tree.children = new_children
            if found_any_private_nodes:
                tree = GrammarParser._squash_private_nodes(tree)
            return tree
