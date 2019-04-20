from selenium.webdriver.common.keys import Keys

from src import test_data
from src.locators import HomePage, PathToCounters, SelectedAddress, NewValue
from src.PageObjects.page import Page
from src.Utilities.logger import logger


class Counters(Page):

    log = logger()

    def __init__(self, driver, base_url=''):
        super().__init__(driver, base_url)
        self.wait_for_element(HomePage.DISPLAY_NAME)

    def open_counters_page(self):
        self.click_on_element(PathToCounters.MENU_ITEM)\
            .wait_for_element(PathToCounters.PANEL)
        return self

    def expand_counters_dropdown(self):
        self.click_on_element(PathToCounters.DROPDOWN)\
            .wait_for_element(PathToCounters.ADDRESSES_LIST)
        return self

    def choose_address(self):
        self.click_on_element(PathToCounters.ADDRESS_INPUT)
        self.send_keys_to_element(test_data.ADDRESS,
                                  PathToCounters.ADDRESS_INPUT)
        self.send_keys_to_element(Keys.ENTER, PathToCounters.ADDRESS_INPUT)
        self.wait_for_element(SelectedAddress.TABLE_BODY)
        return self

    def init_values(self):
        return self.click_on_element(SelectedAddress.INIT_VALUES_BUTTON)

    def get_current_value(self):
        return int(self.get_element(SelectedAddress.CURRENT_VALUE)
                   .get_attribute('data-value'))

    def get_old_value(self):
        return int(self.get_element(SelectedAddress.OLD_VALUE).text)

    def open_new_value_modal(self):
        self.click_on_element(SelectedAddress.NEW_VALUE_BUTTON)\
            .wait_for_element(NewValue.LABEL)\
            .wait_for_element(NewValue.FIELD)
        return self

    def set_new_value(self, value):
        self.send_keys_to_element(str(value), NewValue.FIELD)\
            .click_on_element(NewValue.APPLY_BUTTON)
        return self

    def change_fix_status(self):
        self.click_on_element(SelectedAddress.FIXED_BUTTON)

    def change_active_status(self):
        self.click_on_element(SelectedAddress.ACTIVATE_BUTTON)
