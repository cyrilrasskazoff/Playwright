# сценарий заполнения веб-формы, используя встроенные локаторы Playwright.
def test_loc(page):
    page.goto('https://zimaev.github.io/text_input/')
    page.get_by_label("Email address").fill("qa@example.com")
    page.get_by_title("username").fill("Anton")
    page.get_by_placeholder('password').fill("secret")
    page.get_by_role('checkbox').click()

# Работа с несколькими элементами
def test_loc2(page):
    page.goto('https://zimaev.github.io/checks-radios/')
    checkboxes = page.locator("input")
    for checkbox in range(checkboxes.count()):
        checkboxes.nth(checkbox).click()

# Работа с несколькими элементами (версия playwright  >= 1.29)
# специализированный метод locator.all() для перебора всех совпадающих элементов. Если локатор находит несколько
# элементов, метод locator.all() возвращает массив локаторов указывающих на соответствующие элементы.

def test_loc2_new(page):
    page.goto('https://zimaev.github.io/checks-radios/')
    checkboxes = page.locator("input")
    for checkbox in checkboxes.all():
        checkbox.check()
