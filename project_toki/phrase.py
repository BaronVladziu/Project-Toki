from anytree import NodeMixin, RenderTree


class Phrase(NodeMixin):
    """
    This class represents a grammatical phrase.
    """

    def __init__(self, name, parent=None, children=None):
        self.name = name
        self.parent = parent
        if children:
            self.children = children

    def __str__(self) -> str:
        return f'\n{"\n".join(str(pre) + str(node.name) for pre, _, node in RenderTree(self))}'

    def __eq__(self, other) -> bool:
        return type(other) == type(self) and str(self) == str(other)

    def __hash__(self) -> int:
        return hash(str(self))
