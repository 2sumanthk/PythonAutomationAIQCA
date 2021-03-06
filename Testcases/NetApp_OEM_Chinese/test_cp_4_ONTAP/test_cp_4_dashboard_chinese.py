from functions.base_functions_zh import *
import pytest
import allure
from functions.ExcelFunctions import ReadWriteExcel

# Reading data from excel
data_read = ReadWriteExcel(
    "C://Users//Sumanth//PycharmProjects//PythonTesting//Resources//configurations//testdata//Test_data.xlsx")

# filename to be used in screen shot
test_file_name = os.path.basename(__file__)


def test_ontap_dashboard_one():
    driver.get(properties_china('health_check_url'))
    maximize_window()
    sleep(2)
    actual_output = find_element("dashboard_card_title_ONTAP_xpath")
    expected_output = properties_china('check_point4_ONTAP_string')
    print("Element Returned Test: ", actual_output.text)
    highlight_element(actual_output)
    capture_screenshot(test_file_name)
    assert actual_output.text == expected_output


