import os
import pytest
from loguru import logger
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrome_options
from pom.authorization_page_nav import AuthorizationPageNav


# Set this flag to True to use WebDriver.Remote
USE_REMOTE_DRIVER = True

@pytest.fixture(scope="function")
def get_chrome_options():
    """Get Chrome options."""
    options = chrome_options()
    options.headless = False  # Use headless if you do not need a browser UI
    options.add_argument("--start-maximized")
    options.add_argument("--window-size=1650,900")
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    return options


@pytest.fixture(scope="function")
def get_webdriver(get_chrome_options):
    """Get WebDriver"""
    options = get_chrome_options
    if USE_REMOTE_DRIVER:
        # Using WebDriver.Remote
        driver = webdriver.Chrome(
            options=options,
            # executable_path='/usr/local/bin/chromedriver',
        )
    else:
        # Using WebDriver.Chrome
        driver = webdriver.Chrome(options=options)
    return driver
    
    
@pytest.fixture(autouse=True, scope="function")
def auth_and_setup(get_webdriver):
    driver = get_webdriver
    driver.get("https://material-kit-pro-react.devias.io/dashboard/customers")
    page_nav = AuthorizationPageNav(driver)
    button_login = page_nav.get_button_login()
    button_login.click()
    yield 
    driver.quit()