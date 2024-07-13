import pandas as pd

# 源Excel文件路径
source_file_path = './对账明细查询表_20240701_17时06分.xlsx'
# 目标Excel文件路径
target_file_path = './对账单2024.06月 - Copy.xlsx'

# 使用pandas读取Excel文件的元数据，但不加载数据
xls = pd.ExcelFile(target_file_path,engine='openpyxl')