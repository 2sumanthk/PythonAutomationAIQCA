from functions.base_functions_ja import *
import pytest
import allure
from functions.ExcelFunctions import ReadWriteExcel

# Reading data from excel
data_read = ReadWriteExcel(
    "C://Users//Sumanth//PycharmProjects//PythonTesting//Resources//configurations//testdata//Test_data.xlsx")

# filename to be used in screen shot
test_file_name = os.path.basename(__file__)


def test_active_iq_config_advisor_one():
    driver.get(properties_japan('health_check_url'))
    driver.maximize_window()
    sleep(2)
    click('notifications_bell_icon_xpath')
    sleep(2)

    actual_output = find_element("notifications_product_title2_xpath")
    print("Element Returned Test: ", actual_output.text)
    colindex = 1
    row_count = data_read.get_row_count('CA_product_names')+1
    for row in range(1, row_count):
        if ((data_read.get_cell_value('CA_product_names', row, colindex)) == 'test_cp_3_notifications') and ((data_read.read_by_col_name('CA_product_names', row, 'NetApp Japanese')) == properties_japan('notifications_test_cp_3_string1')):
            expected_output = data_read.read_by_col_name('CA_product_names', row, 'NetApp Japanese')
            print("Expected output : " + expected_output, "\nActual output : " + actual_output.text)
            print("________________________________________________")
            assert actual_output.text == expected_output
    highlight_element(actual_output)


def test_active_iq_config_advisor_two():
    actual_output = find_element('notifications_product_title3_xpath')
    print("Element Returned Test: ", actual_output.text)
    colindex = 1
    row_count = data_read.get_row_count('CA_product_names') + 1
    for row in range(1, row_count):
        if ((data_read.get_cell_value('CA_product_names', row, colindex)) == 'test_cp_3_notifications') and (
                (data_read.read_by_col_name('CA_product_names', row, 'NetApp Japanese')) == properties_japan(
                'notifications_test_cp_3_string2')):
            expected_output = data_read.read_by_col_name('CA_product_names', row, 'NetApp Japanese')
            print("Expected output : " + expected_output, "\nActual output : " + actual_output.text)
            print("________________________________________________")
            assert actual_output.text == expected_output
    highlight_element(actual_output)


def test_active_iq_config_advisor_three():
    actual_output = find_element('notifications_product_title4_xpath')
    print("Element Returned Test: ", actual_output.text)
    colindex = 1
    row_count = data_read.get_row_count('CA_product_names') + 1
    for row in range(1, row_count):
        if ((data_read.get_cell_value('CA_product_names', row, colindex)) == 'test_cp_3_notifications') and (
                (data_read.read_by_col_name('CA_product_names', row, 'NetApp Japanese')) == properties_japan(
                'notifications_test_cp_3_string3')):
            expected_output = data_read.read_by_col_name('CA_product_names', row, 'NetApp Japanese')
            print("Expected output : " + expected_output, "\nActual output : " + actual_output.text)
            print("________________________________________________")
            assert actual_output.text == expected_output
    highlight_element(actual_output)


def test_active_iq_config_advisor_four():
    actual_output = find_element('notifications_product_title5_xpath')
    print("Element Returned Test: ", actual_output.text)
    colindex = 1
    row_count = data_read.get_row_count('CA_product_names') + 1
    for row in range(1, row_count):
        if ((data_read.get_cell_value('CA_product_names', row, colindex)) == 'test_cp_3_notifications') and (
                (data_read.read_by_col_name('CA_product_names', row, 'NetApp Japanese')) == properties_japan(
                'notifications_test_cp_3_string4')):
            expected_output = data_read.read_by_col_name('CA_product_names', row, 'NetApp Japanese')
            print("Expected output : " + expected_output, "\nActual output : " + actual_output.text)
            print("________________________________________________")
            assert actual_output.text == expected_output
    highlight_element(actual_output)
    capture_screenshot(test_file_name)
    scroll_to_location('notifications_product_title8_CA_Bug_fixes_xpath')


def test_active_iq_config_advisor_five():
    actual_output = find_element('notifications_product_title6_new_features_xpath')
    print("Element Returned Test: ", actual_output.text)
    colindex = 1
    row_count = data_read.get_row_count('CA_product_names') + 1
    for row in range(1, row_count):
        if ((data_read.get_cell_value('CA_product_names', row, colindex)) == 'test_cp_3_notifications') and (
                (data_read.read_by_col_name('CA_product_names', row, 'NetApp Japanese')) == properties_japan(
                'notifications_test_cp_3_string5')):
            expected_output = data_read.read_by_col_name('CA_product_names', row, 'NetApp Japanese')
            print("Expected output : " + expected_output, "\nActual output : " + actual_output.text)
            print("________________________________________________")
            assert actual_output.text == expected_output
    highlight_element(actual_output)


def test_active_iq_config_advisor_six():
    actual_output = find_element('notifications_product_title7_new_features_subheading_xpath')
    print("Element Returned Test: ", actual_output.text)
    colindex = 1
    row_count = data_read.get_row_count('CA_product_names') + 1
    for row in range(1, row_count):
        if ((data_read.get_cell_value('CA_product_names', row, colindex)) == 'test_cp_3_notifications') and (
                (data_read.read_by_col_name('CA_product_names', row, 'NetApp Japanese')) == properties_japan(
                'notifications_test_cp_3_string6')):
            expected_output = data_read.read_by_col_name('CA_product_names', row, 'NetApp Japanese')
            print("Expected output : " + expected_output, "\nActual output : " + actual_output.text)
            print("________________________________________________")
            assert actual_output.text == expected_output
    highlight_element(actual_output)


