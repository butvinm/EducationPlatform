from kivymd.uix.dialog import MDDialog


class Banner(MDDialog):
    """Simple widget with notification"""

    def __init__(self, text: str, **kwargs):
        """Set appearance and attrs

        Args:
            text (str): displayed text      
        """
        super().__init__(**kwargs)

        self.text = text
        # self.right_action = ['OK', lambda x: None]