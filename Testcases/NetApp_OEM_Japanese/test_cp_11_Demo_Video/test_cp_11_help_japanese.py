from functions.base_functions_ja import *
import pytest
import allure
from functions.ExcelFunctions import ReadWriteExcel

# filename to be used in screen shot
test_file_name = os.path.basename(__file__)


def test_demo_video_one():
    driver.get(properties_japan('health_check_url'))
    maximize_window()
    sleep(2)
    click('help_product_title_help_button_xpath')
    sleep(2)
    actual_output = find_element("help_product_title_demo_video_xpath")
    expected_output = properties_japan('check_point11_netapp_whats_new_string1')
    print("Element Returned Test: ", actual_output.text)
    highlight_element(actual_output)
    capture_screenshot(test_file_name)
    assert actual_output.text == expected_output


def test_verify_demo_video_link_two():
    actual_output = get_attribute("help_product_title_demo_video_xpath", "href")
    print("Link obtained is: ", actual_output)
    expected_output = properties_japan('help_product_title_demo_video_link')
    assert actual_output == expected_output
    print('Link Verified Successfully')


def test_verify_demo_video_site_title_three():
    click("help_product_title_demo_video_xpath")
    switch_to_window(1)
    actual_output = title()
    expected_output = properties_japan('verify_title_demo_video_string2')
    close_browser()
    assert actual_output == expected_output
    print('Title Verified Successfully')


# test_demo_video_one()
# test_verify_demo_video_link_two()
# test_verify_demo_video_site_title_three()
