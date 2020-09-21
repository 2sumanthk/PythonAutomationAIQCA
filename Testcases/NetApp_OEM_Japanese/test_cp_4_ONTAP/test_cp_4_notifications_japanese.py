from functions.base_functions_ja import *
import pytest
import allure
from functions.ExcelFunctions import ReadWriteExcel

# Reading data from excel
data_read = ReadWriteExcel(
    "C://Users//Sumanth//PycharmProjects//PythonTesting//Resources//configurations//testdata//Test_data.xlsx")

# filename to be used in screen shot
test_file_name = os.path.basename(__file__)


def test_ontap_notifications_one():
    driver.get(properties_japan('health_check_url'))
    driver.maximize_window()
    sleep(2)
    click('notifications_bell_icon_xpath')
    sleep(2)
    scroll_to_location('notifications_product_title6_new_features_xpath')
    actual_output = find_element("notifications_aiq_new_features1_xpath")
    expected_output = properties_japan('check_point4_ONTAP_string_new_features1_string1')
    print("Element Returned Test: ", actual_output.text)
    highlight_element(actual_output)
    assert actual_output.text == expected_output


def test_ontap_notifications_two():
    actual_output = find_element("notifications_aiq_new_features2_xpath")
    expected_output = properties_japan('check_point4_ONTAP_string_new_features2_string2')
    print("Element Returned Test: ", actual_output.text)
    highlight_element(actual_output)
    capture_screenshot(test_file_name)
    assert actual_output.text == expected_output


def test_ontap_notifications_three():
    scroll_to_location('notifications_aiq_ontap_plugin_status_xpath')
    actual_output = find_element("notifications_aiq_ontap_plugin_status_xpath")
    expected_output = properties_japan('check_point4_ONTAP_string')
    print("Element Returned Test: ", actual_output.text)
    highlight_element(actual_output)
    capture_screenshot(test_file_name)
    assert actual_output.text == expected_output


# test_ontap_notifications_one()
# test_ontap_notifications_two()
# test_ontap_notifications_three()