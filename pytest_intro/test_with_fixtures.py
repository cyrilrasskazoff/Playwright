"""
Fixtures — это функции, выполняемые pytest до или после тестовых функций. Это способ выполнения действий для теста, но
не внутри тестовой функции. Основная задача фикстуры - создание соответствующего тестового окружения.
Чтобы сообщить pytest,  что данная функция является фикстурой, необходимо импортировать библиотеку pytest и использовать
 декоратор@pytest.fixture  для функции которая будет выступать фикстурой. Для того чтобы задействовать фикстуру для
 теста, необходимо передать имя данной фикстуры в список параметров тестовой функции.
"""
from playwright.sync_api import sync_playwright, expect
import pytest
@pytest.fixture()
def browser_fixture():
    with sync_playwright() as playwright:
        # browser = playwright.chromium.launch(headless=False)
        browser = playwright.chromium.launch()
        context = browser.new_context()
        page = context.new_page()
        yield page
        page.close()
        browser.close()


# the code below is commented to avoid fail in github actions
# def test_todo_with_fixt(browser_fixture):
#     browser_fixture.goto("https://demo.playwright.dev/todomvc/#/")
#     browser_fixture.get_by_placeholder("What needs to be done?").click()
#     browser_fixture.get_by_placeholder("What needs to be done?").fill("Создать первый сценарий playwright")
#     browser_fixture.get_by_placeholder("What needs to be done?").press("Enter")

"""
Но Playwright подготовил готовое решение и этого вопроса - pytest-playwright
Аддон pytest-playwright реализует несколько фикстур. Наиболее широко используемой из которых является фикстура - "page".
Фикстура page предоставляет новую веб-страницу для запуска теста и функции для работы с ней.
Перепишем записанный код для запуска его с помощью pytest и фикстур из аддона  pytest-playwright
"""
def test_add_todo_with_fixture(page):
    page.goto("https://demo.playwright.dev/todomvc/#/")
    page.get_by_placeholder("What needs to be done?").click()
    page.get_by_placeholder("What needs to be done?").fill("Создать первый сценарий playwright")
    page.get_by_placeholder("What needs to be done?").press("Enter")

"""
По умолчанию pytest-playwright делает браузер headless(безголовым). Если вы хотите выполнить в режиме headed, передайте 
параметр, как показано ниже:
pytest --headed
Либо сконфигуировав файл pytest.ini
"""

