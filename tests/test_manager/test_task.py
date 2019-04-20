import allure

from src.locators import AddScheduleItem
from src.test_data import SCHEDULE_ITEM_DATE


def test_add_task_without_address(get_inspector_schedule_from_manager):
    schedule = get_inspector_schedule_from_manager
    schedule.open_add_schedule_item_modal()
    with allure.step("Verify apply button is enabled"):
        assert schedule.is_button_enabled(AddScheduleItem.APPLY_BUTTON), \
            "Button disabled"
    schedule.add_schedule_item()\
        .wait_for_element(AddScheduleItem.NO_ADDRESS_SET_WARNING)
    with allure.step("Verify there is warning message in case no address"):
        assert schedule.warning_in_add_modal(), "No warning message"
    schedule.close_modal_add()


def test_add_task(get_inspector_schedule_from_manager):
    schedule = get_inspector_schedule_from_manager
    schedule.open_add_schedule_item_modal()\
        .choose_address_in_modal_add()
    schedule.choose_date_in_modal_add(SCHEDULE_ITEM_DATE)
    with allure.step("Verify apply button is enabled"):
        assert schedule.is_add_task_button_enabled(), "Button is disabled"
    schedule.add_schedule_item()\
        .wait_for_element_disappear(AddScheduleItem.APPLY_BUTTON)
    with allure.step("Verify that task was added"):
        assert schedule.is_element_in_schedule(SCHEDULE_ITEM_DATE), \
            "Task wasn't added"


def test_address_deletion(schedule_one_new_value_setup,
                          get_inspector_schedule_from_manager):
    schedule = get_inspector_schedule_from_manager\
        .delete_schedule_item_modal()\
        .delete_schedule_item()
    with allure.step("Verify there is no task on that day"):
        assert not schedule.is_element_in_schedule(SCHEDULE_ITEM_DATE)
