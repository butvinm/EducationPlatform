import context
from kivy.metrics import dp
from kivy.graphics import Color, Line
from kivymd.uix.stacklayout import MDStackLayout

from widgets.page_viewer import PageViewer
from widgets.menu_item import MenuItem


class MenuBar(MDStackLayout):
    """Widget located on the top of window. 
    Consists MenuItem's implementing PageViewer pages opening
    """

    def __init__(self, page_viewer: PageViewer, *args, **kwargs):
        """Set appearance and build menu items

        Args:
            page_viewer (PageViewer): Widget for pages displaying
        """

        super().__init__(*args, **kwargs)
        # widget properties
        self.adaptive_height = True
        self.padding = [dp(5)]
        self.spacing = [dp(10), 0]
        self.line_color = context.COLOR_RGB

        self._update_widgets(page_viewer)

    def _update_widgets(self, page_viewer: PageViewer) -> list[MenuItem]:
        """Build list of MenuItems by PageViewer pages

        Args:
            page_viewer (PageViewer): Widget for pages displaying

        Returns:
            list[MenuItem]: list of MenuItems
        """

        for group, pages in page_viewer.pages.items():
            menu_item = MenuItem(group, list(pages.keys()), page_viewer.open_page)        
            self.add_widget(menu_item)
            