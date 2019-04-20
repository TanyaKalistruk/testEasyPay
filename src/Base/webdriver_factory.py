from selenium import webdriver
from src.url import login_page


def get_chrome_driver():
    return webdriver.Chrome()


def get_firefox_driver():
    return webdriver.Firefox()


def get_edge_driver():
    return webdriver.Edge()


def get_opera_driver():
    return webdriver.Opera()


class WebdriverFactory:

    def __init__(self, browser, base_url=login_page):
        self.browser = browser
        self.base_url = base_url

    def get_webdriver_instance(self):
        browser = self.browser.lower()
        if browser == 'firefox':
            driver = get_firefox_driver()
        elif browser == 'chrome':
            driver = get_chrome_driver()
        elif browser == 'edge':
            driver = get_edge_driver()
        elif browser == 'opera':
            driver = get_opera_driver()
        else:
            print("Browser: %s not supported!" % browser)
            raise NotImplementedError
        driver.implicitly_wait(3)
        driver.maximize_window()
        driver.get(self.base_url)
        return driver
