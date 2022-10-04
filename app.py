"""That strange construction fix kivy's bug with kivy core configuration"""

# autopep8: off
from kivy.config import Config

import context

Config.read(str(context.APP_CONFIG_PATH))
Config.write()

from kivymd.app import MDApp

from parse_utils.pages_parser import PagesParser
from widgets.main_widget import MainWidget

# autopep8: on


class Application(MDApp):
    def build(self) -> MainWidget:
        """Configure kivy core, set app options, parse pages and create main widget

        Returns:
            MainWidget: main application widget

        """

        self.title = context.TITLE
        self.icon = str(context.ICON)
        self.theme_cls.primary_palette = context.COLOR

        pages = PagesParser.get_pages(context.PAGES_PATH)
        pages = {group: pages[group] for group in context.GROUPS_ORDER}

        self.main_widget = MainWidget(pages)
        return self.main_widget


if __name__ == '__main__':

    Application().run()
