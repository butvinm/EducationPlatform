from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout

import structures


class TextBlock(MDBoxLayout):
    """Widget for structure.TextBlock"""

    def __init__(self, block: structures.TextBlock, *args, **kwargs):
        """Build widget from block

        Args:
            block (structures.TextBlock): inherit structure
        """

        super().__init__(*args, **kwargs)

        self.adaptive_height = True
        self.add_widget(MDLabel(text=block.text, font_style='Body1', adaptive_height=True))
