from kivymd.uix.anchorlayout import MDAnchorLayout

from widgets.pages.page import Page


class PageViewer(MDAnchorLayout):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.md_bg_color = (1, 1, 0, 1)
        self.anchor_x = 'center'
        self.anchor_y = 'center'
    
    def open_page(self, page: Page):
        self.clear_widgets()
        self.add_widget(page)