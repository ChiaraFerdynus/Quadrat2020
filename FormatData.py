import pandas as pd
import numpy as np
from openpyxl import load_workbook
import xlsxwriter

df = pd.read_excel("merged_v3_final_BU_FU_outputs_edit.xlsx")

code_group = df.groupby('lakecode').groups

codes = [*code_group]

name_sort = []  # list of names in same order as lake codes
for each in codes:
    val = df.loc[df['lakecode'] == each]
    name = val['lakename'].values[0]
    name_sort.append(name)

name_df = pd.DataFrame(name_sort).T
'''
slope_data = ['merged_OW_30w_10md', 'merged_BU_30w_10md', 'merged_FU_30w_10md', 'merged_OW_30w_20md',
              'merged_BU_30w_20md', 'merged_FU_30w_20md', 'merged_OW_20w_10md', 'merged_BU_20w_10md',
              'merged_FU_20w_10md', 'merged_OW_20w_20md', 'merged_BU_20w_20md', 'merged_FU_20w_20md',
              'merged_OW_50w_10md', 'merged_BU_50w_10md', 'merged_FU_50w_10md', 'merged_OW_50w_20md',
              'merged_BU_50w_20md', 'merged_FU_50w_20md']

OW_slope = ['merged_OW_30w_10md', 'merged_OW_30w_20md', 'merged_OW_30w_25md',
            'merged_OW_20w_10md', 'merged_OW_20w_20md', 'merged_OW_20w_25md',
            'merged_OW_50w_10md', 'merged_OW_50w_20md', 'merged_OW_50w_25md']

BU_slope = ['merged_BU_30w_10md', 'merged_BU_30w_20md', 'merged_BU_30w_25md',
            'merged_BU_20w_10md', 'merged_BU_20w_20md', 'merged_BU_20w_25md',
            'merged_BU_50w_10md', 'merged_BU_50w_20md', 'merged_BU_50w_25md']

FU_slope = ['merged_FU_30w_10md', 'merged_FU_30w_20md', 'merged_FU_30w_25md',
            'merged_FU_20w_10md', 'merged_FU_20w_20md', 'merged_FU_20w_25md',
            'merged_FU_50w_10md', 'merged_FU_50w_20md', 'merged_FU_50w_25md']
'''

OW_trend = ['trend_OW_30w_10md', 'trend_OW_30w_20md', 'trend_OW_30w_25md',
            'trend_OW_20w_10md', 'trend_OW_20w_20md', 'trend_OW_20w_25md',
            'trend_OW_50w_10md', 'trend_OW_50w_20md', 'trend_OW_50w_25md']

BU_trend = ['trend_BU_30w_10md', 'trend_BU_30w_20md', 'trend_BU_30w_25md',
            'trend_BU_20w_10md', 'trend_BU_20w_20md', 'trend_BU_20w_25md',
            'trend_BU_50w_10md', 'trend_BU_50w_20md', 'trend_BU_50w_25md']

FU_trend = ['trend_FU_30w_10md', 'trend_FU_30w_20md', 'trend_FU_30w_25md',
            'trend_FU_20w_10md', 'trend_FU_20w_20md', 'trend_FU_20w_25md',
            'trend_FU_50w_10md', 'trend_FU_50w_20md', 'trend_FU_50w_25md']


writer = pd.ExcelWriter('OW_Q.xlsx', engine='xlsxwriter')
workbook = writer.book

format1 = workbook.add_format({'font_color': '#006100'})  # green
format2 = workbook.add_format({'bg_color':   '#ffcccb', 'border': 1})  # red fill
format3 = workbook.add_format({'font_color': '#9C0006'})  # red
format4 = workbook.add_format({'bg_color':   '#C6EFCE', 'border': 1})  # green fill
format5 = workbook.add_format({'bg_color':   '#D3D3D3', 'border': 1})  # grey fill
format6 = workbook.add_format({'font_color': '#ffcccb'})  # light red

'''
for each in OW_trend:
    df = pd.read_excel('Z'+each[-12:]+'.xlsx')
    # name_df.to_excel(writer, sheet_name=each[10:], index=False, startrow=0, startcol=1)
    df.to_excel(writer, sheet_name=each[-8:], index=False, startrow=1)
    worksheet = writer.sheets[each[-8:]]
    j = 1
    for entry in name_sort:
        worksheet.write(0, j, entry)
        j = j+1

    worksheet.conditional_format(2, 1, df.shape[0] + 1, df.shape[1],
                                 {'type': 'cell', 'criteria': 'equal to',
                                  'value': '"no trend"', 'format': format5})
    worksheet.conditional_format(2, 1, df.shape[0] + 1, df.shape[1],
                                 {'type': 'cell', 'criteria': 'equal to',
                                  'value': '"increasing"', 'format': format4})
    worksheet.conditional_format(2, 1, df.shape[0] + 1, df.shape[1],
                                 {'type': 'cell', 'criteria': 'equal to',
                                  'value': '"decreasing"', 'format': format2})

writer.save()
writer.close()
'''


for each in OW_trend:
    df = pd.read_excel('merged'+each[-12:]+'.xlsx')
    # name_df.to_excel(writer, sheet_name=each[10:], index=False, startrow=0, startcol=1)
    df.to_excel(writer, sheet_name=each[-8:], index=False, startrow=1)
    worksheet = writer.sheets[each[-8:]]
    j = 1
    for entry in name_sort:
        worksheet.write(0, j, entry)
        j = j+1

    worksheet.conditional_format(2, 1, df.shape[0] + 1, df.shape[1],
                                 {'type': 'cell', 'criteria': 'equal to',
                                  'value': '"Not enough data"', 'format': format3})
    worksheet.conditional_format(2, 1, df.shape[0] + 1, df.shape[1],
                                 {'type': 'cell', 'criteria': 'not equal to',
                                  'value': '"Not enough data"', 'format': format1})

writer.save()
writer.close()

'''
for each in FU_slope:
    df = pd.read_excel(each+'.xlsx')
    # name_df.to_excel(writer, sheet_name=each[10:], index=False, startrow=0, startcol=1)
    df.to_excel(writer, sheet_name=each[10:], index=False, startrow=1)
    worksheet = writer.sheets[each[10:]]
    j = 1
    for entry in name_sort:
        worksheet.write(0, j, entry)
        j = j+1

    worksheet.conditional_format(2, 1, df.shape[0] + 1, df.shape[1],
                                 {'type': 'cell', 'criteria': 'equal to',
                                  'value': '"Not enough data"', 'format': format3})
    worksheet.conditional_format(2, 1, df.shape[0] + 1, df.shape[1],
                                 {'type': 'cell', 'criteria': 'not equal to',
                                  'value': '"Not enough data"', 'format': format1})

writer.save()
writer.close()
'''
'''
for each in OW_slope:
    df = pd.read_excel(each+'.xlsx')
    # name_df.to_excel(writer, sheet_name=each[10:], index=False, startrow=0, startcol=1)
    df.to_excel(writer, sheet_name=each[10:], index=False, startrow=1)
    worksheet = writer.sheets[each[10:]]
    j = 1
    for entry in name_sort:
        worksheet.write(0, j, entry)
        j = j+1

    worksheet.conditional_format(2, 1, df.shape[0] + 1, df.shape[1],
                                 {'type': 'cell', 'criteria': 'equal to',
                                  'value': '"Not enough data"', 'format': format3})
    worksheet.conditional_format(2, 1, df.shape[0] + 1, df.shape[1],
                                 {'type': 'cell', 'criteria': 'not equal to',
                                  'value': '"Not enough data"', 'format': format1})

writer.save()
writer.close()
'''


