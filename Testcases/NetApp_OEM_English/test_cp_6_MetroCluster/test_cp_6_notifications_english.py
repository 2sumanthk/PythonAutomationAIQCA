from functions.base_functions_en import *
import pytest
import allure
from functions.ExcelFunctions import ReadWriteExcel



# filename to be used in screen shot
test_file_name = os.path.basename(__file__)


def test_metrocluster_notifications_one():
    driver.get(properties('health_check_url'))
    driver.maximize_window()
    sleep(2)
    click('notifications_bell_icon_xpath')
    sleep(2)
    scroll_to_location('notifications_product_title6_new_features_xpath')
    sleep(1)
    actual_output = find_element("notifications_aiq_new_features4_xpath")
    print("Element Returned Test: ", actual_output.text)
    expected_output = properties('check_point6_metro_cluster_string_new_features4_string1')
    highlight_element(actual_output)
    capture_screenshot(test_file_name)
    assert actual_output.text == expected_output


def test_metrocluster_notifications_two():
    scroll_to_location('notifications_product_title12_CA_resource_status_xpath')
    sleep(1)
    actual_output = find_element("notifications_aiq_ontap_plugin_name_metro_cluster_xpath")
    print("Element Returned Test: ", actual_output.text)
    expected_output = properties('check_point6_metro_cluster_plugin_status_string_string2')
    highlight_element(actual_output)
    capture_screenshot(test_file_name)
    assert actual_output.text == expected_output


# test_metrocluster_notifications_one()
# test_metrocluster_notifications_two()
