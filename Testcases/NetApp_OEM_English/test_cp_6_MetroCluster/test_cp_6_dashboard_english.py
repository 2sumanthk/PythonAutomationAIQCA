from functions.base_functions_en import *
import pytest
import allure
from functions.ExcelFunctions import ReadWriteExcel

# Reading data from excel
data_read = ReadWriteExcel(
    "C://Users//Sumanth//PycharmProjects//PythonTesting//Resources//configurations//testdata//Test_data.xlsx")

# filename to be used in screen shot
test_file_name = os.path.basename(__file__)


def test_metrocluster_one():
    driver.get(properties('health_check_url'))
    maximize_window()
    sleep(2)
    actual_output = find_element("dashboard_card_title_metro_cluster_xpath")
    expected_output = properties('check_point6_metro_cluster_string')
    print("Element Returned Test: ", actual_output.text)
    highlight_element(actual_output)
    capture_screenshot(test_file_name)
    assert actual_output.text == expected_output


test_metrocluster_one()