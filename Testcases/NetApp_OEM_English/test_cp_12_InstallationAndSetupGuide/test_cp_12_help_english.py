from functions.base_functions_en import *
import pytest
import allure
from functions.ExcelFunctions import ReadWriteExcel

# filename to be used in screen shot
test_file_name = os.path.basename(__file__)


def test_install_and_setup_guide_one():
    driver.get(properties('health_check_url'))
    maximize_window()
    sleep(2)
    click('help_product_title_help_button_xpath')
    sleep(2)
    actual_output = find_element("help_product_title_install_and_setup_guide_xpath")
    expected_output = properties('check_point12_netapp_install_and_setup_guide_string1')
    print("Element Returned Test: ", actual_output.text)
    highlight_element(actual_output)
    capture_screenshot(test_file_name)
    assert actual_output.text == expected_output


def test_verify_install_and_setup_guide_link_two():
    actual_output = get_attribute("help_product_title_install_and_setup_guide_xpath", "href")
    print("Link obtained is: ", actual_output)
    expected_output = properties('help_product_title_install_and_setup_guide_link')
    assert actual_output == expected_output
    print('Link Verified Successfully')


# test_install_and_setup_guide_one()
# test_verify_install_and_setup_guide_link_two()


