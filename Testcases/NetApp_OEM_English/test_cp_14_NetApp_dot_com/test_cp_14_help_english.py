from functions.base_functions_en import *
import pytest
import allure
from functions.ExcelFunctions import ReadWriteExcel

# filename to be used in screen shot
test_file_name = os.path.basename(__file__)


def test_netapp_dot_com_one():
    driver.get(properties('health_check_url'))
    maximize_window()
    sleep(2)
    click('help_product_title_help_button_xpath')
    sleep(2)
    actual_output = find_element("help_product_title_NetApp_dot_com_xpath")
    expected_output = properties('check_point14_netapp_NetApp_dot_com_string1')
    print("Element Returned Test: ", actual_output.text)
    highlight_element(actual_output)
    capture_screenshot(test_file_name)
    assert actual_output.text == expected_output


def test_verify_netapp_dot_com_link_two():
    actual_output = get_attribute("help_product_title_NetApp_dot_com_xpath", "href")
    print("Link obtained is: ", actual_output)
    expected_output = properties('help_product_title_NetApp_dot_com_link')
    assert actual_output == expected_output
    print('Link Verified Successfully')


# test_netapp_dot_com_one()
# test_verify_netapp_dot_com_link_two()


