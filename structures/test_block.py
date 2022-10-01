from dataclasses import dataclass, field
from typing import Optional


@dataclass
class QuestionBlock:
    question: str


@dataclass
class InputBlock:
    input: Optional[list[str]]

    def __post_init__(self):
        """Split args splitted with commas or replace empty string with None"""

        if not self.input:
            self.input = None
        else:
            self.input = [i.strip() for i in self.input.split(',')]

            
@dataclass
class AnswerBlock:
    answer: str


@dataclass
class TestQuestion:
    question: QuestionBlock = None
    input: InputBlock = None
    answer: AnswerBlock = None


@dataclass
class TestBlock:
    questions: list[TestQuestion] = field(default_factory=list)