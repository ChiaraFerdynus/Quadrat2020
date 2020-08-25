import pandas as pd
import numpy as np
from openpyxl import load_workbook
import xlsxwriter

BU_Q = ['merged_BU_30w_10md', 'merged_BU_30w_20md', 'merged_BU_30w_25md',
        'merged_BU_20w_10md', 'merged_BU_20w_20md', 'merged_BU_20w_25md',
        'merged_BU_50w_10md', 'merged_BU_50w_20md', 'merged_BU_50w_25md']
# BREAK UP
cfQ = pd.DataFrame(index=range(0, 558))
interQ = pd.DataFrame(index=range(0, 558))

for each in BU_Q:
    df = pd.read_excel('merged_BU'+each[-9:]+'.xlsx')
    df = df.replace(r'Not enough data', np.NaN, regex=True)
    window = float(each[-8:-6])
    period = int(window - 20)
    parameters = each[-8:]
    count = df.count(axis=1) - 1
    interQ['1'] = count
    interQ = interQ.shift(periods=period)
    cfQ[parameters] = interQ
    interQ = interQ.drop(['1'], axis=1)

cfQ.insert(0, 'Year', range(1462, 2020))
# FREEZE UP
cfT = pd.DataFrame(index=range(0, 558))
interT = pd.DataFrame(index=range(0, 558))

for each in BU_Q:
    dfT = pd.read_excel('merged_FU'+each[-9:]+'.xlsx')
    dfT = dfT.replace(r'Not enough data', np.NaN, regex=True)
    window = float(each[-8:-6])
    period = int(window - 20)
    parameters = each[-8:]
    count = dfT.count(axis=1) - 1
    interT['1'] = count
    interT = interT.shift(periods=period)
    cfT[parameters] = interT
    interT = interT.drop(['1'], axis=1)

cfT.insert(0, 'Year', range(1462, 2020))
# OPEN WATER
cfZ = pd.DataFrame(index=range(0, 558))
interZ = pd.DataFrame(index=range(0, 558))

for each in BU_Q:
    dfZ = pd.read_excel('merged_OW'+each[-9:]+'.xlsx')
    dfZ = dfZ.replace(r'Not enough data', np.NaN, regex=True)
    window = float(each[-8:-6])
    period = int(window - 20)
    parameters = each[-8:]
    count = dfZ.count(axis=1) - 1
    interZ['1'] = count
    interZ = interZ.shift(periods=period)
    cfZ[parameters] = interZ
    interZ = interZ.drop(['1'], axis=1)

cfZ.insert(0, 'Year', range(1462, 2020))


writer = pd.ExcelWriter('BU_FU_OW_stats.xlsx', engine='xlsxwriter')
workbook = writer.book
cfQ.to_excel(writer, sheet_name='BU', index=False)
cfT.to_excel(writer, sheet_name='FU', index=False)
cfZ.to_excel(writer, sheet_name='OW', index=False)
writer.save()
writer.close()

