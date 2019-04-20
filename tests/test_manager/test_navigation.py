import allure

from src.locators import Navigation


def test_next_prev_month(get_inspector_schedule_from_manager):
    schedule = get_inspector_schedule_from_manager
    with allure.step("Verify button next month is enabled"):
        assert schedule.is_button_enabled(Navigation.NEXT_MONTH, 'css')
    with allure.step("Verify button previous month is not enabled"):
        assert not schedule.is_button_enabled(Navigation.PREV_MONTH, 'css')
    schedule.click_on_element(Navigation.NEXT_MONTH, 'css')
    with allure.step("Verify button next month is not enabled"):
        assert not schedule.is_button_enabled(Navigation.NEXT_MONTH, 'css')
    with allure.step("Verify button previous month is enabled"):
        assert schedule.is_button_enabled(Navigation.PREV_MONTH, 'css')
    schedule.click_on_element(Navigation.PREV_MONTH, 'css')


def test_navigate_today(get_inspector_schedule_from_manager):
    schedule = get_inspector_schedule_from_manager
    with allure.step("Verify button today is not enabled for current month"):
        assert not schedule.is_button_enabled(Navigation.TODAY)
    schedule.click_on_element(Navigation.NEXT_MONTH, 'css')
    with allure.step("Verify button today is enabled"):
        assert schedule.is_button_enabled(Navigation.TODAY)
