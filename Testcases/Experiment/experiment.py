import base64
import re

# from functions.base_functions_zh import *
from pyjavaproperties import Properties
import pytest
import allure
from functions.ExcelFunctions import ReadWriteExcel
import sys

# # Reading data from excel
# data_read = ReadWriteExcel(
#     "C://Users//Sumanth//PycharmProjects//PythonTesting//Resources//configurations//testdata//Test_data.xlsx")
#
# prop = Properties()
# properties_file = open(
#     'C://Users//Sumanth//PycharmProjects//PythonTesting//Resources//configurations//properties//config.properties')
# prop.load(properties_file)


# def url_call():
#     url_value = []
#     for value in prop.keys():
#         if value.endswith('_url'):
#             value = prop[value]
#             url_value.append(value)
#     return url_value


def search_strings(pattern, string):
    match = re.findall(pattern, string)
    return match  # match returns a list of matched strings


# search_strings('python', 'python is good to learn, python is easy, python is life')

# colindex = 1
# row_count = data_read.get_row_count('CA_product_names') + 1
# print(row_count)
# for row in range(1, row_count):
#     if ((data_read.get_cell_value('CA_product_names', row, colindex)) == 'test_cp_3_notifications') and (
#             (data_read.read_by_col_name('CA_product_names', row, 'NetApp English')) == (
#     properties_china('notifications_test_cp_3_string3'))):
#         expected_output = data_read.read_by_col_name('CA_product_names', row, 'NetApp English')
#         print(expected_output)
#
# print(sys.getdefaultencoding())
# print('Active IQ Config Advisor 插件状态')
str1 = base64.b64encode("Active IQ Config Advisor AutoSupport \u3092\u6709\u52B9\u306B\u3059\u308B\uFF08\u63A8\u5968)".encode('utf-16'))
str2 = base64.b64decode(str1).decode('utf-16')
print(str2)
