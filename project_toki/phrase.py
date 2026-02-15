import re

from anytree import NodeMixin, RenderTree

from project_toki.part_of_speech import PartOfSpeech
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

    @staticmethod
    def from_str(text: str) -> "Phrase":
        """
        This method creates Phrase object from string like:

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
        if text == "":
            raise ValueError(f'Expected phrase tree as text but received "{text}"!')
        return Phrase.from_lines(lines=text.splitlines())

    @staticmethod
    def from_lines(lines: list[str]) -> "Phrase":
        """
        This method creates Phrase object from list of strings like:

        [
            'TEXT',
            '└── SENTENCE',
            '    ├── NOUN_PHRASE',
            '    │   ├── NOUN: "toki"',
            '    │   └── ADJECTIVE_PHRASE',
            '    │       └── ADJECTIVE: "pona"',
            '    ├── PARTICLE: "li"',
            '    ├── VERB_PHRASE',
            '    │   └── ADJECTIVE_PHRASE',
            '    │       └── ADJECTIVE: "pona"',
            '    ├── PARTICLE: "a"',
            '    └── !',
        ]
        """
        return Phrase._parse_names(
            Phrase._from_lines_recursive(
                lines=lines,
            ),
        )

    @staticmethod
    def _from_lines_recursive(lines: list[str]) -> "Phrase":
        lines = [x.rstrip() for x in lines]
        lines = [x for x in lines if x]
        if len(lines) < 1:
            raise ValueError(f'Expected phrase tree as lines but received "{lines}"!')
        if lines[0].startswith(("├── ", "│   ", "└── ", "    ")):
            raise ValueError(f'Expected phrase tree as lines but received "{lines}"!')
        return Phrase(
            name=lines[0],
            children=[
                Phrase._from_lines_recursive(x)
                for x in Phrase._split_to_subphrases(lines[1:])
            ],
        )

    @staticmethod
    def _split_to_subphrases(lines: list[str]) -> list[list[str]]:
        output: list[list[str]] = []
        if len(lines) == 0:
            return output
        line_id: int = 0
        while lines[line_id].startswith("├── "):
            subphrase = Phrase._extract_mid_phrase(lines[line_id:])
            if len(lines[line_id:]) == len(subphrase):
                raise ValueError(
                    f'Failed to parse phrase tree "{lines}" on line "{lines[line_id]}"!',
                )
            output.append(subphrase)
            line_id += len(subphrase)
        if not lines[line_id].startswith("└── "):
            raise ValueError(
                f'Failed to parse phrase tree "{lines}" on line "{lines[line_id]}"!',
            )
        subphrase = Phrase._extract_end_phrase(lines[line_id:])
        if len(lines[line_id:]) != len(subphrase):
            raise ValueError(
                f'Failed to parse phrase tree "{lines}" on line "{lines[line_id]}"!',
            )
        output.append(subphrase)
        return output

    @staticmethod
    def _extract_mid_phrase(lines) -> list[str]:
        assert lines[0].startswith("├── ")
        output: list[str] = [lines[0][4:]]
        line_id: int = 1
        while line_id < len(lines) and lines[line_id].startswith("│   "):
            output.append(lines[line_id][4:])
            line_id += 1
        if len(output) < len(lines) and lines[len(output)].startswith("    "):
            raise ValueError(
                f'Failed to parse phrase tree "{lines}" on line "{lines[len(output)]}"!',
            )
        return output

    @staticmethod
    def _extract_end_phrase(lines) -> list[str]:
        assert lines[0].startswith("└── ")
        output: list[str] = [lines[0][4:]]
        line_id: int = 1
        while line_id < len(lines) and lines[line_id].startswith("    "):
            output.append(lines[line_id][4:])
            line_id += 1
        if len(output) < len(lines):
            raise ValueError(
                f'Failed to parse phrase tree "{lines}" on line "{lines[len(output)]}"!',
            )
        return output

    @staticmethod
    def _parse_names(input: Phrase) -> Phrase:
        input_name: str = str(input.name)
        if input.name == "":
            return input
        match = re.search(r'^(.+): "(.+)"$', input_name)
        output_name: str | Word | Punctuation = ""
        if match:
            output_name = Word(
                text=match.group(2),
                part_of_speech=PartOfSpeech(match.group(1)),
            )
        elif not input_name[0].isalpha():
            output_name = Punctuation(
                text=input_name,
            )
        else:
            output_name = input_name
        return Phrase(
            name=output_name,
            children=[Phrase._parse_names(x) for x in input.children],
        )

    def get_diff(self, other: Phrase) -> str:
        """
        This method returns a pretty diff between two phrases.
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
        return "\n" + "\n".join(output)

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
