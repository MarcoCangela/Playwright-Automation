from playwright.sync_api import Playwright, sync_playwright, expect
from home_page_elements import HomePage

def verifying_homepage(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    page = browser.new_page()
    page.goto("https://qa-practice.netlify.app/")
    # page.pause()
    home_page = HomePage(page)
    expect(home_page.contacto).to_be_visible()
    expect(home_page.welcome).to_be_visible()

with sync_playwright() as playwright:
    verifying_homepage(playwright)