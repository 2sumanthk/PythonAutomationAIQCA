from functions.ExcelFunctions import ReadWriteExcel

# Reading data from excel
# x = ReadWriteExcel("C:/Users/Sumanth/Downloads/nba.xlsx")
y = ReadWriteExcel("C:/Users/Sumanth/Downloads/Test_data.xlsx")
# print(x.read_by_col_index('nba', 3, 4))  # SF
# print(x.read_by_col_name('nba', 3, 'Weight'))  # 235
# print(x.get_row_count('nba'))  # 458
# print(x.get_col_count('nba'))  # 9

print(y.get_row_count('CA_product_names'))
for value in range(1, y.get_row_count('CA_product_names')):
    print(value)
    print(y.get_cell_value('CA_product_names', value, 1))
    print(y.read_by_col_name('CA_product_names', value, 'NetApp'))

# writing data to excel

# x.write_by_col_index('nba', 3, 4, 'SF')
