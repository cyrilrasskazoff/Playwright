# Checkbox, radio buttons, toggle
def test_checkbox(page):
    page.goto('https://zimaev.github.io/checks-radios/')
    page.locator("text=Default checkbox").check()
    page.locator("text=Checked checkbox").check()
    page.locator("text=Default radio").check()
    page.locator("text=Default checked radio").check()
    page.locator("text=Checked switch checkbox input").check()


def test_checkbox2(page):
    page.goto('https://zimaev.github.io/checks-radios/')
    page.locator("text=Default checkbox").click()
    page.locator("text=Checked checkbox").click()
    page.locator("text=Default radio").click()
    page.locator("text=Default checked radio").click()
    page.locator("text=Checked switch checkbox input").click()


# Выпадающий список
def test_select(page):
    page.goto('https://zimaev.github.io/select/')
    page.select_option('#floatingSelect', value="3")
    page.select_option('#floatingSelect', index=1)
    page.select_option('#floatingSelect', label="Нашел и завел bug")

# Если в вашем приложении реализован множественный выбор в выпадающем списке, то для реализации данного сценария
# необходимо передать массив опций, который требуется выбрать.
def test_select_multiple(page):
    page.goto('https://zimaev.github.io/select/')
    page.select_option('#skills', value=["playwright", "python"])


# Drag&Drop
def test_drag_and_drop(page):
    page.goto('https://zimaev.github.io/draganddrop/')
    page.drag_and_drop("#drag", "#drop")

# Диалоговые окна
# действия по умолчанию
def test_dialogs(page):
    page.goto("https://zimaev.github.io/dialog/")
    page.get_by_text("Диалог Alert").click()
    page.get_by_text("Диалог Confirmation").click()  # по умолчанию: dismiss
    page.get_by_text("Диалог Prompt").click()  # по умолчанию: dismiss

# вариативныя работа с окнами
def test_dialogs_non_default(page):
    """
    page.once - прослушивает события которые, происходит в приложении
    "dialog" - указывает на тип события которое нужно обработать
    lambda dialog: dialog.accept() - анонимная функция обрабатывающая событие, анонимная функция, в качестве параметра
    принимает экземпляр класса Dialog
    """
    page.goto("https://zimaev.github.io/dialog/")
    page.once("dialog", lambda dialog: dialog.accept())
    page.get_by_text("Диалог Confirmation").click()

    page.once("dialog", lambda dialog: dialog.accept('15'))
    page.get_by_text("Диалог Prompt").click()


# Загрузка файла
import os
import pathlib
current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'hello.txt')    # добавляем к этому пути имя файла
def test_select_file(page):
    page.goto('https://zimaev.github.io/upload/')
    page.on("filechooser", lambda file_chooser: file_chooser.set_files(file_path))
    page.locator("#formFile").click()


# another way
absol_path = os.path.abspath(pathlib.Path('actions', 'hello.txt'))
def test_select_file_1(page):
    page.goto('https://zimaev.github.io/upload/')
    with page.expect_file_chooser() as fc_info:
        page.locator("#formFile").click()
    file_chooser = fc_info.value
    file_chooser.set_files(absol_path)


# Скачивание файлов
def test_download(page):

    page.goto("https://demoqa.com/upload-download")

    with page.expect_download() as download_info:
        page.locator("a:has-text(\"Download\")").click()

    download = download_info.value
    file_name = download.suggested_filename
    destination_folder_path = "actions/data/"
    download.save_as(os.path.join(destination_folder_path, file_name))

# извлечь данные с веб-страниц
def test_extract_data(page):
    page.goto('https://zimaev.github.io/table/')
    row = page.locator("tr")
    print(row.all_inner_texts())
    print("*"*100)
    print(row.all_text_contents())


# скринщоты
def test_screenshot(page):
    destination_folder = "actions/screenshots/"
    page.goto('https://zimaev.github.io/table/')
    page.screenshot(path=os.path.join(destination_folder, "screenshot.jpeg"), full_page=True, type="jpeg", quality=100)


# Работа с несколькими вкладками(Tabs)
def test_new_tab(page):
    page.goto("https://zimaev.github.io/tabs/")
    with page.context.expect_page() as tab:
        page.get_by_text("Переход к Dashboard").click()

    new_tab = tab.value
    assert new_tab.url == "https://zimaev.github.io/tabs/dashboard/index.html?"
    sign_out = new_tab.locator('.nav-link', has_text='Sign out')
    assert sign_out.is_visible()