from functions.base_functions_en import *
import pytest
import allure
from functions.ExcelFunctions import ReadWriteExcel

# Reading data from excel
data_read = ReadWriteExcel(
    "C://Users//Sumanth//PycharmProjects//PythonTesting//Resources//configurations//testdata//Test_data.xlsx")

# filename to be used in screen shot
test_file_name = os.path.basename(__file__)


def test_active_iq_config_advisor_one():
    driver.get(properties('health_check_url'))
    driver.maximize_window()
    sleep(2)
    click('notifications_bell_icon_xpath')
    sleep(2)
    actual_output = find_element("notifications_product_title2_xpath")
    print("Element Returned Test: ", actual_output.text)
    expected_output = properties('notifications_test_cp_3_string1')
    highlight_element(actual_output)
    assert actual_output.text == expected_output


def test_active_iq_config_advisor_two():
    actual_output = find_element('notifications_product_title3_xpath')
    print("Element Returned Test: ", actual_output.text)
    expected_output = properties('notifications_test_cp_3_string2')
    highlight_element(actual_output)
    assert actual_output.text == expected_output


def test_active_iq_config_advisor_three():
    actual_output = find_element('notifications_product_title4_xpath')
    print("Element Returned Test: ", actual_output.text)
    expected_output = properties('notifications_test_cp_3_string3')
    highlight_element(actual_output)
    assert actual_output.text == expected_output


def test_active_iq_config_advisor_four():
    actual_output = find_element('notifications_product_title5_xpath')
    print("Element Returned Test: ", actual_output.text)
    expected_output = properties( 'notifications_test_cp_3_string4')
    highlight_element(actual_output)
    capture_screenshot(test_file_name)
    assert actual_output.text == expected_output


def test_active_iq_config_advisor_five():
    scroll_to_location('notifications_product_title8_CA_Bug_fixes_xpath')
    actual_output = find_element('notifications_product_title6_new_features_xpath')
    print("Element Returned Test: ", actual_output.text)
    expected_output = properties('notifications_test_cp_3_string5')
    highlight_element(actual_output)
    capture_screenshot(test_file_name)
    assert actual_output.text == expected_output


def test_active_iq_config_advisor_six():
    actual_output = find_element('notifications_product_title7_new_features_subheading_xpath')
    print("Element Returned Test: ", actual_output.text)
    expected_output = properties('notifications_test_cp_3_string6')
    highlight_element(actual_output)
    assert actual_output.text == expected_output


def test_active_iq_config_advisor_seven():
    actual_output = find_element('notifications_product_title8_CA_Bug_fixes_xpath')
    print("Element Returned Test: ", actual_output.text)
    expected_output = properties('notifications_test_cp_3_string7')
    highlight_element(actual_output)
    assert actual_output.text == expected_output


def test_active_iq_config_advisor_eight():
    actual_output = find_element('notifications_product_title9_CA_Bug_fixes_subheading_xpath')
    print("Element Returned Test: ", actual_output.text)
    expected_output = properties('notifications_test_cp_3_string8')
    highlight_element(actual_output)
    assert actual_output.text == expected_output


def test_active_iq_config_advisor_nine():
    actual_output = find_element('notifications_product_title10_CA_Bug_fixes_caution_xpath')
    print("Element Returned Test: ", actual_output.text)
    expected_output = properties('notifications_test_cp_3_string9')
    highlight_element(actual_output)
    capture_screenshot(test_file_name)
    assert actual_output.text == expected_output


def test_active_iq_config_advisor_ten():
    scroll_to_location('notifications_product_title12_CA_resource_status_xpath')
    actual_output = find_element('notifications_product_title11_CA_plugin_status_xpath')
    print("Element Returned Test: ", actual_output.text)
    expected_output = properties('notifications_test_cp_3_string10')
    highlight_element(actual_output)
    assert actual_output.text == expected_output


def test_active_iq_config_advisor_eleven():
    actual_output = find_element('notifications_product_title12_CA_resource_status_xpath')
    print("Element Returned Test: ", actual_output.text)
    expected_output = properties('notifications_test_cp_3_string11')
    highlight_element(actual_output)
    capture_screenshot(test_file_name)
    assert actual_output.text == expected_output


# test_active_iq_config_advisor_one()
# test_active_iq_config_advisor_two()
# test_active_iq_config_advisor_three()
# test_active_iq_config_advisor_four()
# test_active_iq_config_advisor_five()
# test_active_iq_config_advisor_six()
# test_active_iq_config_advisor_seven()
# test_active_iq_config_advisor_eight()
# test_active_iq_config_advisor_nine()
# test_active_iq_config_advisor_ten()
# test_active_iq_config_advisor_eleven()

