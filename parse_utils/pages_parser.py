import re
from concurrent.futures import process
from pathlib import Path
from typing import Optional, Union

from structures import (AnswerBlock, Content, EndBlock, ImageBlock, InputBlock,
                        QuestionBlock, TestBlock, TextBlock, TitleBlock)
from structures.test_block import TestQuestion


class ParseError(Exception):
    ...


class PagesParser:
    """Implement parsing of files with page markup and building content objects

    Page-markup block syntax:

        [TYPE] Entity:  TYPE is one of TITLE, TEXT, IMAGE, TEST, QUESTION, INPUT, ANSWER
                        Entity is string

    Types definitions (see structures/ and widgets/ for more details about types):

        [TITLE] text

        [TEXT] text

        [IMAGE] Optional(size, default=150), url | file_path

        [TEST] Optional(repeatable, default=0), title
            [QUESTION] text
            [INPUT] var1, var2, ... | NULL
            [ANSWER] text

        [END]

    !!! All files must ends with [END] block.
    """

    BLOCK_PATTERN = r'((?=\[\w+\])(.|\n)+?(?=\[\w+\]))|(\[END\])'
    TYPE_PATTERN = r'\[\w+\]'

    BLOCK_BUILDERS = {
        '[TITLE]': TitleBlock,
        '[TEXT]': TextBlock,
        '[IMAGE]': ImageBlock,
        '[TEST]': TestBlock,
        '[QUESTION]': QuestionBlock,
        '[INPUT]': InputBlock,
        '[ANSWER]': AnswerBlock,
        '[END]': EndBlock
    }
    TYPES_UNION = Union[TitleBlock, TextBlock, ImageBlock,
                        TestBlock, QuestionBlock, InputBlock, AnswerBlock]

    @classmethod
    def get_pages(cls, pages_path: Path) -> dict[str, dict[str, Content]]:
        """Parse pages content form pages_path.
        All subdirectories of pages_path interpretates as groups and
        all files in subdirectories parses as pages content.

        So if directory structure is:

            pages_path/
              |_PagesGroup1/
              |   |_page1
              |   |_page2
              |
              |_PagesGroup2/
                  |_page1

        The result will be:

        {
            'PagesGroup1': {
                'page1': <Content> object,
                'page2': <Content> object
            },
            'PagesGroup2': {
                'page1': <Content> object
            }
        }

        Args:
            pages_path (Path): destination of pages

        Returns:
            dict[str, dict[str, Content]]: dictionary with pages content (see structure above)
        """

        pages = {
            group.name: {
                page.name: cls.get_page(page)
                for page in group.iterdir() if page.is_file() and not page.suffix
            }
            for group in pages_path.iterdir() if group.is_dir()
        }

        return pages

    @classmethod
    def get_page(cls, page_path: Path) -> Content:
        """Get content of page from one file

        Args:
            page_path (Path): destination of content file

        Returns:
            Content: parsed page content (see structures/)
        """

        with open(str(page_path), 'r', encoding='utf-8') as f:
            file_text = f.read()

        content = cls.parse_text(file_text)
        return content

    @classmethod
    def parse_text(cls, text: str) -> Content:
        """Parse input string with rules defined in PageParser description

        Args:
            text (str): text for parsing

        Returns:
            Content: parsed content (see structures/)
        """

        content = []

        test_block: TestBlock = None
        question = TestQuestion()

        for match in re.finditer(cls.BLOCK_PATTERN, text):
            raw_block = match.group()
            raw_type = re.match(cls.TYPE_PATTERN, raw_block).group()
            raw_entity = raw_block.replace(raw_type, '').strip()

            block_type = cls.BLOCK_BUILDERS[raw_type]

            block, test_block, question = cls._process_block(
                block_type, raw_block, raw_type, raw_entity, test_block, question
            )
            if block is not None:
                if test_block is not None:
                    content.append(test_block)
                    test_block = None

                content.append(block)

        return content

    @classmethod
    def _process_block(
        cls,
        block_type: TYPES_UNION,
        raw_block: str,
        raw_type: str,
        raw_entity: str,
        test_block: Optional[TestBlock],
        question: Optional[TestQuestion]
    ) -> tuple[Optional[TYPES_UNION], TestBlock, Optional[TestQuestion]]:
        """Process and build block from raw data. Gradually build question and then test block. 

        Args:
            block_type (TYPES_UNION): block class (see structures/)
            raw_block (str): raw string block definition from parsed text. Uses for errors messages
            raw_type (str): raw string block type from parsed text. Uses for errors messages 
            raw_entity (str): raw string block entity from parsed text 
            test_block (Optional): closure for TestBlock building
            question (Optional): closure for TestQuestion building

        Returns:
            tuple[Optional[TYPES_UNION], TestBlock, Optional(TestQuestion)]: 
                first: New block or None if missed
                second: Updated (maybe not) test_block
                third: Updated (maybe not) question
        """

        if test_block is not None:
            if question.is_full:
                test_block.questions.append(question)
                question = TestQuestion()

            if block_type == QuestionBlock:
                if question.question is not None:
                    raise ParseError(
                        f'Double [QUESTION] block found at {raw_block}')

                question.question = block_type(raw_entity).question
                block = None
            elif block_type == InputBlock:
                if question.input is not None:
                    raise ParseError(
                        f'Double [INPUT] block found at {raw_block}')

                question.input = block_type(raw_entity).input
                block = None
            elif block_type == AnswerBlock:
                if question.answer is not None:
                    raise ParseError(
                        f'Double [ANSWER] block found at {raw_block}')

                question.answer = block_type(raw_entity).answer
                block = None
            else:
                if not question.is_empty:
                    raise ParseError(
                        f'Unexpected {raw_type} block in [TEST] block at {raw_block}')

                block = block_type(raw_entity)
        else:
            if block_type == TestBlock:
                test_block = TestBlock(raw_entity, [])
                block = None
            elif block_type in (QuestionBlock, InputBlock, AnswerBlock):
                raise ParseError(
                    f'Unexpected {raw_type} block out of [TEST] block at {raw_block}')
            else:
                block = block_type(raw_entity)

        return block, test_block, question
