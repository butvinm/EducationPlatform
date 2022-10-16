from kivymd.uix.floatlayout import MDFloatLayout
from kivy.uix.image import AsyncImage


class PreviewImage(MDFloatLayout):
    """Widget that shown in PageViewer first"""


    def __init__(self, image_path: str, *args, **kwargs):
        """Set appearance and widgets

        Args:
            image_path (str): Path to image
        """

        super().__init__(*args, **kwargs)

        self._update_widgets(image_path)
    
    def _update_widgets(self, image_path: str):
        """Add image widget

        Args:
            image_path (str): path to image
        """
        
        image = AsyncImage(source=image_path)
        self.add_widget(image)