def test_active_iq_config_advisor_seven():
    actual_output = find_element('notifications_product_title8_CA_Bug_fixes_xpath')
    print("Element Returned Test: ", actual_output.text)
    colindex = 1
    row_count = data_read.get_row_count('CA_product_names') + 1
    for row in range(1, row_count):
        if ((data_read.get_cell_value('CA_product_names', row, colindex)) == 'test_cp_3_notifications') and (
                (data_read.read_by_col_name('CA_product_names', row, 'NetApp Japanese')) == properties_japan(
                'notifications_test_cp_3_string7')):
            expected_output = data_read.read_by_col_name('CA_product_names', row, 'NetApp Japanese')
            print("Expected output : " + expected_output, "\nActual output : " + actual_output.text)
            print("________________________________________________")
            assert actual_output.text == expected_output
    highlight_element(actual_output)


def test_active_iq_config_advisor_eight():
    actual_output = find_element('notifications_product_title9_CA_Bug_fixes_subheading_xpath')
    print("Element Returned Test: ", actual_output.text)
    colindex = 1
    row_count = data_read.get_row_count('CA_product_names') + 1
    for row in range(1, row_count):
        if ((data_read.get_cell_value('CA_product_names', row, colindex)) == 'test_cp_3_notifications') and (
                (data_read.read_by_col_name('CA_product_names', row, 'NetApp Japanese')) == properties_japan(
                'notifications_test_cp_3_string8')):
            expected_output = data_read.read_by_col_name('CA_product_names', row, 'NetApp Japanese')
            print("Expected output : " + expected_output, "\nActual output : " + actual_output.text)
            print("________________________________________________")
            assert actual_output.text == expected_output
    highlight_element(actual_output)


def test_active_iq_config_advisor_nine():
    actual_output = find_element('notifications_product_title10_CA_Bug_fixes_caution_xpath')
    print("Element Returned Test: ", actual_output.text)
    colindex = 1
    row_count = data_read.get_row_count('CA_product_names') + 1
    for row in range(1, row_count):
        if ((data_read.get_cell_value('CA_product_names', row, colindex)) == 'test_cp_3_notifications') and (
                (data_read.read_by_col_name('CA_product_names', row, 'NetApp Japanese')) == properties_japan(
                'notifications_test_cp_3_string9')):
            expected_output = data_read.read_by_col_name('CA_product_names', row, 'NetApp Japanese')
            print("Expected output : " + expected_output, "\nActual output : " + actual_output.text)
            print("________________________________________________")
            assert actual_output.text == expected_output
    highlight_element(actual_output)
    capture_screenshot(test_file_name)
    scroll_to_location('notifications_product_title12_CA_resource_status_xpath')


def test_active_iq_config_advisor_ten():
    actual_output = find_element('notifications_product_title11_CA_plugin_status_xpath')
    print("Element Returned Test: ", actual_output.text)
    colindex = 1
    row_count = data_read.get_row_count('CA_product_names') + 1
    for row in range(1, row_count):
        if ((data_read.get_cell_value('CA_product_names', row, colindex)) == 'test_cp_3_notifications') and (
                (data_read.read_by_col_name('CA_product_names', row, 'NetApp Japanese')) == properties_japan(
                'notifications_test_cp_3_string10')):
            expected_output = data_read.read_by_col_name('CA_product_names', row, 'NetApp Japanese')
            print("Expected output : " + expected_output, "\nActual output : " + actual_output.text)
            print("________________________________________________")
            assert actual_output.text == expected_output
    highlight_element(actual_output)


def test_active_iq_config_advisor_eleven():
    actual_output = find_element('notifications_product_title12_CA_resource_status_xpath')
    print("Element Returned Test: ", actual_output.text)
    colindex = 1
    row_count = data_read.get_row_count('CA_product_names') + 1
    for row in range(1, row_count):
        if ((data_read.get_cell_value('CA_product_names', row, colindex)) == 'test_cp_3_notifications') and (
                (data_read.read_by_col_name('CA_product_names', row, 'NetApp Japanese')) == properties_japan(
                'notifications_test_cp_3_string11')):
            expected_output = data_read.read_by_col_name('CA_product_names', row, 'NetApp Japanese')
            print("Expected output : " + expected_output, "\nActual output : " + actual_output.text)
            print("________________________________________________")
            assert actual_output.text == expected_output
    highlight_element(actual_output)
    capture_screenshot(test_file_name)


test_active_iq_config_advisor_one()
test_active_iq_config_advisor_two()
test_active_iq_config_advisor_three()
test_active_iq_config_advisor_four()
test_active_iq_config_advisor_five()
test_active_iq_config_advisor_six()
test_active_iq_config_advisor_seven()
test_active_iq_config_advisor_eight()
test_active_iq_config_advisor_nine()
test_active_iq_config_advisor_ten()
test_active_iq_config_advisor_eleven()

