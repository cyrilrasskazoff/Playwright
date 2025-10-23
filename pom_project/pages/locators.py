from playwright.sync_api import Page, Locator

class DashboardPageLocators:
    PROFILE = '#usernameDisplay'
    LOGOUT = '#logout'


class LoginPageLocators:
    USER_NAME_INPUT = '#username'
    PASSWORD_INPUT = '#password'
    LOGIN_BUTTON = '#login'
    ERROR_MESSAGE = '#errorAlert'



