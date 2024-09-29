import pytest
from playwright.sync_api import Playwright

@pytest.fixture
def set_up(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    page = browser.new_page()
    page.goto("https://qa-practice.netlify.app/")
    page.set_default_timeout(3000)

    yield page