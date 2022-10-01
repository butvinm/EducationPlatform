from functools import partial

import context
from kivy.metrics import dp
from kivymd.uix.button import MDRoundFlatButton
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.stacklayout import MDStackLayout

from widgets.page_viewer import PageViewer
from widgets.pages.about_page import AboutPage
from widgets.pages.page import Page
from widgets.pages.practice_page import PracticePage
from widgets.pages.testing_page import TestingPage
from widgets.pages.theory_page import TheoryPage


class MenuItem(MDRoundFlatButton):
    def __init__(
        self,
        label: str,
        page_viewer: PageViewer,
        page_type: Page,
        drop_items: list[str],
        **kwargs
    ):
        super().__init__(**kwargs)
        self.text = label
        self.page_viewer = page_viewer

        if not drop_items:
            page = page_type(self.text)
            self.action = partial(self.page_viewer.open_page, page)
        else:
            self.dropdown = self._build_dropdown(page_type, drop_items)
            self.action = self.dropdown.open

    def on_press(self):
        self.action()
        return super().on_press()

    def _build_dropdown(self, page_type: Page, drop_items: list[str]) -> MDDropdownMenu:
        drop_items = [
            {
                'text': item,
                "height": dp(48),
                'viewclass': 'OneLineListItem',
                'on_release': partial(self.page_viewer.open_page, page_type(item))
            } for item in drop_items
        ]

        dropdown = MDDropdownMenu(
            caller=self,
            items=drop_items,
            width_mult=4,
        )
        return dropdown


class MenuBar(MDStackLayout):
    def __init__(self, page_viewer: PageViewer, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.adaptive_height = True
        self.padding = [dp(5)]
        self.spacing = [dp(10), 0]

        menu_items = self._build_menu_items(page_viewer)
        for menu_item in menu_items:
            self.add_widget(menu_item) 

    def _build_menu_items(self, page_viewer: PageViewer) -> list[MenuItem]:
        theory_menu_item = MenuItem(
            'Теория',
            page_viewer,
            TheoryPage,
            context.THEORY_DROP_ITEMS,
        )
        practice_menu_item = MenuItem(
            'Практика',
            page_viewer,
            PracticePage,
            context.PRACTICE_DROP_ITEMS,
        )
        testing_menu_item = MenuItem(
            'Тестирования',
            page_viewer,
            TestingPage,
            context.TESTING_DROP_ITEMS,
        )
        about_menu_item = MenuItem(
            'Об авторах',
            page_viewer,
            AboutPage,
            context.ABOUT_DROP_ITEMS,
        )

        return [
            theory_menu_item,
            practice_menu_item,
            testing_menu_item,
            about_menu_item
        ]
