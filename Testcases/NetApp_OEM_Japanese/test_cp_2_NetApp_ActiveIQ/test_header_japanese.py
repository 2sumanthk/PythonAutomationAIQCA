from functions.base_functions_ja import *
import pytest
import allure
from functions.ExcelFunctions import ReadWriteExcel

# Reading data from excel
data_read = ReadWriteExcel(
    "C://Users//Administrator//PycharmProjects//PythonAutomationAIQCA//Resources//configurations//testdata//Test_data.xlsx")

# filename to be used in screen shot
test_file_name = os.path.basename(__file__)


def header_one():
    redirect_urls = all_url_call()
    header1_element_set = set()
    for redirect_url in redirect_urls:
        driver.get(redirect_url)
        driver.maximize_window()
        sleep(2)
        header1_element = find_element("netapp_active_iq_name_xpath")  # NetApp Active IQ
        highlight_element(header1_element)
        capture_screenshot(test_file_name)
        sleep(1)
        header1_element_set.add(header1_element.text)
    return header1_element_set


def header_two():
    redirect_urls = all_url_call()
    header2_element_set = set()
    for redirect_url in redirect_urls:
        driver.get(redirect_url)
        driver.maximize_window()
        sleep(2)
        header2_element = find_element("netapp_configAdvisor_name_xpath")  # Config Advisor
        highlight_element(header2_element)
        capture_screenshot(test_file_name)
        sleep(1)
        header2_element_set.add(header2_element.text)
    return header2_element_set


def test_header_one_japanese():
    actual_output = list(header_one())
    colindex = 1
    if data_read.get_cell_value('CA_product_names', 2, colindex) == 'product name':
        expected_output = data_read.read_by_col_name('CA_product_names', 2, 'NetApp Japanese')
        assert expected_output == actual_output[0]


def test_header_two_japanese():
    actual_output = list(header_two())
    colindex = 1
    if data_read.get_cell_value('CA_product_names', 3, colindex) == 'product name':
        expected_output = data_read.read_by_col_name('CA_product_names', 3, 'NetApp Japanese')
        assert expected_output== actual_output[0]












    # with pytest.raises(Exception) as exception_info:
    #     result = list(header_two())
    #     colindex = 1
    #     if data_read.get_cell_value('CA_product_names', 3, colindex) == 'product name':
    #         actual_output = data_read.read_by_col_name('CA_product_names', 3, 'NetApp English')
    #         assert actual_output == result[0]
    # assert str(exception_info.value) == 'Failed with String Mismatch'