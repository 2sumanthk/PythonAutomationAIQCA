import base64
import urllib.request

import allure
from allure_commons.types import AttachmentType
from pyjavaproperties import Properties
from selenium import webdriver
from selenium.webdriver import ActionChains, DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from datetime import datetime
import re
import time
import logging
import os

prop_ja = Properties()
properties_file_ja = open(
    'C://Users//Administrator//PycharmProjects//PythonAutomationAIQCA//Resources//configurations//properties//config_ja.properties')
prop_ja.load(properties_file_ja)


def properties_japan(prop_key):
    prop_value = prop_ja[prop_key]
    return prop_value


browser_name = 'chrome'
if browser_name == 'chrome':
    options = webdriver.ChromeOptions()
    options.add_argument('ChromeDriverManager().install()')
    options.add_argument('--ignore-ssl-errors=yes')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--lang=ja-JP')
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)


elif browser_name == 'firefox':
    options = webdriver.FirefoxOptions()
    ff_profile = webdriver.FirefoxProfile()
    binary = FirefoxBinary('C:\\Program Files\\Mozilla Firefox\\firefox.exe')
    firefox_capabilities = DesiredCapabilities.FIREFOX
    ff_profile.set_preference("intl.accept_languages", "ja")
    ff_profile.update_preferences()
    firefox_capabilities['marionette'] = True
    ff_profile.accept_untrusted_certs = True
    driver = webdriver.Firefox(firefox_binary=binary, executable_path=GeckoDriverManager().install(), firefox_profile=ff_profile)

else:
    print('specify the correct browser name')


def maximize_window():
    with allure.step("Maximizing Window..."):
        driver.maximize_window()


def minimize_window():
    driver.minimize_window()


def title():
    with allure.step("Verifying the window title  : " + driver.title):
        sleep(1)
        return driver.title


def click(element_to_be_clicked):
    with allure.step("Clicking on " + element_to_be_clicked):
        obj = properties_japan(element_to_be_clicked)
        if element_to_be_clicked.endswith('_xpath'):
            val = driver.find_element('xpath', obj).click()
        elif element_to_be_clicked.endswith('_id'):
            val = driver.find_element('id', obj).click()
        elif element_to_be_clicked.endswith('_name'):
            val = driver.find_element('name', obj).click()
        else:
            val = driver.find_element('css_selector', obj).click()


def move_to_element(element):
    obj = properties_japan(element)
    if element.endswith('_xpath'):
        source = driver.find_element('xpath', obj)
    elif element.endswith('_id'):
        source = driver.find_element('id', obj)
    elif element.endswith('_name'):
        source = driver.find_element('name', obj)
    else:
        source = driver.find_element('css_selector', obj)
    # action chain object
    action = ActionChains(driver)
    # move to element operation
    return action.move_to_element(source)


def type_in(element, data):
    placeholder_value = find_element(element).get_attribute('placeholder')
    with allure.step("Typing data in the "+placeholder_value+" field : " + data):
        return get_element(element).send_keys(data)


def find_element(element_to_be_found):
    with allure.step("Finding Element " + element_to_be_found):
        obj = properties_japan(element_to_be_found)
        if element_to_be_found.endswith('_xpath'):
            source = driver.find_element('xpath', obj)
        elif element_to_be_found.endswith('_id'):
            source = driver.find_element('id', obj)
        elif element_to_be_found.endswith('_name'):
            source = driver.find_element('name', obj)
        else:
            source = driver.find_element('css_selector', obj)
        return source


def find_elements(elements_to_be_found):
    obj = properties_japan(elements_to_be_found)
    if elements_to_be_found.endswith('_xpath'):
        val = driver.find_elements('xpath', obj)
    elif elements_to_be_found.endswith('_id'):
        val = driver.find_elements('id', obj)
    elif elements_to_be_found.endswith('_name'):
        val = driver.find_elements('name', obj)
    else:
        val = driver.find_elements('css_selector', obj)
    return val


def get_attribute(link_element, attribute_name):
    obj = properties_japan(link_element)
    if link_element.endswith('_xpath'):
        val = driver.find_element('xpath', obj).get_attribute(attribute_name)
    elif link_element.endswith('_id'):
        val = driver.find_element('id', obj).get_attribute(attribute_name)
    elif link_element.endswith('_name'):
        val = driver.find_element('name', obj).get_attribute(attribute_name)
    else:
        val = driver.find_element('css_selector', obj).get_attribute(attribute_name)
    return val

