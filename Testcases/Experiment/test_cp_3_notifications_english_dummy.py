from functions.base_functions_en import *
import pytest
import allure
from functions.ExcelFunctions import ReadWriteExcel

# Reading data from excel
data_read = ReadWriteExcel(
    "C://Users//Sumanth//PycharmProjects//PythonTesting//Resources//configurations//testdata//Test_data.xlsx")

# filename to be used in screen shot
test_file_name = os.path.basename(__file__)

# a global list that appends all the values obtained from functions (active_iq_config_advisor)
notifications_prod_titles_list = []

global actual_output, expected_output


def test_active_iq_config_advisor_one():
    driver.get(properties('health_check_url'))
    driver.maximize_window()
    sleep(2)
    click('notifications_bell_icon_xpath')
    sleep(2)

    prod_title2 = find_element('notifications_product_title2_xpath')
    prod_title3 = find_element('notifications_product_title3_xpath')
    prod_title4 = find_element('notifications_product_title4_xpath')
    prod_title5 = find_element('notifications_product_title5_xpath')

    notifications_prod_titles1 = [prod_title2, prod_title3, prod_title4, prod_title5]

    for prod_title in notifications_prod_titles1:
        highlight_element(prod_title)
        notifications_prod_titles_list.append(prod_title.text)
    capture_screenshot(test_file_name)
    return notifications_prod_titles_list


def test_active_iq_config_advisor_two():
    scroll_to_location('notifications_product_title8_CA_Bug_fixes_xpath')

    prod_title6 = find_element('notifications_product_title6_new_features_xpath')
    prod_title7 = find_element('notifications_product_title7_new_features_subheading_xpath')
    prod_title8 = find_element('notifications_product_title8_CA_Bug_fixes_xpath')
    prod_title9 = find_element('notifications_product_title9_CA_Bug_fixes_subheading_xpath')
    prod_title10 = find_element('notifications_product_title10_CA_Bug_fixes_caution_xpath')

    notifications_prod_titles2 = [prod_title6, prod_title7, prod_title8, prod_title9, prod_title10]

    for prod_title in notifications_prod_titles2:
        highlight_element(prod_title)
        notifications_prod_titles_list.append(prod_title.text)
    capture_screenshot(test_file_name)
    return notifications_prod_titles_list


# def test_active_iq_config_advisor_three():
#     sleep(2)
#     scroll_to_location('notifications_product_title11_CA_plugin_status_xpath')
#
#     prod_title11 = find_element('notifications_product_title11_CA_plugin_status_xpath')
#     prod_title12 = find_element('notifications_product_title12_CA_resource_status_xpath')
#
#     notifications_prod_titles3 = [prod_title11, prod_title12]
#
#     for prod_title in notifications_prod_titles3:
#         highlight_element(prod_title)
#         notifications_prod_titles_list.append(prod_title.text)
#     capture_screenshot(test_file_name)
#     return notifications_prod_titles_list


def test_active_iq_config_advisor_one_english():
    global actual_output, expected_output
    result = notifications_prod_titles_list
    for res in result:
        if res == properties('notifications_test_cp_3_string1'):
            expected_output = res

    colindex = 1
    row_count = data_read.get_row_count('CA_product_names')
    for row in range(1, row_count):
        if ((data_read.get_cell_value('CA_product_names', row, colindex)) == 'test_cp_3_notifications') and (
                (data_read.read_by_col_name('CA_product_names', row, 'NetApp English')) == properties('notifications_test_cp_3_string1')):
            actual_output = data_read.read_by_col_name('CA_product_names', row, 'NetApp English')
    assert actual_output == expected_output


def test_active_iq_config_advisor_two_english():
    global actual_output, expected_output
    result = notifications_prod_titles_list
    for res in result:
        if res == properties('notifications_test_cp_3_string2'):
            expected_output = res

    colindex = 1
    row_count = data_read.get_row_count('CA_product_names')
    for row in range(1, row_count):
        if ((data_read.get_cell_value('CA_product_names', row, colindex)) == 'test_cp_3_notifications') and (
                (data_read.read_by_col_name('CA_product_names', row, 'NetApp English')) == properties('notifications_test_cp_3_string2')):
            actual_output = data_read.read_by_col_name('CA_product_names', row, 'NetApp English')
    assert actual_output == expected_output


def test_active_iq_config_advisor_three_english():
    global actual_output, expected_output
    result = notifications_prod_titles_list
    for res in result:
        if res == properties('notifications_test_cp_3_string3'):
            expected_output = res

    colindex = 1
    row_count = data_read.get_row_count('CA_product_names')
    for row in range(1, row_count):
        if ((data_read.get_cell_value('CA_product_names', row, colindex)) == 'test_cp_3_notifications') and (
                (data_read.read_by_col_name('CA_product_names', row, 'NetApp English')) == properties('notifications_test_cp_3_string3')):
            actual_output = data_read.read_by_col_name('CA_product_names', row, 'NetApp English')
    assert actual_output == expected_output


def test_active_iq_config_advisor_four_english():
    global actual_output, expected_output
    result = notifications_prod_titles_list
    for res in result:
        if res == properties('notifications_test_cp_3_string4'):
            expected_output = res

    colindex = 1
    row_count = data_read.get_row_count('CA_product_names')
    for row in range(1, row_count):
        if ((data_read.get_cell_value('CA_product_names', row, colindex)) == 'test_cp_3_notifications') and (
                (data_read.read_by_col_name('CA_product_names', row, 'NetApp English')) == properties('notifications_test_cp_3_string4')):
            actual_output = data_read.read_by_col_name('CA_product_names', row, 'NetApp English')
    assert actual_output == expected_output


