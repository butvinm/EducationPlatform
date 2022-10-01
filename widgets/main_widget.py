from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout

from widgets.menu_bar import MenuBar
from widgets.page_viewer import PageViewer


class MainWidget(MDBoxLayout):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.orientation = 'vertical'

        self.page_viewer = PageViewer()
        self.menu_bar = MenuBar(self.page_viewer)

        self.add_widget(self.menu_bar)
        self.add_widget(self.page_viewer)
