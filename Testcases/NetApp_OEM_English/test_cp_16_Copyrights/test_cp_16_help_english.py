from functions.base_functions_en import *
import pytest
import allure
from functions.ExcelFunctions import ReadWriteExcel

# filename to be used in screen shot
test_file_name = os.path.basename(__file__)


def test_copyrights_one():
    driver.get(properties('health_check_url'))
    maximize_window()
    sleep(2)
    click('help_product_title_help_button_xpath')
    sleep(2)
    click('help_product_title_whats_new_xpath')
    switch_to_window(1)  # next window tab
    found_element = find_element("help_product_copyrights_xpath")
    expected_output = properties('help_product_copyrights_string1')
    print("Element Returned Test: ", found_element.text)
    actual_output = search_strings(properties("help_product_copyrights_string1"), found_element.text)
    highlight_element(found_element)
    capture_screenshot(test_file_name)
    assert actual_output == expected_output


def test_copyrights_two():
    found_element = find_element("help_product_copyrights_xpath")
    expected_output = properties('help_product_copyrights_string2')
    print("Element Returned Test: ", found_element.text)
    actual_output = search_strings(properties("help_product_copyrights_string2"), found_element.text)
    assert actual_output == expected_output
    close_browser()
    switch_to_window(0)


# test_copyrights_one()
# test_copyrights_two()


