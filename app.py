# do not replace imports
# this import order fix kivy Config bag

import context
from kivy.config import Config

Config.read(str(context.APP_CONFIG_PATH))
Config.write()

from kivymd.app import MDApp

from widgets.main_widget import MainWidget


class Application(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def build(self) -> MainWidget:
        """Configure kivy core, set app options, create main widget

        Returns:
            MainWidget: main application widget

        """

        self.title = context.TITLE
        self.icon = context.ICON
        self.theme_cls.primary_palette = context.COLOR
        context.COLOR_RGB = self.theme_cls.primary_color
        self.main_widget = MainWidget()

        return self.main_widget


if __name__ == '__main__':
    Application().run()
