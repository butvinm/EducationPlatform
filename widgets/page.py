from typing import Union
from kivymd.uix.stacklayout import MDStackLayout
from context import context
from structures.content import Content

class Page(MDStackLayout):
    def __init__(self, group: str, name: str, *args, **kwargs):
        super().__init__(*args, **kwargs)

        content = context.PAGES[group][name]
        self._update_content(content)
    
    def _update_content(self, content: Content):
        pass
