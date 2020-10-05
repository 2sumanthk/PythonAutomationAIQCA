from functions.base_functions_en import *
import pytest
import allure
from functions.ExcelFunctions import ReadWriteExcel



# filename to be used in screen shot
test_file_name = os.path.basename(__file__)


def test_active_iq_config_advisor_shutdown_one():
    driver.get(properties('health_check_url'))
    driver.maximize_window()
    sleep(5)
    click('shutdown_power_off_button_xpath')
    sleep(2)
    actual_output = find_element("shutdown_confirm_product_title1_xpath")
    print("Element Returned Test: ", actual_output.text)
    expected_output = properties('shutdown_confirm_test_cp_3_string1')
    highlight_element(actual_output)
    assert actual_output.text == expected_output


def test_active_iq_config_advisor_shutdown_two():
    actual_output = find_element("shutdown_note_product_title2_xpath")
    print("Element Returned Test: ", actual_output.text)
    expected_output = properties('shutdown_note_test_cp_3_string2')
    highlight_element(actual_output)
    capture_screenshot(test_file_name)
    assert actual_output.text == expected_output


# test_active_iq_config_advisor_shutdown_one()
# test_active_iq_config_advisor_shutdown_two()
