from functions.base_functions_zh import *
import pytest
import allure


# filename to be used in screen shot
test_file_name = os.path.basename(__file__)


def test_cisco_nexus_switch_one():
    driver.get(properties_china('health_check_url'))
    maximize_window()
    sleep(2)
    click("dashboard_card_title_ONTAP_xpath")
    click('ontap_card_ontap_deploy_toggle_button_guided_to_expert_xpath')
    sleep(1)
    element_found = find_element("ontap_deploy_expert_cisco_nexus_switch_add_xpath")
    click('ontap_deploy_expert_cisco_nexus_switch_add_xpath')
    actual_output = search_strings(properties_china('ontap_deploy_expert_cisco_nexus_switch_add_string'), element_found.text)
    expected_output = properties_china('ontap_deploy_expert_cisco_nexus_switch_add_string')
    #print("Element Returned Test:", element_found.text)
    highlight_element(element_found)
    assert actual_output == expected_output


def test_cisco_nexus_switch_two():
    element_found = find_element("ontap_deploy_expert_cisco_nexus_switch_details_xpath")
    actual_output = search_strings(properties_china('ontap_deploy_expert_cisco_nexus_switch_add_string'), element_found.text)
    expected_output = properties_china('ontap_deploy_expert_cisco_nexus_switch_add_string')
    #print("Element Returned Test: ", actual_output.text)
    highlight_element(element_found)
    capture_screenshot(test_file_name)
    assert actual_output == expected_output


# test_cisco_nexus_switch_one()
# test_cisco_nexus_switch_two()