# Common Utility Functions


def is_element_present(locator_key):
    obj = properties_japan(locator_key)
    element_list = []
    wait = WebDriverWait(driver, 30)
    if locator_key.endswith('_xpath'):
        element_list = wait.until(expected_conditions.presence_of_all_elements_located((By.XPATH, obj)))
    elif locator_key.endswith('_id'):
        element_list = wait.until(expected_conditions.presence_of_all_elements_located((By.ID, obj)))
    elif locator_key.endswith('_name'):
        element_list = wait.until(expected_conditions.presence_of_all_elements_located((By.NAME, obj)))
    else:
        element_list = wait.until(expected_conditions.presence_of_all_elements_located((By.CSS_SELECTOR, obj)))
    if len(element_list) == 0:
        return False
        # report Failure
    else:
        return True


def is_element_visible(locator_key):
    obj = properties_japan(locator_key)
    element_list = []
    wait = WebDriverWait(driver, 30)
    if locator_key.endswith('_xpath'):
        element_list = wait.until(expected_conditions.visibility_of_all_elements_located((By.XPATH, obj)))
    elif locator_key.endswith('_id'):
        element_list = wait.until(expected_conditions.visibility_of_all_elements_located((By.ID, obj)))
    elif locator_key.endswith('_name'):
        element_list = wait.until(expected_conditions.visibility_of_all_elements_located((By.NAME, obj)))
    else:
        element_list = wait.until(expected_conditions.visibility_of_all_elements_located((By.CSS_SELECTOR, obj)))
    if len(element_list) == 0:
        return False
        # report Failure
    else:
        return True


def get_element(locator_key):
    obj = properties_japan(locator_key)
    if is_element_present(locator_key) and is_element_visible(locator_key):
        try:
            if locator_key.endswith('_xpath'):
                element = driver.find_element('xpath', obj)
            elif locator_key.endswith('_id'):
                element = driver.find_element('id', obj)
            elif locator_key.endswith('_name'):
                element = driver.find_element('name', obj)
            else:
                element = driver.find_element('css_selector', obj)
            return element
        except Exception:
            print("element not found")
    else:
        print('element is not present or visible ', locator_key)


def highlight_element(element):
    checkpoint = element.text
    with allure.step("Highlighting Checkpoint - " + checkpoint):
        driver.execute_script("arguments[0].setAttribute('style', 'background: none; border: 5px solid red;');",
                          element)
    time.sleep(1)


def switch_to_window(value):
    driver.switch_to.window(driver.window_handles[value])
    # value = 0 -> switches to  default window or primary working window,
    # value = 1 -> switches to 1st new window or new tab


def scroll_page(height):
    driver.execute_script("window.scrollTo(0," + str(height) + ")")


def scroll_to_location(element):
    value = find_element(element)
    driver.execute_script('arguments[0].scrollIntoView({block: "center", inline: "center"})', value)
    time.sleep(2)
    # value2 = value.location_once_scrolled_into_view()


def capture_screenshot(test_filename):
    test_filename_new = test_filename.split('.py')
    now = datetime.now()  # dd/mm/YY H:M:S
    dt_string = now.strftime("%b_%d_%Y_%I_%M_%S")
    screenshot_name = test_filename_new[0] + '_' + browser_name + '_' + dt_string
    driver.get_screenshot_as_file('C://Users//Administrator//PycharmProjects//PythonAutomationAIQCA//ScreenShots//ScreenShots_JA//'+ screenshot_name + '.png')
    allure.attach(driver.get_screenshot_as_png(), ""+screenshot_name, AttachmentType.PNG)


def quit_browser():
    sleep(1)
    driver.quit()


def close_browser():
    sleep(1)
    driver.close()


def sleep(time_in_seconds):
    time.sleep(time_in_seconds)


def search_strings(pattern, string):
    match = re.search(pattern, string)
    if match:
        found = match.group(0)
        return found
    else:
        return "Checkpoint captured did not match with", pattern


def all_url_call():
    url_values = []
    for value in prop_ja.keys():
        if value.endswith('_url'):
            value = prop_ja[value]
            url_values.append(value)
    return url_values


def encode_and_decode(value):
    str1 = base64.b64encode(value.encode('utf-8'))
    str2 = base64.b64decode(str1).decode('utf-8')
    print(str2)


