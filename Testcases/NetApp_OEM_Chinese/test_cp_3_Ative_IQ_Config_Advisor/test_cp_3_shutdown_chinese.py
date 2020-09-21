from functions.base_functions_zh import *
import pytest
import allure
import pytest_check as check
from functions.ExcelFunctions import ReadWriteExcel

# Reading data from excel
data_read = ReadWriteExcel(
    "C://Users//Sumanth//PycharmProjects//PythonTesting//Resources//configurations//testdata//Test_data.xlsx")

# filename to be used in screen shot
test_file_name = os.path.basename(__file__)


def test_active_iq_config_advisor_shutdown_one():
    driver.get(properties_china('health_check_url'))
    driver.maximize_window()
    sleep(5)
    click('shutdown_power_off_button_xpath')
    sleep(2)
    actual_output = find_element("shutdown_confirm_product_title1_xpath")
    print("Element Returned Test: ", actual_output.text)
    expected_output = properties_china('shutdown_confirm_test_cp_3_string1')
    highlight_element(actual_output)
    assert actual_output.text == expected_output


def test_active_iq_config_advisor_shutdown_two():
    actual_output = find_element("shutdown_note_product_title2_xpath")
    print("Element Returned Test: ", actual_output.text)
    expected_output = properties_china('shutdown_note_test_cp_3_string2')
    highlight_element(actual_output)
    capture_screenshot(test_file_name)
    assert actual_output.text == expected_output










# test_active_iq_config_advisor_shutdown_one()
# test_active_iq_config_advisor_shutdown_two()
