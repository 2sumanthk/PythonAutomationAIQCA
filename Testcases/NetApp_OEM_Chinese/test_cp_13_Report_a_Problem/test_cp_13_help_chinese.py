from functions.base_functions_zh import *
import pytest
import allure
from functions.ExcelFunctions import ReadWriteExcel

# filename to be used in screen shot
test_file_name = os.path.basename(__file__)


def test_report_a_problem_one():
    driver.get(properties_china('health_check_url'))
    maximize_window()
    sleep(2)
    click('help_product_title_help_button_xpath')
    sleep(2)
    actual_output = find_element("help_product_title_report_a_problem_xpath")
    highlight_element(actual_output)
    capture_screenshot(test_file_name)


def test_verify_report_a_problem_link_two():
    actual_output = get_attribute("help_product_title_report_a_problem_xpath", "href")
    print("Link obtained is: ", actual_output)
    expected_output = properties_china('help_product_title_report_a_problem_link')
    assert actual_output == expected_output
    print('Link Verified Successfully')


# test_report_a_problem_one()
# test_verify_report_a_problem_link_two()


