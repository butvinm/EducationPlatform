import context
import structures
from kivy.metrics import dp
from kivymd.uix.label import MDLabel
from kivymd.uix.stacklayout import MDStackLayout

from widgets.page_blocks import ImageBlock, TestBlock, TextBlock, TitleBlock

BLOCK_BUILDERS = {
    structures.TextBlock: TextBlock,
    structures.TitleBlock: TitleBlock,
    structures.ImageBlock: ImageBlock,
    structures.TestBlock: TestBlock
}


class Page(MDStackLayout):
    """Page widget generated from page-markup"""

    def __init__(self, group: str, name: str, *args, **kwargs):
        """Set appearance and build children widgets by markup

        Args:
            group (str): group of pages name
            name (str): name of page-markup file
        """

        super().__init__(*args, **kwargs)

        self.adaptive_height = True
        self.padding = [dp(20)]
        self.spacing = [0, dp(20)]

        self.group = group
        self.name = name
        self._update_widgets()

    def _update_widgets(self):
        """Set children widgets by Content from context.PAGES and page title"""

        title = MDLabel(
            text=f'[u]{self.name}[/u]', 
            font_style='H5', 
            adaptive_height=True, 
            markup=True
        )
        self.add_widget(title)

        content = context.PAGES[self.group][self.name]
        for block in content:
            block_type = type(block)
            if block_type == structures.EndBlock:
                break

            block_builder = BLOCK_BUILDERS[block_type]
            block_widget = block_builder(block)
            self.add_widget(block_widget)

    def __repr__(self) -> str:
        group = self.__dict__.get('group')
        name = self.__dict__.get('name')
        return f'Page({group=}, {name=})'
