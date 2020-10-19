from functions.base_functions_zh import *
import pytest
import allure
from functions.ExcelFunctions import ReadWriteExcel


# filename to be used in screen shot
test_file_name = os.path.basename(__file__)


def test_active_iq_config_advisor_settings_one():
    driver.get(properties_china('health_check_url'))
    driver.maximize_window()
    sleep(5)
    action = move_to_element('settings_gear_icon_xpath')
    action.click().perform()
    sleep(2)
    element = find_element("settings_modal_product_title1_xpath")
    print("Element Returned Test: ", element.text.encode('utf-8'))
    actual_output = search_strings(properties_china('settings_test_cp_3_string1'), element.text)
    print("checkpoint captured:", actual_output)
    expected_output = properties_china('settings_test_cp_3_string1')
    highlight_element(element)
    capture_screenshot(test_file_name)
    assert actual_output == expected_output


# test_active_iq_config_advisor_settings_one()

