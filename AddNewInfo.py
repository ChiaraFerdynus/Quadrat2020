import pandas as pd
import numpy as np
from openpyxl import load_workbook
import xlsxwriter

'''
This script only organizes additional info according to lake codes
'''

dfOld = pd.read_excel("merged_v3_final_BU_FU_outputs_edit.xlsx")

code_group = dfOld.groupby('lakecode').groups
codes = [*code_group]

df = pd.read_excel('Sites1.xlsx')
code_group = df.groupby('lakecode').groups
codesNew = [*code_group]

dfIndex = df.set_index('lakecode')
dfIndexTr = dfIndex.transpose()

NewInfo = pd.DataFrame(index=['lakename', 'lakeorriver', 'region',
                              'country', 'lat_decimal', 'lon_decimal'],
                       columns=codes)

for code in codes:
    NewInfo[code] = dfIndexTr[code]

writer = pd.ExcelWriter('NewInfo1.xlsx', engine='xlsxwriter')
workbook = writer.book
NewInfo.to_excel(writer, index=True)
writer.save()
writer.close()

#  dfcheck = pd.read_excel('merged_OW_30w_10md.xlsx')
