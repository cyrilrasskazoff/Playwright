from playwright.sync_api import Page, expect
from .locators import LoginPageLocators


class LoginPageWithLocators:
    def __init__(self, page: Page):
        self.page = page
        self.locators = LoginPageLocators()

# Каждый метод в Page Class должен быть независимым и выполнять одну конкретную задачу

    def navigate(self):
        """Открывает страницу логина."""
        self.page.goto('https://zimaev.github.io/pom/')

    def login(self, username: str, password: str):
        """Выполняет вход с заданными учетными данными."""
        self.page.fill(self.locators.USER_NAME_INPUT, username)
        self.page.fill(self.locators.PASSWORD_INPUT, password)
        self.page.click(self.locators.LOGIN_BUTTON)

    def get_error_message(self):
        """Возвращает текст сообщения об ошибке."""
        return self.page.inner_text(self.locators.ERROR_MESSAGE)