# def test_active_iq_config_advisor_five_english():
#     global actual_output, expected_output
#     result = notifications_prod_titles_list
#     for res in result:
#         if res == properties('notifications_test_cp_3_string5'):
#             expected_output = res
#
#     colindex = 1
#     row_count = data_read.get_row_count('CA_product_names')
#     for row in range(1, row_count):
#         if ((data_read.get_cell_value('CA_product_names', row, colindex)) == 'test_cp_3_notifications') and (
#                 (data_read.read_by_col_name('CA_product_names', row, 'NetApp English')) == properties('notifications_test_cp_3_string5')):
#             actual_output = data_read.read_by_col_name('CA_product_names', row, 'NetApp English')
#     assert actual_output == expected_output
#
#
# def test_active_iq_config_advisor_six_english():
#     global actual_output, expected_output
#     result = notifications_prod_titles_list
#     for res in result:
#         if res == properties('notifications_test_cp_3_string6'):
#             expected_output = res
#
#     colindex = 1
#     row_count = data_read.get_row_count('CA_product_names')
#     for row in range(1, row_count):
#         if ((data_read.get_cell_value('CA_product_names', row, colindex)) == 'test_cp_3_notifications') and (
#                 (data_read.read_by_col_name('CA_product_names', row, 'NetApp English')) == properties('notifications_test_cp_3_string6')):
#             actual_output = data_read.read_by_col_name('CA_product_names', row, 'NetApp English')
#     assert actual_output == expected_output
#
#
# def test_active_iq_config_advisor_seven_english():
#     global actual_output, expected_output
#     result = notifications_prod_titles_list
#     for res in result:
#         if res == properties('notifications_test_cp_3_string7'):
#             expected_output = res
#
#     colindex = 1
#     row_count = data_read.get_row_count('CA_product_names')
#     for row in range(1, row_count):
#         if ((data_read.get_cell_value('CA_product_names', row, colindex)) == 'test_cp_3_notifications') and (
#                 (data_read.read_by_col_name('CA_product_names', row, 'NetApp English')) == properties('notifications_test_cp_3_string7')):
#             actual_output = data_read.read_by_col_name('CA_product_names', row, 'NetApp English')
#     assert actual_output == expected_output
#
#
# def test_active_iq_config_advisor_eight_english():
#     global actual_output, expected_output
#     result = notifications_prod_titles_list
#     for res in result:
#         if res == properties('notifications_test_cp_3_string8'):
#             expected_output = res
#
#     colindex = 1
#     row_count = data_read.get_row_count('CA_product_names')
#     for row in range(1, row_count):
#         if ((data_read.get_cell_value('CA_product_names', row, colindex)) == 'test_cp_3_notifications') and (
#                 (data_read.read_by_col_name('CA_product_names', row, 'NetApp English')) == properties('notifications_test_cp_3_string8')):
#             actual_output = data_read.read_by_col_name('CA_product_names', row, 'NetApp English')
#     assert actual_output == expected_output
#
#
# def test_active_iq_config_advisor_nine_english():
#     global actual_output, expected_output
#     result = notifications_prod_titles_list
#     for res in result:
#         if res == properties('notifications_test_cp_3_string9'):
#             expected_output = res
#
#     colindex = 1
#     row_count = data_read.get_row_count('CA_product_names')
#     for row in range(1, row_count):
#         if ((data_read.get_cell_value('CA_product_names', row, colindex)) == 'test_cp_3_notifications') and (
#                 (data_read.read_by_col_name('CA_product_names', row, 'NetApp English')) == properties('notifications_test_cp_3_string9')):
#             actual_output = data_read.read_by_col_name('CA_product_names', row, 'NetApp English')
#     assert actual_output == expected_output
#
#
# def test_active_iq_config_advisor_ten_english():
#     global actual_output, expected_output
#     result = notifications_prod_titles_list
#     for res in result:
#         if res == properties('notifications_test_cp_3_string10'):
#             expected_output = res
#
#     colindex = 1
#     row_count = data_read.get_row_count('CA_product_names')
#     for row in range(1, row_count):
#         if ((data_read.get_cell_value('CA_product_names', row, colindex)) == 'test_cp_3_notifications') and (
#                 (data_read.read_by_col_name('CA_product_names', row, 'NetApp English')) == properties('notifications_test_cp_3_string10')):
#             actual_output = data_read.read_by_col_name('CA_product_names', row, 'NetApp English')
#     assert actual_output == expected_output
#
#
# def test_active_iq_config_advisor_eleven_english():
#     global actual_output, expected_output
#     result = notifications_prod_titles_list
#     for res in result:
#         if res == properties('notifications_test_cp_3_string11'):
#             expected_output = res
#
#     colindex = 1
#     row_count = data_read.get_row_count('CA_product_names')
#     for row in range(1, row_count):
#         if ((data_read.get_cell_value('CA_product_names', row, colindex)) == 'test_cp_3_notifications') and (
#                 (data_read.read_by_col_name('CA_product_names', row, 'NetApp English')) == properties('notifications_test_cp_3_string11')):
#             actual_output = data_read.read_by_col_name('CA_product_names', row, 'NetApp English')
#     assert actual_output == expected_output


# test_active_iq_config_advisor_one()
# test_active_iq_config_advisor_two()
# test_active_iq_config_advisor_three()