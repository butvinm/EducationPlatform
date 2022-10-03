from functools import partial

from kivy.metrics import dp
from kivymd.uix.button import MDRoundFlatButton
from kivymd.uix.menu import MDDropdownMenu

from widgets.page import Page
from widgets.page_viewer import PageViewer


class MenuItem(MDRoundFlatButton):
    """Widget contained at MenuBar. Represents on group of pages.
    Provide page opening by dropdown menu or button click(for one-element groups)
    """

    def __init__(
        self,
        label: str,
        dropdown_labels: list[str],
        page_viewer: PageViewer,
        **kwargs
    ):
        """Set appearance and build dropdown menu with pages names.
        Select action for one or more elements at group.

        Args:
            label (str): pages group name, displayed on button
            dropdown_labels (list[str]): group pages names, displayed in dropdown 
            page_viewer (PageViewer): widget provides pages displaying
        """

        super().__init__(**kwargs)
        self.text = label

        if len(dropdown_labels) == 1:
            page = Page(label, dropdown_labels[0])
            self.action = partial(page_viewer.open_page, page)
        else:
            self.dropdown = self._build_dropdown(dropdown_labels, page_viewer)
            self.action = self.dropdown.open

    def on_press(self):
        """Action executed when button pressed.
        May be dropdown menu opening or page displaying
        """

        self.action()
        return super().on_press()

    def _build_dropdown(self, dropdown_labels: list[str], page_viewer: PageViewer) -> MDDropdownMenu:
        """Create MDDropdownMenu from dropdown_labels. 
        Dropdown's item pressing call page_viewer.open_page

        Args:
            dropdown_labels (list[str]): group pages names, displayed in dropdown
            page_viewer (PageViewer): widget provides pages displaying

        Returns:
            MDDropdownMenu: dropdown menu
        """
        dropdown_items = [
            {
                'text': label,
                "height": dp(48),
                'viewclass': 'OneLineListItem',
                'on_release': partial(page_viewer.open_page, Page(self.text, label))
            } for label in dropdown_labels
        ]

        dropdown = MDDropdownMenu(
            caller=self,
            items=dropdown_items,
            width_mult=4,
        )
        return dropdown
