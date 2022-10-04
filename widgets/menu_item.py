from functools import partial
from typing import Callable

from kivy.metrics import dp
from kivymd.uix.button import MDRoundFlatButton
from kivymd.uix.menu import MDDropdownMenu


class MenuItem(MDRoundFlatButton):
    """Widget contained at MenuBar.
    Call callback action on press with parameters of self and clicked dropdown item labels
    """

    def __init__(
        self,
        label: str,
        dropdown_labels: list[str],
        callback: Callable,
        **kwargs
    ):
        """Set appearance and build dropdown menu with pages names.
        Select action for one or more elements at group.

        Args:
            label (str): pages group name, displayed on button
            dropdown_labels (list[str]): group pages names, displayed in dropdown 
            callback (Callable): function called when item pressed. must get two arguments with item and dropdown labels
        """

        super().__init__(**kwargs)
        # widget properties
        self.text = label

        if len(dropdown_labels) == 1:
            self.action = partial(callback, label, dropdown_labels[0])
        else:
            self.dropdown = self._build_dropdown(dropdown_labels, callback)
            self.action = self.dropdown.open

    def _build_dropdown(self, dropdown_labels: list[str], callback: Callable) -> MDDropdownMenu:
        """Create MDDropdownMenu from dropdown_labels. 
        Dropdown's item pressing call page_viewer.open_page

        Args:
            dropdown_labels (list[str]): group pages names, displayed in dropdown
            callback (Callable): function called when dropdown item pressed

        Returns:
            MDDropdownMenu: dropdown menu
        """

        dropdown_items = [
            {
                'text': label,
                "height": dp(48),
                'viewclass': 'OneLineListItem',
                'on_release': partial(callback, self.text, label)
            } for label in dropdown_labels
        ]

        dropdown = MDDropdownMenu(
            caller=self,
            items=dropdown_items,
            width_mult=4,
        )
        return dropdown

    def on_press(self):
        """Action executed when button pressed.
        May be dropdown menu opening or calling of callback
        """

        self.action()
        return super().on_press()
