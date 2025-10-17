import pytest
from pom_project.pages.login_page import LoginPage
from pom_project.pages.dashboard_page import DashboardPage


@pytest.fixture
def login_page(page):
    return LoginPage(page)


@pytest.fixture
def dashboard_page(page):
    return DashboardPage(page)