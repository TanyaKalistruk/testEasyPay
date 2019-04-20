from src.PageObjects.page import Page
from src.PageObjects.schedule_page import Schedule
from src.locators import HomePage, PathToCounters, PathToInspectors
from src.PageObjects.counters_page import Counters


class NavMenu(Page):

    def __init__(self, driver):
        super().__init__(driver)
        self.wait_for_element(HomePage.NAV_MENU)

    def open_inspector_page(self):
        self.click_on_element(PathToInspectors.MENU_ITEM).\
            wait_for_element(PathToInspectors.INSPECTOR)
        return Schedule(self.driver)

    def open_counters_page(self):
        self.click_on_element(PathToCounters.MENU_ITEM) \
            .wait_for_element(PathToCounters.PANEL)
        return Counters(self.driver)
