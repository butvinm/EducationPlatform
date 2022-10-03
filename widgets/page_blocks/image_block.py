from typing import Optional

import structures
from kivy.metrics import dp
from kivy.uix.image import AsyncImage
from kivymd.uix.boxlayout import MDBoxLayout


class Image(AsyncImage):
    """ImageBlock Image class"""
    
    def __init__(self, source: str, size: Optional[int], *args, **kwargs):
        """Set appearance, source and size

        Args:
            source (str): url or file path
            size (Optional[int]): image height in dp
        """

        super().__init__(*args, **kwargs)        

        self.source = source
        self.size_hint = None, None
        self.allow_stretch = True
        self._size = dp(size) if size is not None else dp(150)

    def on_load(self, *args):
        """Fit by height"""

        self.height = self._size
        self.width = self._size * (self.texture.width / self.texture.height)

        return super().on_load(*args)


class ImageBlock(MDBoxLayout):
    """Widget for structure.ImageBlock"""

    def __init__(self, block: structures.ImageBlock, *args, **kwargs):
        """Build widget from block

        Args:
            block (structures.ImageBlock): inherit structure
        """

        super().__init__(*args, **kwargs)

        self.adaptive_height = True
        self.add_widget(Image(block.url, block.size))
