from pom_project.pages.login_page_with_locators import LoginPageWithLocators
from pom_project.pages.dashboard_page_with_locators import DashboardPageWithLocators
import pytest
import allure

@allure.feature('Авторизация')
@allure.story('Авторизации недействительные учетные данные')
@allure.severity(allure.severity_level.CRITICAL)
@allure.title('Авторизаиця с недействительными учетными данными')

def test_login_failure_allure(login_page_with_locators):
    with allure.step('Открыть страницу авторизации'):
        login_page_with_locators.navigate()
    with allure.step('Ввести в форму авторизации недействительные учетные данные'):
        login_page_with_locators.login('invalid_user', 'invalid_password')
    with allure.step('Отображается ошибка - Invalid credentials. Please try again.'):
        assert login_page_with_locators.get_error_message() == 'Invalid credentials. Please try again.'


@allure.feature('Login')
@allure.story('Login with valid credentials')
@allure.severity(allure.severity_level.CRITICAL)
@allure.title('Авторизаиця с корректными учетными данными')
@pytest.mark.parametrize('username, password', [
    ('user', 'user'),
    ('admin', 'admin')
])
def test_login_success_allure(login_page_with_locators, dashboard_page_with_locators, username, password):
    with allure.step('Открыть страницу авторизации'):
        login_page_with_locators.navigate()
    with allure.step('Ввести в форму авторизации недействительные учетные данные'):
        login_page_with_locators.login(username, password)
    with allure.step('Отображается приветственное сообщение с именем пользователя'):
        assert dashboard_page_with_locators.get_welcome_message() == f"Welcome {username}"



