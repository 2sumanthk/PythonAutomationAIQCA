from functions.base_functions_en import *
import pytest
import allure
from functions.ExcelFunctions import ReadWriteExcel

# Reading data from excel
data_read = ReadWriteExcel("C://Users//Administrator//PycharmProjects//PythonAutomationAIQCA//Resources//configurations//testdata//Test_data.xlsx")

# filename to be used in screen shot
test_file_name = os.path.basename(__file__)


def product_name():
    redirect_urls = all_url_call()
    for redirect_url in redirect_urls:
        if redirect_url == properties('health_check_url'):
            driver.get(redirect_url)
            driver.maximize_window()
            time.sleep(2)
            click('notifications_bell_icon_xpath')
            time.sleep(2)

            prod_title2 = find_element('notifications_product_title2_xpath')
            prod_title3 = find_element('notifications_product_title3_xpath')
            prod_title4 = find_element('notifications_product_title4_xpath')
            prod_title5 = find_element('notifications_product_title5_xpath')

            notifications_prod_titles1 = [prod_title2, prod_title3, prod_title4, prod_title5]

            for prod_title in notifications_prod_titles1:
                highlight_element(prod_title)
            capture_screenshot(test_file_name)

            scroll_to_location('notifications_product_title8_CA_Bug_fixes_xpath')

            prod_title6 = find_element('notifications_product_title6_new_features_xpath')
            prod_title7 = find_element('notifications_product_title7_new_features_subheading_xpath')
            prod_title8 = find_element('notifications_product_title8_CA_Bug_fixes_xpath')
            prod_title9 = find_element('notifications_product_title9_CA_Bug_fixes_subheading_xpath')
            prod_title10 = find_element('notifications_product_title10_CA_Bug_fixes_caution_xpath')

            notifications_prod_titles2 = [prod_title6, prod_title7, prod_title8, prod_title9, prod_title10]

            for prod_title in notifications_prod_titles2:
                highlight_element(prod_title)
            capture_screenshot(test_file_name)

            scroll_to_location('notifications_product_title12_CA_resource_status_xpath')

            prod_title11 = find_element('notifications_product_title11_CA_plugin_status_xpath')
            prod_title12 = find_element('notifications_product_title12_CA_resource_status_xpath')

            notifications_prod_titles3 = [prod_title11, prod_title12]

            for prod_title in notifications_prod_titles3:
                highlight_element(prod_title)
            capture_screenshot(test_file_name)

# logo_and_headers()

# product_name()


# def logo_and_headers():
#     # env_name = pytest.config.getoption("--env")
#     global header1_element, header2_element
#     redirect_urls = all_url_call()
#     for redirect_url in redirect_urls:
#         driver.get(redirect_url)
#         driver.maximize_window()
#         time.sleep(2)
#         image_element = find_element("netapp_logo_xpath")  # NetApp logo
#         header1_element = find_element("netapp_active_iq_name_xpath")  # header title NetApp ActiveIQ
#         header2_element = find_element("netapp_configAdvisor_name_xpath")  # header title config Advisor
#         element_list = [image_element, header1_element, header2_element]
#         for element in element_list:
#             highlight_element(element)
#         capture_screenshot(test_file_name)
#     result_return = []
#     if header1_element.text == properties("netapp_active_IQ_name"):
#         result_return.append(header1_element.text)
#     else:
#         result_return.append(header1_element.text)
#         print("The Header Title DOES NOT MATCH")
#
#     if header2_element.text == properties("config_advisor_name"):
#         result_return.append(header2_element.text)
#     else:
#         result_return.append(header2_element.text)
#         print("The Header Title DOES NOT MATCH")
#     print(result_return)
#     return result_return