from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=2000)
    page = browser.new_page()
    page.goto("https://google.com")
    page.screenshot(path="sync_example.png")
    browser.close()