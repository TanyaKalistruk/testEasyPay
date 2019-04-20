from src import credentials
from src.PageObjects.page import Page
from src.Utilities.logger import logger
from src.locators import HomePage


class Login(Page):

    log = logger()

    def __init__(self, driver, base_url=''):
        super().__init__(driver, base_url)

    def set_email(self, email):
        self.get_element('email', 'id').clear()
        self.send_keys_to_element(email, 'email', 'id')

    def set_password(self, password):
        self.get_element('password', 'id').clear()
        self.send_keys_to_element(password, 'password', 'id')

    def sign_in(self):
        self.click_on_element('Login_button', 'id')

    def login(self, email, password):
        self.set_email(email)
        self.set_password(password)
        self.sign_in()
        self.wait_for_element(HomePage.DISPLAY_NAME)

    def login_as_admin(self):
        self.login(credentials.ADMIN_EMAIL, credentials.PASSWORD)
        return self

    def login_as_manager(self):
        self.login(credentials.MANAGER_EMAIL, credentials.PASSWORD)
        return self

    def login_as_inspector(self):
        self.login(credentials.INSPECTOR_EMAIL, credentials.PASSWORD)
        return self

    def login_as_user(self):
        self.login(credentials.USER_EMAIL, credentials.PASSWORD)
        return self
