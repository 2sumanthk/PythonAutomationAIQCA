from functions.base_functions_en import *
import pytest
import allure


# filename to be used in screen shot
test_file_name = os.path.basename(__file__)


def test_cisco_nexus_switch_one():
    driver.get(properties('health_check_url'))
    maximize_window()
    sleep(2)
    click("dashboard_card_title_ONTAP_xpath")
    click('ontap_card_ontap_deploy_toggle_button_guided_to_expert_xpath')
    sleep(1)
    actual_output = find_element("ontap_deploy_expert_cisco_nexus_switch_add_xpath")
    click('ontap_deploy_expert_cisco_nexus_switch_add_xpath')
    expected_output = properties('ontap_deploy_expert_cisco_nexus_switch_add_string')
    print("Element Returned Test:", actual_output.text)
    highlight_element(actual_output)
    assert actual_output.text == expected_output


def test_cisco_nexus_switch_two():
    actual_output = find_element("ontap_deploy_expert_cisco_nexus_switch_details_xpath")
    expected_output = properties('check_point4_cisco_nexus_switch_string')
    print("Element Returned Test: ", actual_output.text)
    highlight_element(actual_output)
    capture_screenshot(test_file_name)
    assert actual_output.text == expected_output


# test_cisco_nexus_switch_one()
# test_cisco_nexus_switch_two()