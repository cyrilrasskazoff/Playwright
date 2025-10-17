from playwright.sync_api import sync_playwright, expect
import pytest

@pytest.mark.parametrize("non_default_browser", ["firefox"])
def test_todo_with_ff(page, non_default_browser):
    page.goto("https://demo.playwright.dev/todomvc/#/")
    page.get_by_placeholder("What needs to be done?").click()
    page.get_by_placeholder("What needs to be done?").fill("Создать первый сценарий playwright")
    page.get_by_placeholder("What needs to be done?").press("Enter")

