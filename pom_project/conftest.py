import pytest

from pom_project.pages.dashboard_page_with_locators import DashboardPageWithLocators
from pom_project.pages.login_page import LoginPage
from pom_project.pages.dashboard_page import DashboardPage
from pom_project.pages.login_page_with_locators import LoginPageWithLocators


@pytest.fixture
def login_page(page):
    return LoginPage(page)


@pytest.fixture
def login_page_with_locators(page):
    return LoginPageWithLocators(page)


@pytest.fixture
def dashboard_page(page):
    return DashboardPage(page)

@pytest.fixture
def dashboard_page_with_locators(page):
    return DashboardPageWithLocators(page)