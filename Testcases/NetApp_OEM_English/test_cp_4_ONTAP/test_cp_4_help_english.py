from functions.base_functions_en import *
import pytest
import allure
from functions.ExcelFunctions import ReadWriteExcel


# filename to be used in screen shot
test_file_name = os.path.basename(__file__)


def test_ontap_help_one():
    driver.get(properties('health_check_url'))
    maximize_window()
    sleep(2)
    click('help_product_title_help_button_xpath')
    sleep(2)
    click('help_product_title_whats_new_xpath')
    switch_to_window(1)  # next window tab
    actual_output = find_element("help_aiq_supported_new_features_xpath")
    expected_output = properties('help_aiq_supported_new_features_string1')
    print("Element Returned Test: ", actual_output.text)
    highlight_element(actual_output)
    assert actual_output.text == expected_output


def test_ontap_help_two():
    actual_output = find_element("help_aiq_issues_addressed_new_features_xpath")
    expected_output = properties('help_aiq_issues_addressed_new_features_string2')
    print("Element Returned Test: ", actual_output.text)
    highlight_element(actual_output)
    capture_screenshot(test_file_name)
    sleep(1)
    assert actual_output.text == expected_output
    switch_to_window(0)


# test_ontap_help_one()
# test_ontap_help_two()