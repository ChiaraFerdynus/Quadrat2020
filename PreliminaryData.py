import pymannkendall as MK
import pandas as pd
import numpy as np
from openpyxl import load_workbook

#path  = r"C:\Users\Chiara Ferdynus\Documents\PYCHARM\test_site_merged.xlsx"
#writer = pd.ExcelWriter(path, engine = 'openpyxl')
#writer.book = book

# Load the given data
df = pd.read_excel("test_site.xlsx")
'''
# separate Julian Days column, period from '31 - '05
JD = df['ALA-RIEVELI']
date = df['NAME']
print(date)

test = MK.original_test(JD, 0.1) # MK test of Julian Days with alpha = 0.1
slope = MK.sens_slope(JD) # Sen's slope of Julian Days, already included in MK test

print(JD.loc[0: 30]);

df_transpose = df.copy()
df_transpose = df_transpose.transpose()

window = 30 # 30 year window
length = JD.shape[0]
iterations = length - (window - 1)

start = df['NAME'].values[0]
start_index = df['NAME'].values[window-1]
final_index = df['NAME'].values[length-1]+1

Year = pd.Series(range(start_index, final_index))

stats_list = pd.DataFrame(index=Year, columns=['trend', 'Ha', 'p', 'Z', 'S', 'VAR(S)', 'slope'])
# add Year column and set it as index

for instance in range(0, iterations):
    snip = JD.loc[instance:instance+window-1]
    snip_test = MK.original_test(snip, 0.1)
    stats_list['trend'].values[instance] = snip_test[0]
    stats_list['Ha'].values[instance] = snip_test[1]
    stats_list['p'].values[instance] = snip_test[2]
    stats_list['Z'].values[instance] = snip_test[3]
    stats_list['S'].values[instance] = snip_test[5]
    stats_list['VAR(S)'].values[instance] = snip_test[6]
    stats_list['slope'].values[instance] = snip_test[7]

print(stats_list)

#stats_list.to_excel("test_site_stats_30.xlsx")

ALL_df = pd.DataFrame()

files = ['test_site_stats_20.xlsx', 'test_site_stats_30.xlsx', 'test_site_stats_50.xlsx', 'test_site_stats_ALL.xlsx']
for f in files:
    new_data = pd.read_excel(f)
    ALL_df = ALL_df.append(new_data)


# BETTER VERSION

windows = [20, 30, 50, 75]
for each in windows:
    start_index = df['NAME'].values[each - 1]
    final_index = df['NAME'].values[length - 1] + 1

    Year = pd.Series(range(start_index, final_index))

    iterations = length - (each - 1)
    stats_list2 = pd.DataFrame(index=range(0, iterations),
                               columns=['Year', 'trend', 'Ha', 'p', 'Z', 'S', 'VAR(S)', 'slope'])

    for instance in range(0, iterations):
        stats_list2['Year'].values[instance] = Year[instance]

    for instance in range(0, iterations):
        snip = JD.loc[instance:instance + each - 1]
        snip_test = MK.original_test(snip, 0.1)
        stats_list2['trend'].values[instance] = snip_test[0]
        stats_list2['Ha'].values[instance] = snip_test[1]
        stats_list2['p'].values[instance] = snip_test[2]
        stats_list2['Z'].values[instance] = snip_test[3]
        stats_list2['S'].values[instance] = snip_test[5]
        stats_list2['VAR(S)'].values[instance] = snip_test[6]
        stats_list2['slope'].values[instance] = snip_test[7]

    print(stats_list2)
    sheet = str(each) +' Year window'
    stats_list2.to_excel(writer, sheet_name=sheet, index=False)

writer.save()
writer.close()
'''

'''works if Year and Location are in columns'''
def mk_column(Data, YearCol, LocCol, windows):
    for each in windows:
        length = Data[LocCol].shape[0]
        start_index = Data[YearCol].values[each - 1]
        final_index = Data[YearCol].values[length - 1] + 1

        Year = pd.Series(range(start_index, final_index))

        iterations = length - (each - 1)
        stats_list2 = pd.DataFrame(index=range(0, iterations),
                                   columns=['Year', 'trend', 'Ha', 'p', 'Z', 'S', 'VAR(S)', 'slope'])
        stats_list2.insert(0,'Name', None)
        stats_list2['Name'].values[0] = LocCol

        for instance in range(0, iterations):
            stats_list2['Year'].values[instance] = Year[instance]

        for instance in range(0, iterations):
            snip = Data[LocCol].loc[instance:instance + each - 1]
            snip_test = MK.original_test(snip, 0.1)
            stats_list2['trend'].values[instance] = snip_test[0]
            stats_list2['Ha'].values[instance] = snip_test[1]
            stats_list2['p'].values[instance] = snip_test[2]
            stats_list2['Z'].values[instance] = snip_test[3]
            stats_list2['S'].values[instance] = snip_test[5]
            stats_list2['VAR(S)'].values[instance] = snip_test[6]
            stats_list2['slope'].values[instance] = snip_test[7]

        # stats_list2 = stats_list2.transpose()
        # stats_list2.insert(stats_list2.shape[1],None,None)
        # stats_list2 = stats_list2.transpose()
        stats_list2 = stats_list2.append(pd.Series([np.nan]), ignore_index=True)
        print(stats_list2)
       # stats_list2.to_excel("testNewColTranspose.xlsx", index=False)
        ''' need to find way to store it in Excel '''

mk_column(df, 'NAME', 'ALA-RIEVELI', [30])

empty = pd.Series([None,None], index=['NAME', 'ALA-RIEVELI'])
#df = df.append(pd.Series([np.nan]), ignore_index = True)
