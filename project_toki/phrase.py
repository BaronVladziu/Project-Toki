from anytree import NodeMixin, RenderTree

from project_toki.punctuation import Punctuation
from project_toki.word import Word


class Phrase(NodeMixin):
    """
    This class represents a grammatical phrase.
    """

    def __init__(
        self,
        name: str | Word | Punctuation,
        parent: None | Phrase = None,
        children: None | list[Phrase] = None,
    ):
        self.name: str | Word | Punctuation = name
        self.parent: None | Phrase = parent
        if children:
            self.children: list[Phrase] = children

    def get_diff(self, other: Phrase) -> str:
        """
        This method returns a pretty diff between phrases
        """
        lines_self: list[str] = str(self).splitlines()
        lines_other: list[str] = str(other).splitlines()
        max_line_len: int = max(len(x) for x in lines_self)
        output: list[str] = []
        for line_id in range(max(len(lines_self), len(lines_other))):
            line_self: str = lines_self[line_id] if line_id < len(lines_self) else ""
            line_other: str = lines_other[line_id] if line_id < len(lines_other) else ""
            diff_marker: str = "X" if line_self != line_other else " "
            output.append(
                diff_marker + " " + line_self.ljust(max_line_len + 1, " ") + line_other,
            )
        return "\n".join(output)

    def __str__(self) -> str:
        """
        This method creates str object like:

        TEXT
        └── SENTENCE
            ├── NOUN_PHRASE
            │   ├── NOUN: "toki"
            │   └── ADJECTIVE_PHRASE
            │       └── ADJECTIVE: "pona"
            ├── PARTICLE: "li"
            ├── VERB_PHRASE
            │   └── ADJECTIVE_PHRASE
            │       └── ADJECTIVE: "pona"
            ├── PARTICLE: "a"
            └── !
        """
        return f'{"\n".join(str(pre) + str(node.name) for pre, _, node in RenderTree(self))}'

    def __eq__(self, other) -> bool:
        return type(other) == type(self) and str(self) == str(other)

    def __hash__(self) -> int:
        return hash(str(self))
