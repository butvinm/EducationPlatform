import context
from kivy.metrics import dp
from kivy.graphics import Color, Line
from kivymd.uix.stacklayout import MDStackLayout

from widgets.page_viewer import PageViewer
from widgets.menu_item import MenuItem


class MenuBar(MDStackLayout):
    """Widget located on the top of window. 
    Consisted MenuItem's for pages opening. MenuItem's are related on context.PAGES
    """

    def __init__(self, page_viewer: PageViewer, *args, **kwargs):
        """Set appearance and generate menu items

        Args:
            page_viewer (PageViewer): Widget for pages displaying
        """

        super().__init__(*args, **kwargs)
        self.adaptive_height = True
        self.padding = [dp(5)]
        self.spacing = [dp(10), 0]
        self.line_color = context.COLOR_RGB

        menu_items = self._build_menu_items(page_viewer)
        for menu_item in menu_items:
            self.add_widget(menu_item)

    def _build_menu_items(self, page_viewer: PageViewer) -> list[MenuItem]:
        """Build list of MenuItems from context.PAGES

        Args:
            page_viewer (PageViewer): Widget for pages displaying

        Returns:
            list[MenuItem]: list of MenuItems
        """

        menu_items = [
            MenuItem(group, list(pages.keys()), page_viewer)
            for group, pages in context.PAGES.items()
        ]
        return menu_items
