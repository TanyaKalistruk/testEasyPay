from src import test_data


class HomePage(object):
    DISPLAY_NAME = '//*[@id="display-name"]'
    NAV_MENU = '//div[@class="menu_section"]'


class PathToCounters(object):
    MENU_ITEM = '//*[@id="sidebar-menu"]/div/ul/li[2]/a'
    DROPDOWN = '//*[@class="input-group-addon dropdown-toggle"]'
    ADDRESSES_LIST = '//ul[@class="typeahead typeahead-long dropdown-menu"]'
    ADDRESS_LI = '//li[@data-value="' + test_data.ADDRESS + '"]'
    PANEL = '//div[@class="x_panel"]'
    ADDRESS_INPUT = '//input[@class="form-control combobox"]'


class SelectedAddress(object):
    TABLE = '//TABLE[@id="countersTable"]'
    TABLE_BODY = '//*[@id="countersTable"]/tbody/tr'
    UTILITY = '//*[@id="countersTable"]//td[contains(text(),"' + \
              test_data.UTILITY_NAME + '")]'
    OLD_VALUE = '//td[@class="oldValue"]'
    CURRENT_VALUE = '//td[@class="counter-value"]'
    IS_ACTIVE_TD = '//td[@class="is-active"]'
    IS_FIXED_TD = '//td[@class="is-fixed"]'
    ACTIVATE_BUTTON = '//button[@class="change-status btn btn-primary"]'
    FIXED_BUTTON = '//button[@class="change-type btn btn-primary"]'
    INIT_VALUES_BUTTON = '//button[@class="init-with-values btn btn-primary"]'
    NEW_VALUE_BUTTON = '//button[@class="btn btn-primary change-value"]'
    NOTIFY = '//div[@class="ALERT ui-pnotify-container ALERT-danger ui-pnotify-shadow"]'
    ALERT = '.alert'


class NewValue(object):
    LABEL = '//h4[@id="myModalLabel"]'
    CLOSE = '//button[@class="close"]'
    FIELD = '//input[@id="newCurrentValue"]'
    APPLY_BUTTON = '//button[@class="btn btn-primary js-apply"]'
    WRONG_VALUE_BUTTON = '//*[@id="wrong-value"]'
    CONFIRM_DIALOG = '//*[@id="confirm-dialog"]'
    CLOSE_BUTTON = '//button[@data-locale-item="close"]'


class PathToInspectors(object):
    MENU_ITEM = '//*[@id="sidebar-menu"]/div/ul/li[1]/a'
    INSPECTOR = '//*[@id="tab-inspectors"]//' \
                'a[@href="/manager/schedule/inspector/110/"]'


class Navigation(object):
    NEXT_MONTH = 'button.fc-corner-right'
    PREV_MONTH = 'button.fc-corner-left'
    TODAY = '//*[@id="manager-calendar"]/div[1]/div[1]/button'


class ManagerSchedule(object):
    DELETE_BUTTON = '//button[@data-id=%s]' % test_data.SCHEDULE_ITEM_ID
    EDIT_BUTTON = '//*[@id="manager-calendar"]/div[2]/div/TABLE/tbody/tr/td' \
                  '/div/div/div[5]/div[2]/TABLE/tbody/tr/td[5]/a/div/span'
    ADD_SCHEDULE_ITEM_BUTTON = '//*[@id="manager-calendar"]/div[1]/div[2]/button'
    SCHEDULE = '//*[@id="manager-calendar"]/div[2]'
    DELETE_DATE = '//td[@data-date="%s"]' % test_data.SCHEDULE_ITEM_DATE
    ROUTE = '//*[@id="manager-calendar"]//a[@data-date="%s"]' \
            % test_data.SCHEDULE_ITEM_DATE


class DeleteScheduleItem(object):
    APPLY_BUTTON = '//*[@id="remove-modal"]/div/div/div[3]/button[2]'
    CLOSE_BUTTON = '//*[@id="remove-modal"]/div/div/div[3]/button[1]/span'
    CLOSE = '//*[@id="remove-modal"]/div/div/div[1]/button/span'
    MODAL_WINDOW = '//*[@id="remove-modal"]/div/div/div[1]/h4'


class Route(object):
    ROUTE_BUTTON = '//*[@id="manager-calendar"]/div[2]/div/TABLE/tbody/tr/td' \
                   '/div/div/div[3]/div[2]/TABLE/thead/tr/td[4]/a'
    CLOSE = '//*[@id="map-modal"]/div/div/div[1]/button/span'


class EditScheduleItem(object):
    EDIT_DATA = '//*[@id="datetimepicker-edit"]'
    REMOVE_ADDRESS = '//*[@id="edit-schedule-item-form"]/div/div/span/span[2]'
    DROPDOWN_LIST_ADDRESSES = '//*[@id="edit-schedule-item-form"]/div/div/span'
    ADDRESS_CHOSEN = '//li[@data-value="' + test_data.EDIT_ADDRESS_FOR_SCHEDULE + '"]'
    REPEAT_EVERY_MONTH_CHECKBOX = '//*[@id="edit-schedule-item-form"]/span/small'
    CLOSE_BUTTON = '//*[@id="edit-modal"]/div/div/div[3]/button[1]/span'
    APPLY_BUTTON = '//*[@id="edit-modal"]/div/div/div[3]/button[2]/span'
    CLOSE = '//*[@id="edit-modal"]/div/div/div[1]/button/span'
    NO_ADDRESS_SET_WARNING = '//li[@class="address-error"]'
    EDIT_MODAL = '//*[@id="edit-modal"]/div/div/div[1]/h4/span'
    IS_ELEMENT_PRESENT = '//td[@data-date="%s"]//a'


class AddScheduleItem(object):
    CHOOSE_DATA_EDIT = '//*[@id="datetimepicker"]'
    DROPDOWN_LIST_ADDRESS = '//*[@id="add-schedule-item-form"]/div/div/span'
    ADDRESS_DROPDOWN = '//*[@id="add-schedule-item-form"]//input[@placeholder=' \
                       '"Select a Address"]'
    ADDRESS_CHOSEN = '//li[@data-value="' + test_data.ADDRESS_FOR_SCHEDULE + '"]'
    REPEAT_EVERY_MONTH_CHECKBOX = '//input[@id="repeat"]'
    CLOSE_BUTTON = '//*[@id="add-modal"]//button[@class="btn btn-default"]'
    APPLY_BUTTON = '//button[@class="btn btn-primary js-add-apply"]'
    CLOSE = '//*[@id="add-modal"]/div/div/div[1]/button'
    NO_ADDRESS_SET_WARNING = '//li[@class="address-error"]'
