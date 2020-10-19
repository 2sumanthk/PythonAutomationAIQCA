from functions.base_functions_ja import *
import pytest
import allure


# filename to be used in screen shot
test_file_name = os.path.basename(__file__)


def test_netapp_switch_one():
    driver.get(properties_japan('health_check_url'))
    maximize_window()
    sleep(2)
    click("dashboard_card_title_ONTAP_xpath")
    click('ontap_card_ontap_deploy_toggle_button_guided_to_expert_xpath')
    sleep(1)
    element_found = find_element("ontap_deploy_expert_netapp_switch_add_xpath")
    click('ontap_deploy_expert_netapp_switch_add_xpath')
    actual_output = search_strings(properties_japan('check_point17_netapp_switch_string'), element_found.text)
    expected_output = properties_japan('check_point17_netapp_switch_string')
    print("Element Returned Test:", element_found.text)
    highlight_element(element_found)
    assert actual_output == expected_output


def test_netapp_switch_two():
    element_found = find_element("ontap_deploy_expert_netapp_switch_details_xpath")
    actual_output = search_strings(properties_japan('check_point17_netapp_switch_string'), element_found.text)
    expected_output = properties_japan('check_point17_netapp_switch_string')
    print("Element Returned Test: ", element_found.text)
    highlight_element(element_found)
    capture_screenshot(test_file_name)
    assert actual_output == expected_output


# test_netapp_switch_one()
# test_netapp_switch_two()