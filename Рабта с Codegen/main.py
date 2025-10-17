# Для запуска codegen откройте терминал,  введите  приведенную ниже команду и нажмите Enter.
# playwright codegen demo.playwright.dev/todomvc/#/

import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    # запуск браузера chromium
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    # Следующие три строки отвечают за запуск браузера и создание в нем контекста
    context = browser.new_context()  # new_context() - создает изолированный сеанс браузера
    page = context.new_page()   # new_page()  - открывает новую страницу(tab) в браузере
    page.goto("https://demo.playwright.dev/todomvc/#/")
    page.get_by_placeholder("What needs to be done?").click()  # С помощью метода get_by_placeholder("What needs to be
    # done?")  playwright находит в DOM дереве веб-элемент  c  атрибутом тега placeholder и значением атрибута
    # What needs to be done?
    page.get_by_role("textbox", name="What needs to be done?").fill("Создать первый сценарий playwright")
    page.get_by_role("textbox", name="What needs to be done?").press("Enter")
    page.get_by_text("Mark all as complete").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)

# **********************************************
"""
Codegen
Дополнительные опции Codegen
Помимо указания url, сodegen может принимать еще несколько дополнительных атрибутов.

Общий синтаксический формат для записи сценария выглядит так:

codegen [параметры] [url]
                  
Узнать доступные опции и краткое их описание можно, выполнив команду

playwright codegen --help

пример использования:  playwright codegen -o lesson.py --viewport-size=800,600 https://demo.playwright.dev/todomvc/#/  
"""
# *********************************************
"""
Playwright  работает с тремя различными слоями, которые строятся друг на друге:  Browser, Context и Page.

Browsers
Для работы каждой версии  Playwright требуются определенные версии браузеров. В отличие от Selenium, Playwright не 
использует webdriver. С каждой новым выпуском, Playwright обновляет версии браузеров которые он поддерживает. Это 
означает, что при каждом обновлении Playwright вам, возможно придется заново запускать команду  playwright install

Для Google Chrome, Microsoft Edge и других браузеров на базе Chromium по умолчанию Playwright использует сборки Chromium
с открытым исходным кодом.

BrowserContext
Playwright использует контексты браузера для достижения изоляции тестов. Страницы в двух отдельных контекстах не имеют 
общих cookie, настроек профиля.  Контекстом можно назвать независимую сессию браузера, схожую с режимом инкогнито. По 
сравнению с Selenium, они не требуют собственного процесса браузера.Для получения чистой среды тест может просто открыть
 новый контекст. Как правило, каждый тест имеет свой собственный контекст.

Pages
Page содержит содержимое загруженного веб-сайта.Каждый Context может иметь несколько страниц. Используется для навигации
 по URL-адресам и взаимодействия с содержимым страницы.
"""
