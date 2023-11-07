"""authorization_page_nav.py."""
from base.seleniumbase import SeleniumBase


class CustomersPageNav(SeleniumBase):
    """CustomersPageNav."""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.customers = "#__next > div.css-1np3eo0 > div > main > div > div > div.MuiPaper-root.MuiPaper-elevation.MuiPaper-rounded.MuiPaper-elevation1.MuiCard-root.css-gnq6ov > div.MuiBox-root.css-79elbk > div.css-0 > div.simplebar-wrapper > div.simplebar-mask > div > div > div > table > tbody"
        self.returning = "#__next > div.css-1np3eo0 > div > main > div > div > div.MuiPaper-root.MuiPaper-elevation.MuiPaper-rounded.MuiPaper-elevation1.MuiCard-root.css-gnq6ov > div.MuiTabs-root.css-1edh49 > div.MuiTabs-scroller.MuiTabs-hideScrollbar.MuiTabs-scrollableX.css-12qnib > div > button.MuiButtonBase-root.MuiTab-root.MuiTab-textColorPrimary.Mui-selected.css-ty6wwo"

    def get_customers(self):
        """Get customers."""
        return self.is_visible("css", self.customers, "customers")

    def get_returning(self):
        """Get input returning."""
        return self.is_visible("css", self.returning, "returning")

    def get_button_login(self):
        """Get button login."""
        return self.is_visible("css", self.login_button, "button_login")
    
    def text_email(self) -> str:
        """Get error text email"""
        return self.get_text_from_webelement(
            self.is_visible("css", self.error_text_email, "text_email")
        )
    
    def text_password(self) -> str:
        """Get error text password"""
        return self.get_text_from_webelement(
            self.is_visible("css", self.error_text_password, "text_password")
        )