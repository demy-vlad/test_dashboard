import pytest
import time
import os
from loguru import logger
from pom.authorization_page_nav import AuthorizationPageNav


@pytest.mark.usefixtures(
    "get_webdriver"
)
class TestLogin(object):
    """Authorization"""
    def test_login(self, get_webdriver):
        driver = get_webdriver
        time.sleep(5)
        logger.debug(driver.title)
        assert "Dashboard: Customer List | Devias Kit PRO" in driver.title, "Authorization failed"