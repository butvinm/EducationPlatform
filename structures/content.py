from dataclasses import dataclass
from typing import Union

from structures.image_block import ImageBlock
from structures.test_block import TestBlock
from structures.text_block import TextBlock
from structures.title_block import TitleBlock


@dataclass
class Content:
    items: list[Union[TitleBlock, TextBlock, ImageBlock, TestBlock]]
