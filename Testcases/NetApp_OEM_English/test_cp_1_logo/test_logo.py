from functions.base_functions_en import *
import pytest
from functions.ExcelFunctions import ReadWriteExcel

# Reading data from excel
data_read = ReadWriteExcel("C://Users//Administrator//PycharmProjects//PythonAutomationAIQCA//Resources//configurations//testdata//Test_data.xlsx")

# filename to be used in screen shot
test_file_name = os.path.basename(__file__)


def test_logo():
    redirect_urls = all_url_call()
    img_element_set = set()
    for redirect_url in redirect_urls:
        driver.get(redirect_url)
        driver.maximize_window()
        time.sleep(2)
        image_element = find_element("netapp_logo_xpath")  # NetApp logo
        highlight_element(image_element)
        capture_screenshot(test_file_name)
        img_element_set.add(image_element)
    return img_element_set

