from kivymd.uix.anchorlayout import MDAnchorLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.scrollview import MDScrollView

from widgets.page import Page


class PageViewer(MDAnchorLayout):
    """Widget provides displaying Page's with scrolling"""

    def __init__(self, *args, **kwargs):
        """Set appearance and create scrool view widget"""

        super().__init__(*args, **kwargs)
        self.anchor_x = 'center'
        self.anchor_y = 'top'

        scroll_view = MDScrollView()
        self.add_widget(scroll_view)
        
        self.container = MDBoxLayout(adaptive_height=True)
        scroll_view.add_widget(self.container)
        
    def open_page(self, page: Page):
        """Set page as ScrollView content

        Args:
            page (Page): _description_
        """

        self.container.clear_widgets()
        self.container.add_widget(page)
