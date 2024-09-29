from playwright.sync_api import Playwright, sync_playwright, expect
from pom.home_page_elements import HomePage
import pytest

def test_verifying_homepage(set_up):
    # page.pause()
    page  = set_up
    home_page = HomePage(page)
    expect(home_page.contacto).to_be_visible()
    expect(home_page.welcome).to_be_visible()

@pytest.mark.skip(reason="test not finished..")
def test_verifying_homepage2(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    page = browser.new_page()
    page.goto("https://qa-practice.netlify.app/")
    # page.pause()
    home_page = HomePage(page)
    expect(home_page.contacto).to_be_visible()
    expect(home_page.welcome).to_be_visible()