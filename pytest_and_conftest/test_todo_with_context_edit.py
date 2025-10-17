# Редактирование контекста браузера
def test_add_todo_with_context_editing(page):  #! фикстуру browser_context_args не нужно передавать в качестве параметра
    page.goto("https://demo.playwright.dev/todomvc/#/")
    page.get_by_placeholder("What needs to be done?").click()
    page.get_by_placeholder("What needs to be done?").fill("Создать первый сценарий playwright")
    page.get_by_placeholder("What needs to be done?").press("Enter")

