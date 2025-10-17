from pom_project.pages.login_page import LoginPage
from pom_project.pages.dashboard_page import DashboardPage
import pytest


def test_login_failure(page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login('invalid_user', 'invalid_password')
    assert login_page.get_error_message() == 'Invalid credentials. Please try again.'


def test_login_success(page):
    login_page = LoginPage(page)
    dashboard_page = DashboardPage(page)

    login_page.navigate()
    login_page.login('admin', 'admin')

    dashboard_page.assert_welcome_message("Welcome admin")


# параметризация
@pytest.mark.parametrize('username, password', [
    ('user', 'user'),
    ('admin', 'admin')
])
def test_login_success(page, username, password):
    login_page = LoginPage(page)
    dashboard_page = DashboardPage(page)

    login_page.navigate()
    login_page.login(username, password)

    dashboard_page.assert_welcome_message(f"Welcome {username}")


# *********************************
# использование conftest.py:
# 1. Удалены импорты классов страниц
# 2. Фикстура page не передается в теста
# 3. Фикстуры login_page и dashboard_page используются для инициализации соответствующих объектов.
# 4. Тесты становятся более лаконичными и легко читаемыми.

def test_login_failure_with_conftest(login_page):
    login_page.navigate()
    login_page.login('user', 'password')

    assert login_page.get_error_message() == 'Invalid credentials. Please try again.'


@pytest.mark.parametrize('username, password', [
    ('user', 'user'),
    ('admin', 'admin')
])
def test_login_success_with_conftest(login_page, dashboard_page, username, password):
    login_page.navigate()
    login_page.login(username,password)
    dashboard_page.assert_welcome_message(f"Welcome {username}")


# *********************
# использование аннотаций Allure в тестах

import allure

@allure.feature('Авторизация')
@allure.story('Авторизации недействительные учетные данные')
@allure.severity(allure.severity_level.CRITICAL)
@allure.title('Авторизаиця с недействительными учетными данными')
def test_login_failure_allure(login_page):
    with allure.step('Открыть страницу авторизации'):
        login_page.navigate()
    with allure.step('Ввести в форму авторизации недействительные учетные данные'):
        login_page.login('invalid_user', 'invalid_password')
    with allure.step('Отображается ошибка - Invalid credentials. Please try again.'):
        assert login_page.get_error_message() == 'Invalid credentials. Please try again.'


@allure.feature('Login')
@allure.story('Login with valid credentials')
@allure.severity(allure.severity_level.CRITICAL)
@allure.title('Авторизаиця с корректными учетными данными')
@pytest.mark.parametrize('username, password', [
    ('user', 'user'),
    ('admin', 'admin')
])
def test_login_success_allure(login_page, dashboard_page, username, password):
    with allure.step('Открыть страницу авторизации'):
        login_page.navigate()
    with allure.step('Ввести в форму авторизации недействительные учетные данные'):
        login_page.login(username, password)
    with allure.step('Отображается приветственное сообщение с именем пользователя'):
        dashboard_page.assert_welcome_message(f"Welcome {username}")


