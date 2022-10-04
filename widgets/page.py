import context
import structures
from kivy.metrics import dp
from kivymd.uix.label import MDLabel
from kivymd.uix.stacklayout import MDStackLayout
from structures import Content

from widgets.page_blocks import ImageBlock, TestBlock, TextBlock, TitleBlock


BLOCK_BUILDERS = {
    structures.TextBlock: TextBlock,
    structures.TitleBlock: TitleBlock,
    structures.ImageBlock: ImageBlock,
    structures.TestBlock: TestBlock
}


class Page(MDStackLayout):
    """Page widget generated from page-markup"""

    def __init__(self, name: str, content: Content, *args, **kwargs):
        """Set appearance and build children widgets by markup

        Args:
            name (str): name of page-markup file
            content (Content): content object with page blocks
        """

        super().__init__(*args, **kwargs)

        self.adaptive_height = True
        self.padding = [dp(20)]
        self.spacing = [0, dp(20)]

        self.name = name
        self._update_widgets(content)

    def _update_widgets(self, content: Content):
        """Set blocks widgets by content
        
        Args:
            content (Content): content object with page blocks
        """

        title = MDLabel(
            text=f'[u]{self.name}[/u]',
            font_style='H5',
            adaptive_height=True,
            markup=True
        )
        self.add_widget(title)

        for block in content:
            block_type = type(block)
            if block_type == structures.EndBlock:
                break

            block_builder = BLOCK_BUILDERS[block_type]
            block_widget = block_builder(block)
            self.add_widget(block_widget)

    @classmethod
    def from_content(cls, pages_content: dict[str, dict[str, Content]]) -> dict[str, dict[str, 'Page']]:
        """Build Page objects by content

        Args:
            pages_content (dict[str, dict[str, Content]]): content objects with pages blocks separated by groups

        Returns:
            dict[str, dict[str, Page]]: Page objects with names separated by groups
        """

        pages = {
            group: {
                page_name: Page(page_name, page_content)
                for page_name, page_content in group_pages.items()
            } for group, group_pages in pages_content.items()
        }

        return pages

    def __repr__(self) -> str:
        # because parent Widget object introspect itself before child object initialize
        name = self.__dict__.get('name')
        return f'Page(name={name})'
