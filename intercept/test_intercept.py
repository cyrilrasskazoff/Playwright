# work with request
def test_listen_network(page):
    page.on("request", lambda request: print(">>", request.method, request.url))
    page.on("response", lambda response: print("<<", response.status, response.url))
    page.goto('https://onliner.by/')

# abort
def test_modify(page):
    page.route("**/*.{png,jpg,jpeg}", lambda route: route.abort())
    page.goto('https://onliner.by/')

# modify
def test_network(page):
    page.route("**/register", lambda route: route.continue_(post_data='{"email": "user","password": "secret"}'))
    page.goto('https://reqres.in/')
    page.get_by_text(' Register - successful ').click()
    response_code=page.locator('//span[@data-key="response-code"]')
    response_code.wait_for()
    expect(response_code).to_have_text('400')

# work with response: mock
from playwright.sync_api import expect

def test_intercepted(page):
    def handle_route(route):
        response = route.fetch()
        json = response.json()  # {"id":4,"token":"QpwL5tke4Pnpja7X4"}
        json["id"] = ["5"]
        json["token"] = ["newToken"]
        route.fulfill(json=json)

    page.route("**/api/register", handle_route)

    page.goto("https://reqres.in/")
    page.get_by_text(' Register - successful ').click()
    mocked_response = page.locator("//pre[@data-key='output-response']")
    mocked_response.wait_for()
    expect(mocked_response).to_contain_text("newToken")
    expect(mocked_response).to_contain_text("5")

# HAR
"""
1) В консоли введем следующую команду, чтобы записать данные har-файл
playwright open --save-har=example.har --save-har-glob="**/api/users/2" https://reqres.in                  
2) Редактируем полученный файл.
"""
def test_replace_from_har(page):
    page.goto("https://reqres.in/")
    page.route_from_har("example.har")
    users_single = page.locator('li[data-id="users-single"]')
    users_single.click()
    response = page.locator('[data-key="output-response"]')
    response.wait_for()
    expect(response).to_contain_text("This is a test text.")