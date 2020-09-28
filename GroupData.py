import pymannkendall as MK
import pandas as pd
import numpy as np
from openpyxl import load_workbook
import xlsxwriter

'''
This code creates the new format spreadheets for BU, FU and OW, sorted by the lake codes
'''

pd.set_option('display.max_columns', 7)

df = pd.read_excel("merged_v3_final_BU_FU_outputs_edit.xlsx")

df['open water'] = df['open water'].astype(np.float16)
df['season'] = df['season'].astype(np.int16)

group = df.groupby('lakename').groups
code_group = df.groupby('lakecode').groups

codes = [*code_group]
names = [*group]    # list of keys (lakenames)

index_start = df['season'].min()
index_end = df['season'].max()

#indexes = group[names[0]]  # accesses the indexes of certain lake

name_sort = []  # list of names in same order as lake codes
for each in codes:
    val = df.loc[df['lakecode'] == each]
    name = val['lakename'].values[0]
    name_sort.append(name)

part1 = codes[:100]

tup_list = list(zip(name_sort, codes))  # list of tuples with lake name and code accordingly

# header = [np.array(codes), np.array(name_sort)]
# merged_frame = pd.DataFrame(columns=header (or codes))    # first header = lake code, 2nd header = lake name LATER
merged_frame = pd.DataFrame()
year = pd.Series(range(index_start, index_end+1))
merged_frame.insert(0, 'YEAR', year)

cols = merged_frame.columns     # list of tuples of multi-index --> cols[x][1] (the 2nd is the code)
# merged_frame[cols[1][0]] --> first column selected based on lake code
# merged_frame[str(part1[2])]
'''
# OPEN WATER DAYS
merged_frame_OW = merged_frame.copy()
for entry in codes:
    indexes = code_group[entry]     # iterate through lake codes (code_group)
    cut_df = df.loc[indexes[0]:indexes[-1], 'lakecode':'open water']
    name = cut_df['lakename'].values[0]
    code = cut_df['lakecode'].values[0]
    temp_df = pd.DataFrame()
    temp_df['YEAR'] = cut_df['season']
    temp_df[code] = cut_df['open water']
    #temp_df = temp_df.set_index('YEAR')
    merged_frame_OW = pd.merge(merged_frame_OW, temp_df, on='YEAR', how='outer')
'''
'''
# FREEZEUP
merged_frame_FU = merged_frame.copy()
for entry in codes:
    indexes = code_group[entry]     # iterate through lake codes (code_group)
    cut_df = df.loc[indexes[0]:indexes[-1], 'lakecode':'open water']
    name = cut_df['lakename'].values[0]
    code = cut_df['lakecode'].values[0]
    tempF_df = pd.DataFrame()
    tempF_df['YEAR'] = cut_df['season']
    tempF_df[code] = cut_df['freezeup']
    #temp_df = temp_df.set_index('YEAR')
    merged_frame_FU = pd.merge(merged_frame_FU, tempF_df, on='YEAR', how='outer')

# BREAKUP
merged_frame_BU = merged_frame.copy()
for entry in codes:
    indexes = code_group[entry]     # iterate through lake codes (code_group)
    cut_df = df.loc[indexes[0]:indexes[-1], 'lakecode':'open water']
    name = cut_df['lakename'].values[0]
    code = cut_df['lakecode'].values[0]
    tempB_df = pd.DataFrame()
    tempB_df['YEAR'] = cut_df['season']
    tempB_df[code] = cut_df['breakup']
    #temp_df = temp_df.set_index('YEAR')
    merged_frame_BU = pd.merge(merged_frame_BU, tempB_df, on='YEAR', how='outer')
'''
'''
frame_list = []
name_list = []
start = 0
size = 346
end = size
for each in range(0, int(len(names)/size)):
    name_list.append(names[start:end])
    frame_list.append(merged_frame)
    start = end
    end = end + 346
    # name_list[1][0] --> 0th entry of second(1) list in name_list

#DONT REMEMBER WHAT THIS WAS FOR
for (snip, frame) in zip(name_list, frame_list):
    for entry in snip:
        indexes = group[entry]
        cut_df = df.loc[indexes[0]:indexes[-1], 'lakename':'open water']
        temp_df = pd.DataFrame()
        temp_df['YEAR'] = cut_df['season']
        name = cut_df['lakename'].values[0]
        temp_df[name] = cut_df['open water']
        temp_df.set_index('YEAR')
        frame = pd.merge(frame, temp_df, how='outer')
'''

'''
First, create merge_frame with just the YEAR as column so that temp_df can later be merged on YEAR
This is only the data frame to be used later, all in columns based on the LAKE CODE


writer = pd.ExcelWriter('NewFormat_Breakup.xlsx', engine='xlsxwriter')
workbook = writer.book
merged_frame_BU.to_excel(writer, index=False)
writer.save()
writer.close()

'''
