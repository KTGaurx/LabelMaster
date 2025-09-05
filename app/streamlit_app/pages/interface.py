# app/streamlit_app/pages/page_adapter.py

from abc import ABC, abstractmethod


class PageAdapter(ABC):
    @abstractmethod
    def render(self):
        """Render the page content."""
        pass

    def setup(self):
        """Optional setup before rendering."""
        pass
