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

driver.get('C:\\Users\\Sumanth\\PycharmProjects\\PythonTesting\\dropdown.html')

all_elements = []
AllDiv = driver.find_elements_by_tag_name('div')
All_options = driver.find_elements_by_tag_name('option')
all_elements.append(AllDiv)
all_elements.append(All_options)


def all_text(web_elements):
    result = set()
    final = []
    for ele_list in web_elements:
        for ele in ele_list:
            ele_text = ele.text.split(' ')
            for value in ele_text:
                result.add(value)
        for ele_new in result:
            if len(ele_new) > 0:
                final.append(ele_new)
        return final


def is_eng():
    all_val = all_text(all_elements)
    print(all_val)
    for value in all_val:
        value = re.sub(r'[^\x00-\x7f]', r'', value)
        # value = value.encode('ascii', errors='ignore')
        if len(value) > 0:
            print(value)


is_eng()
