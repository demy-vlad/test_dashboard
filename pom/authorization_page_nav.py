"""authorization_page_nav.py."""
from base.seleniumbase import SeleniumBase


class AuthorizationPageNav(SeleniumBase):
    """AuthorizationPageNav."""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.user_email = "#email"
        self.password = "#password"
        self.login_button = "div.MuiCardContent-root.css-1dzn5ey > form > button"
        self.error_text_email = "#form_auth > div:nth-child(2) > div"
        self.error_text_password = "#form_auth > div.mt-3 > div"
        ERROR_TEXT_EMAIL = "The email field is required."
        ERROR_TEXT_PASSWORD = "The password field is required."

    def get_input_email(self):
        """Get input username."""
        return self.is_visible("css", self.user_email, "input_email")

    def get_input_password(self):
        """Get input password."""
        return self.is_visible("css", self.password, "input_password")

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