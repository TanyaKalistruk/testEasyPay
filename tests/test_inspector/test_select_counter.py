import allure

from src.locators import PathToCounters, SelectedAddress


''' Verify that the list of clients addresses assigned
 to the inspector is available.'''


def test_addresses_available(inspector_setup):
    counters = inspector_setup
    counters.open_counters_page() \
        .expand_counters_dropdown()
    with allure.step("Addresses list displayed"):
        assert counters.is_displayed(PathToCounters.ADDRESSES_LIST), \
            "Addresses list not displayed"


def test_select_counter(inspector_counter):
    counters = inspector_counter
    with allure.step("Counter info displayed"):
        assert counters.is_displayed(SelectedAddress.UTILITY), \
            "Utility not displayed"
        assert counters.is_displayed(SelectedAddress.OLD_VALUE), \
            "Old value not displayed"
        assert counters.is_displayed(SelectedAddress.CURRENT_VALUE), \
            "Current value not displayed"
        assert counters.is_displayed(SelectedAddress.ACTIVATE_BUTTON), \
            "Activate/deactivate button not displayed"
        assert counters.is_displayed(SelectedAddress.FIXED_BUTTON), \
            "Fix/unfix button not displayed"
        assert counters.is_displayed(SelectedAddress.INIT_VALUES_BUTTON), \
            "Init values button not displayed"
        assert counters.is_displayed(SelectedAddress.NEW_VALUE_BUTTON), \
            "New value button not displayed"
