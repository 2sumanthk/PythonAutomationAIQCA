from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import re


browserName = 'chrome'
if browserName == 'chrome':
    driver = webdriver.Chrome(ChromeDriverManager().install())
elif browserName == 'firefox':
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
else:
    print('specify the correct browser name')

driver.get('https://jp.pactera.com/')

AllDiv = driver.find_elements_by_tag_name('div')


def all_text(web_elements):
    result = []
    final = []
    for ele in web_elements:
        ele_text = ele.text.split(' ')
        for value in ele_text:
            if value not in result:
                result.append(value)
    for ele_new in result:
        if len(ele_new) > 0:
            final.append(ele_new)
    return final


def is_eng():
    all_val = all_text(AllDiv)
    for value in all_val:
        value = re.sub(r'[^\x00-\x7f]', r'', value)
        # value = value.encode('ascii', errors='ignore')
        print(value)


is_eng()