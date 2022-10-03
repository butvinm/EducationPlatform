from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout

import structures


class TitleBlock(MDBoxLayout):
    """Widget for structure.TitleBlock"""

    def __init__(self, block: structures.TitleBlock, *args, **kwargs):
        """Build widget from block

        Args:
            block (structures.TitleBlock): inherit structure
        """

        super().__init__(*args, **kwargs)
        self.adaptive_height = True
        self.add_widget(MDLabel(text=block.text, font_style='H6', adaptive_height=True))
