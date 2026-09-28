from playwright.sync_api import Page

class LoginPage:

    def __init__(self, page: Page):
        self.page = page
        self.username = page.locator("#user-name")
        self.password = page.locator("#password")
        self.login_button = page.locator("#login-button")
        self.err_msg =page.locator('[data-test="error"]')

    def open(self):
        self.page.goto("https://www.saucedemo.com/")

    def login(self, username: str, password: str):
        self.username.fill(username)
        self.password.fill(password)
        self.login_button.click()

    def is_logged_in(self):
        return self.page.url == "https://www.saucedemo.com/inventory.html"

    def get_error_message(self):
        return self.err_msg.inner_text()