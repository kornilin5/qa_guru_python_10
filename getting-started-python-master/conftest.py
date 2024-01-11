import pytest
from selene import browser

@pytest.fixture()
def options_browser():
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    yield
    browser.quit()
    