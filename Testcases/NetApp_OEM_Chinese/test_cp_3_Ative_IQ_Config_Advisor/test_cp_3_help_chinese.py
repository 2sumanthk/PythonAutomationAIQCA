from functions.base_functions_zh import *
import pytest
import allure
from functions.ExcelFunctions import ReadWriteExcel

# filename to be used in screen shot
test_file_name = os.path.basename(__file__)


def test_active_iq_config_advisor_help_one():
    driver.get(properties_china('health_check_url'))
    maximize_window()
    sleep(2)
    click('help_product_title_help_button_xpath')
    sleep(2)
    click('help_product_title_whats_new_xpath')
    switch_to_window(1)  # next window tab
    actual_output = find_element("help_product_title1_whats_new_new_tab_xpath")
    expected_output = properties_china('help_whats_new_new_tab_test_cp_3_string1')
    print("Element Returned Test: ", actual_output.text)
    assert actual_output.text == expected_output
    highlight_element(actual_output)


def test_active_iq_config_advisor_help_two():
    actual_output = find_element("help_product_title2_support_for_new_features_xpath")
    print("Element Returned Test: ", actual_output.text)
    expected_output = properties_china('help_support_for_new_features_test_cp_3_string2')
    assert actual_output.text == expected_output
    highlight_element(actual_output)


def test_active_iq_config_advisor_help_three():
    actual_output = find_element("help_product_title2_key_issues_addressed_xpath")
    print("Element Returned Test: ", actual_output.text)
    expected_output = properties_china('help_key_issues_addressed_test_cp_3_string3')
    assert actual_output.text == expected_output
    highlight_element(actual_output)
    capture_screenshot(test_file_name)
    sleep(2)
    switch_to_window(0)  # default window


# test_active_iq_config_advisor_help_one()
# test_active_iq_config_advisor_help_two()
# test_active_iq_config_advisor_help_three()