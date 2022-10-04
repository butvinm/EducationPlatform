from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from structures import Content

from widgets.menu_bar import MenuBar
from widgets.page import Page
from widgets.page_viewer import PageViewer


class MainWidget(MDBoxLayout):
    def __init__(self, pages_content: dict[str, dict[str, Content]], *args, **kwargs):
        """Set appearance and add widgets

        Args:
            pages_content (dict[str, dict[str, Content]]): page contents separated by groups
        """

        super().__init__(*args, **kwargs)
        # widget properties
        self.orientation = 'vertical'

        self._update_widgets(pages_content)

    def _update_widgets(self, pages_content: dict[str, dict[str, Content]]):
        """Build Page objects from them contents, create PageViewer and MenuBar

        Args:
            pages_content (dict[str, dict[str, Content]]): page contents separated by groups
        """

        pages = Page.from_content(pages_content)
        self.page_viewer = PageViewer(pages)
        self.menu_bar = MenuBar(self.page_viewer)

        self.add_widget(self.menu_bar)
        self.add_widget(self.page_viewer)
