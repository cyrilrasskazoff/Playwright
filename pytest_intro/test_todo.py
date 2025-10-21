from playwright.sync_api import Playwright, sync_playwright, expect

def test_add_todo(playwright: Playwright) -> None:
    # browser = playwright.chromium.launch(headless=False) commented to avoid fails in github actions, caused by headed mode
    browser = playwright.chromium.launch()
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://demo.playwright.dev/todomvc/#/")
    page.get_by_placeholder("What needs to be done?").click()
    page.get_by_placeholder("What needs to be done?").fill("Создать первый сценарий playwright")
    page.get_by_placeholder("What needs to be done?").press("Enter")

    context.close()
    browser.close()