from functions.base_functions_en import *
import pytest
import allure
from functions.ExcelFunctions import ReadWriteExcel

# filename to be used in screen shot
test_file_name = os.path.basename(__file__)


def test_ontap_deploy_guided_modal_number_one():
    driver.get(properties('health_check_url'))
    maximize_window()
    sleep(2)
    click("dashboard_card_title_ONTAP_xpath")
    type_in("ONTAP_post_deployment_guided_Hostname_xpath", properties("ONTAP_post_deployment_guided_Hostname"))
    type_in("ONTAP_post_deployment_guided_password_xpath", properties("ONTAP_post_deployment_guided_password"))
    click("ONTAP_post_deployment_guided_form_validate_xpath")
    sleep(20)
    found_element = find_element("ONTAP_post_deployment_guided_modal_number_xpath")
    actual_output = search_strings(properties("ONTAP_post_deployment_guided_modal_number_details"), found_element.text)
    expected_output = properties('ONTAP_post_deployment_guided_modal_number_details')
    print("Element Returned Test: ", found_element.text)
    highlight_element(found_element)
    assert actual_output == expected_output


def test_ontap_deploy_os_version_two():
    found_element = find_element("ONTAP_post_deployment_guided_os_version_xpath")
    actual_output = search_strings(properties("ONTAP_post_deployment_guided_os_version_details"), found_element.text)
    expected_output = properties('ONTAP_post_deployment_guided_os_version_details')
    print("Element Returned Test: ", found_element.text)
    highlight_element(found_element)
    capture_screenshot(test_file_name)
    assert actual_output == expected_output


# test_ontap_deploy_guided_modal_number_one()
# test_ontap_deploy_os_version_two()