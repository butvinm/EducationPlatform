from dataclasses import dataclass, field
from typing import Optional


@dataclass
class QuestionBlock:
    question: str


@dataclass(init=False)
class InputBlock:
    input: Optional[list[str]]

    def __init__(self, entity: str):
        """Set args from entity splitted by commas or replace empty string with None

        Args:
            entity (str): raw string block entity from parsed text 
        """

        splitted = entity.split(',')
        if len(splitted) <= 1: 
            self.input = []
        else:
            self.input = [i.strip() for i in splitted]
        

@dataclass
class AnswerBlock:
    answer: str


@dataclass
class TestQuestion:
    question: str = None
    input: list[str] = None
    answer: str = None

    @property
    def is_empty(self):
        return all(value is None for value in self.__dict__.values())

    @property
    def is_full(self):
        return all(value is not None for value in self.__dict__.values())
        

@dataclass(init=False)
class TestBlock:
    repeatable: bool
    title: str
    questions: list[TestQuestion]

    def __init__(self, entity: str, questions: list[str]) -> None:
        """Get repeatable and title splitted by comma from entry. 
        If no comma, repeatable is False

        Args:
            entity (str): raw string block entity from parsed text 
            questions (list[str]): test questions
        """
        
        splitted = entity.split(',')
        if len(splitted) == 1:
            self.repeatable = False
            self.title = splitted[0]
        elif len(splitted) == 2:
            repeatable, self.title = splitted
            self.repeatable = bool(int(repeatable))
        else:
            raise ValueError
        
        self.questions = questions