import pytest

# доки со всеми параметрами контекста смотри по ссылке ниже
# https://playwright.dev/python/docs/api/class-browser#browser-new-context%C2%A0

# фикстура для изменения размера окна браузера
@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {

        "viewport": {
            "width": 1920,
            "height": 1080,
        }
    }

