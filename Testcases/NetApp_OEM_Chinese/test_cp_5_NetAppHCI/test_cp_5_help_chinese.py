from functions.base_functions_zh import *
import pytest
import allure
from functions.ExcelFunctions import ReadWriteExcel

# Reading data from excel
data_read = ReadWriteExcel(
    "C://Users//Sumanth//PycharmProjects//PythonTesting//Resources//configurations//testdata//Test_data.xlsx")

# filename to be used in screen shot
test_file_name = os.path.basename(__file__)


def test_netapp_hci_help_one():
    driver.get(properties_china('health_check_url'))
    maximize_window()
    sleep(2)
    click('help_product_title_help_button_xpath')
    sleep(2)
    click('help_product_title_whats_new_xpath')
    switch_to_window(1)  # next window tab
    actual_output = find_element("help_aiq_supported_new_features_NetAppHCI_xpath")
    expected_output = properties_china('check_point5_ONTAP_string_new_features3_change_string1')
    print("Element Returned Test: ", actual_output.text)
    highlight_element(actual_output)
    capture_screenshot(test_file_name)
    quit_browser()
    #assert actual_output.text == expected_output


test_netapp_hci_help_one()