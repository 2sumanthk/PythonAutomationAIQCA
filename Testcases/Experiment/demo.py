from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from pyjavaproperties import Properties

prop_en = Properties()
properties_file_en = open('C://Users//Administrator//PycharmProjects//PythonAutomationAIQCA//Resources//configurations//properties//config.properties')
prop_en.load(properties_file_en)


def properties(prop_value):
    value = prop_en[prop_value]
    return value

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(properties('health_check_url'))