# browser_name = input("Enter The Browser Name :")
# locale = input("Enter The Locale Option (en-US or zh-CN or ja-JP) :")
# if browser_name == 'chrome' and (locale == 'en-US' or locale == 'zh-CN' or locale == 'ja-JP'):
#     options = webdriver.ChromeOptions()
#     options.add_argument('ChromeDriverManager().install()')
#     options.add_argument('--ignore-ssl-errors=yes')
#     options.add_argument('--ignore-certificate-errors')
#     options.add_argument('--lang=' + locale)
#     driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
#
# elif browser_name == 'firefox' and (locale == 'en-US' or locale == 'zh-CN' or locale == 'ja-JP'):
#     options = webdriver.FirefoxProfile()
#     options.binary_location = "/usr/bin/firefox"
#     # options.add_("-headless")
#     options.accept_untrusted_certs = True
#     driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), firefox_options=options)
#
# else:
#     print('specify the correct browser name or language correctly')

# def all_locale_call():
#     locale_values = []
#     for locale in prop.keys():
#         if locale.endswith('_locale'):
#             locale = prop[locale]
#             locale_values.append(locale)
#     return locale_values


# def fetch_image_urls(img_objects):
#     img_url_list = []
#     for img_url in img_objects:
#         src_val = img_url.get_attribute('src')
#         img_url_list.append(src_val)
#
#     image_elements = []
#     for value in img_url_list:
#         value = value.split('http://localhost:8055/')
#         new_value = ""
#         value = new_value.join(value)
#         value = driver.find_element_by_xpath("//img[@src='" + value + "']")
#         image_elements.append(value)
#     return image_elements


# def get_redirect_url(url):
#     request = urllib.request.urlopen(url)
#     return request.url
#
#
# def get_urls(filename):
#     with open(filename) as infile:
#         return [get_redirect_url(url.strip()) for url in infile]

# def image_elements_capture(image_url_list):
#     image_elements = []
#     for value in image_url_list:
#         value = value.split('http://localhost:8055/')
#         new_value = ""
#         value = new_value.join(value)
#         value = driver.find_element_by_xpath("//img[@src='" + value + "']")
#         image_elements.append(value)
#     return image_elements


# def link_elements_capture(links_url_list):
#     for value in links_url_list:
#         stripped_value = value.rstrip('/')
#         if not value == stripped_value:
#             value = driver.find_element_by_xpath("//a[@href='" + stripped_value + "']")
#             highlight_element(value)
#     capture_screenshot()
#
#     for value in links_url_list:
#         add_slash_value = value + "/"
#         if not value == add_slash_value:
#             value = driver.find_element_by_xpath("//a[@href='" + add_slash_value + "']")
#             driver.execute_script("arguments[0].setAttribute('style', 'background: none; border: 5px solid red;');",
#                                   value)
#     capture_screenshot()


# def fetch_prod_names(prod_name_objects):
#     prod_name_list = list()
#     for prod_name in prod_name_objects:
#         # url_begin = 'http://localhost:8055/'
#         href_val = prod_name.get_attribute('href')
#         links_url_list.append(href_val)
#     # verify_link_url(links_url_list)
#     return prod_name_list


# def verify_img_url(captured_url):
#     filename = 'lenovo_img_file_url.txt'
#     with open(filename) as file:
#         for url_f in file:
#             for url_c in captured_url:
#                 if url_f == url_c:
#                     print('Image Source and the image url matches successfully->', captured_url)
#                     capture_screenshot()


# def verify_link_url(captured_url):
#     filename = 'lenovo_link_file_url.txt'
#     with open(filename) as file:
#         for url_f in file:
#             for url_c in captured_url:
#                 if url_f == url_c:
#                     print('Link Source and the link url matches successfully->', captured_url)
#                     capture_screenshot()


# for redirect_url in get_urls('input_url.txt'):
#     print('In the Page', redirect_url)
#     get_url = driver.get(redirect_url)
#     driver.maximize_window()
#
#     image_objects = driver.find_elements_by_tag_name('img')
#     img_url_list = fetch_image_urls(image_objects)
#
#     string_objects = driver.find_elements_by_tag_name('div')
#
#     links_url_list = fetch_link_urls(string_objects)
#
#     image_elements_capture(img_url_list)
#
#     link_elements_capture(links_url_list)
