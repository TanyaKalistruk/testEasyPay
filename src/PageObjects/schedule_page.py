import time

from src.locators import HomePage, PathToInspectors, \
    AddScheduleItem, EditScheduleItem, DeleteScheduleItem, Navigation, Route, \
    ManagerSchedule
from src.PageObjects.page import Page
from src.Utilities.logger import logger
from src.test_data import ADDRESS_FOR_SCHEDULE


class Schedule(Page):
    log = logger()

    def __init__(self, driver):
        super().__init__(driver)
        self.wait_for_element(HomePage.DISPLAY_NAME)

    def open_inspectors_page(self):
        self.click_on_element(PathToInspectors.MENU_ITEM)\
            .wait_for_element(PathToInspectors.INSPECTOR)
        return self

    def open_schedule_page(self):
        self.click_on_element(PathToInspectors.INSPECTOR) \
            .wait_for_element(ManagerSchedule.ADD_SCHEDULE_ITEM_BUTTON)
        return self

    def open_add_schedule_item_modal(self):
        self.click_on_element(ManagerSchedule.ADD_SCHEDULE_ITEM_BUTTON) \
            .wait_for_element(AddScheduleItem.CHOOSE_DATA_EDIT)
        return self

    def choose_date_in_modal_add(self, data):
        from selenium.webdriver.common.keys import Keys
        self.wait_for_element(AddScheduleItem.CHOOSE_DATA_EDIT)\
            .click_on_element(AddScheduleItem.CHOOSE_DATA_EDIT)\
            .send_keys_to_element(8 * Keys.BACK_SPACE,
                                  AddScheduleItem.CHOOSE_DATA_EDIT)
        time.sleep(2)
        self.send_keys_to_element(data, AddScheduleItem.CHOOSE_DATA_EDIT)
        return self

    def choose_address_in_modal_add(self):
        self.click_on_element(AddScheduleItem.ADDRESS_DROPDOWN)
        self.send_keys_to_element(ADDRESS_FOR_SCHEDULE,
                                  AddScheduleItem.ADDRESS_DROPDOWN)
        self.click_on_element(AddScheduleItem.ADDRESS_CHOSEN)
        return self

    def repeat_every_month_add(self):
        self.click_on_element(AddScheduleItem.REPEAT_EVERY_MONTH_CHECKBOX)
        return self

    def warning_in_add_modal(self):
        self.is_displayed(AddScheduleItem.NO_ADDRESS_SET_WARNING)
        return self

    def add_schedule_item(self):
        self.click_on_element(AddScheduleItem.APPLY_BUTTON)
        return self

    def is_add_task_button_enabled(self):
        return self.is_button_enabled(AddScheduleItem.APPLY_BUTTON)

    def open_edit_schedule_item_modal(self):
        self.click_on_element(ManagerSchedule.EDIT_BUTTON) \
            .wait_for_element(EditScheduleItem.APPLY_BUTTON)
        return self

    def choose_date_in_modal_edit(self, data):
        from selenium.webdriver.common.keys import Keys
        self.wait_for_element(EditScheduleItem.EDIT_DATA) \
            .send_keys_to_element(8 * Keys.BACK_SPACE,
                                  EditScheduleItem.EDIT_DATA)
        self.send_keys_to_element(data, EditScheduleItem.EDIT_DATA)
        return self

    def is_element_in_schedule(self, date):
        return self.is_element_present(EditScheduleItem.IS_ELEMENT_PRESENT % date)

    def choose_address_in_modal_edit(self):
        self.click_on_element(EditScheduleItem.REMOVE_ADDRESS) \
            .click_on_element(EditScheduleItem.DROPDOWN_LIST_ADDRESSES) \
            .click_on_element(EditScheduleItem.ADDRESS_CHOSEN)
        return self

    def repeat_every_month_edit(self):
        self.click_on_element(EditScheduleItem.REPEAT_EVERY_MONTH_CHECKBOX)
        return self

    def is_displayed_warning(self):
        return self.is_displayed(EditScheduleItem.NO_ADDRESS_SET_WARNING)

    def edit_schedule_item(self):
        self.click_on_element(EditScheduleItem.APPLY_BUTTON)\
            .wait_for_element_disappear(EditScheduleItem.APPLY_BUTTON)
        return self

    def delete_schedule_item_modal(self):
        self.click_on_element(ManagerSchedule.DELETE_BUTTON)
        self.wait_for_element(DeleteScheduleItem.MODAL_WINDOW)
        return self

    def delete_schedule_item(self):
        self.click_on_element(DeleteScheduleItem.APPLY_BUTTON)\
            .wait_for_element_disappear(DeleteScheduleItem.APPLY_BUTTON)
        return self

    def schedule_route(self):
        self.click_on_element(Route.ROUTE_BUTTON)
        return self

    def navigate_to_next_month(self):
        self.click_on_element(Navigation.NEXT_MONTH)
        return self

    def navigate_to_prev_month(self):
        self.click_on_element(Navigation.PREV_MONTH)
        return self

    def navigate_today(self):
        self.click_on_element(Navigation.TODAY)
        return self

    def close_modal_add(self):
        self.click_on_element(AddScheduleItem.CLOSE)\
            .wait_for_element_disappear(AddScheduleItem.CLOSE)
        return self
