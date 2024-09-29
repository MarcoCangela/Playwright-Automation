import re
from playwright.sync_api import Playwright, sync_playwright, expect

# PLaying with automation on a basic netlify page
def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://qa-practice.netlify.app/")
    page.get_by_role("link", name="Contact").click()
    page.get_by_role("link", name="Home").click()
    page.locator("#sidebarCollapse").click()
    page.locator("#sidebarCollapse").click()
    page.get_by_role("link", name="Intercept API Request").click()
    page.get_by_role("link", name="Tables").click()
    page.get_by_role("link", name="Dynamic Table").click()
    with page.expect_popup() as page1_info:
        page.get_by_role("link", name="Learn with RV - YouTube").click()
    page1 = page1_info.value
    page1.close()
    page.get_by_role("link", name="QA Practice").click()
    page.get_by_role("link",name="Forms").click()
    page.get_by_role("link", name="Register").click()
    page.get_by_placeholder("Enter first name").fill("Marco")
    page.get_by_placeholder("Enter last name").fill("Garujo")
    page.get_by_placeholder("Enter phone number").fill("827025827")
    page.locator("#countries_dropdown_menu").select_option('Mozambique')
    page.get_by_placeholder("Enter email").fill("Testemail@email.com")
    page.get_by_placeholder("Password").fill("asdadadsad")
    page.get_by_label("I agree with the terms and").click()
    page.get_by_role("button", name="Register").click()
    page.wait_for_load_state("networkidle")
    expect(page.get_by_text("The account has been"))
    page.pause()

    # expect(page.locator("#sidebarCollapse")).to_be_visible()
    print("Execution Finished")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)