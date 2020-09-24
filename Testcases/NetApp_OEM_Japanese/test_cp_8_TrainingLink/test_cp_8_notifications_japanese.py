from functions.base_functions_ja import *
import pytest
import allure
from functions.ExcelFunctions import ReadWriteExcel


# filename to be used in screen shot
test_file_name = os.path.basename(__file__)


def test_training_link_notifications_one():
    driver.get(properties_japan('health_check_url'))
    driver.maximize_window()
    sleep(2)
    click('notifications_bell_icon_xpath')
    sleep(5)
    actual_output = find_element("notifications_product_title4_xpath")
    print("Element Returned Text: ", actual_output.text)
    expected_output = properties_japan('check_point8_netapp_training_link_string1')
    highlight_element(actual_output)
    capture_screenshot(test_file_name)
    assert actual_output.text == expected_output


def test_verify_training_link():
    actual_output = get_attribute("notifications_product_title4_xpath", "href")
    print("Link obtained is: ", actual_output)
    expected_output = properties_japan('netapp_training_link')
    assert actual_output == expected_output
    status_code = verify_link(actual_output)
    assert status_code == 200


# test_training_link_notifications_one()
# test_verify_training_link()
