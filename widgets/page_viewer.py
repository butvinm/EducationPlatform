from kivymd.uix.anchorlayout import MDAnchorLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.scrollview import MDScrollView

from widgets.page import Page
from widgets.preview_image import PreviewImage
import context


class PageViewer(MDAnchorLayout):
    """Widget provides displaying Page's with scrolling"""

    def __init__(self, pages: dict[str, dict[str, Page]], *args, **kwargs):
        """Set appearance and widgets

        Args:
            pages (dict[str, dict[str, Page]]): dictionary with Page objects separated by groups 
        """

        super().__init__(*args, **kwargs)
        # widget properties
        self.anchor_x = 'center'
        self.anchor_y = 'top'

        self.pages = pages
        self._update_widgets()

    def _update_widgets(self):
        """Create scroll view and pages's container"""

        self.preview_image = PreviewImage(context.PREVIEW_IMAGE_PATH.as_posix()) 
        self.add_widget(self.preview_image)

        scroll_view = MDScrollView()
        self.add_widget(scroll_view)

        self.container = MDBoxLayout(adaptive_height=True)
        scroll_view.add_widget(self.container)

    def open_page(self, group: str, page_name: str):
        """Get page by group and name and set to container

        Args:
            group (str): name of pages group
            page_name (str): name of page 
        """

        if hasattr(self, 'preview_image'):
            self.remove_widget(self.preview_image)
            del self.preview_image

        page = self.pages.get(group, {}).get(page_name, None)
        if page is not None:
            self.container.clear_widgets()
            self.container.add_widget(page)
