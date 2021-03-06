from functions.base_functions_zh import *
import pytest
import allure
from functions.ExcelFunctions import ReadWriteExcel

# Reading data from excel
data_read = ReadWriteExcel(
    "C://Users//Sumanth//PycharmProjects//PythonTesting//Resources//configurations//testdata//Test_data.xlsx")

# filename to be used in screen shot
test_file_name = os.path.basename(__file__)


def test_active_iq_config_advisor_settings_one():
    driver.get(properties_china('health_check_url'))
    driver.maximize_window()
    sleep(5)
    action = move_to_element('settings_gear_icon_xpath')
    action.click().perform()
    # click('settings_gear_icon_xpath')
    sleep(2)
    actual_output = find_element("settings_modal_product_title1_xpath")
    print("Element Returned Test: ", actual_output.text)
    expected_output = properties_china('settings_test_cp_3_string1')
    print(expected_output)
    print("Expected output : " + expected_output, "\nActual output : " + actual_output.text)
    assert actual_output.text == expected_output
    highlight_element(actual_output)
    capture_screenshot(test_file_name)


#test_active_iq_config_advisor_settings_one()

