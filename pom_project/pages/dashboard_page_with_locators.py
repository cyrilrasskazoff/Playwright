from playwright.sync_api import Page, expect
from .locators import DashboardPageLocators

class DashboardPageWithLocators:
    def __init__(self, page: Page):
        self.page = page
        self.locators = DashboardPageLocators

    def is_loaded(self) -> bool:
        return self.page.is_visible(self.locators.PROFILE)

    # def is_logout_button_present(self) -> bool:
    #     return self.page.is_visible(self.locators.LOGOUT)

    def get_welcome_message(self):
        # return self.page.text_content(self.locators.PROFILE)
        return self.page.text_content(self.locators.PROFILE)