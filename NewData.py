import pymannkendall as MK
import pandas as pd
import numpy as np
from openpyxl import load_workbook
import xlsxwriter

df = pd.read_excel("NewData.xlsx")

columns = df.columns[1:]  # drop first one (bc it is the Year)


def missing_values(snip, window, threshold):
    missing = snip.isnull().sum()
    percent = (missing/window)*100
    if percent > threshold:
        return 0
    else:
        # print(missing, percent)
        return 1


def multiple_dfs(df_list, file_name, spaces):
    writer = pd.ExcelWriter(file_name, engine='openpyxl')
    row = 0
    for dataframe in df_list:
        dataframe.to_excel(writer, index=False, startrow=row , startcol=0)
        row = row + len(dataframe.index) + spaces + 1
    writer.save()
    # writer.close() #(?)


'''works if Year and Location are in columns [dataframe, 'NAME', 'Location', [windows]]'''
def mk_column(Data, YearCol, LocCol, windows, datalist, threshold, alpha = 0.1):
    for each in windows:
        length = Data[LocCol].shape[0]
        start_index = Data[YearCol].values[each - 1]
        final_index = Data[YearCol].values[length - 1] + 1

        Year = pd.Series(range(start_index, final_index))

        iterations = length - (each - 1)
        stats_list2 = pd.DataFrame(index=range(0, iterations),
                                   columns=[LocCol, 'Year', 'trend', 'Ha', 'p', 'Z', 'S', 'VAR(S)', 'slope'])
        stats_list2[LocCol].values[0] = str(each)+" Year window"

        for instance in range(0, iterations):
            stats_list2['Year'].values[instance] = Year[instance]

        for instance in range(0, iterations):
            snip = Data[LocCol].loc[instance:instance + each - 1] # INSERT TEST FOR 10%
            if missing_values(snip, each, threshold):
                snip_test = MK.original_test(snip, alpha)
                stats_list2['trend'].values[instance] = snip_test.trend
                stats_list2['Ha'].values[instance] = snip_test.h
                stats_list2['p'].values[instance] = snip_test.p
                stats_list2['Z'].values[instance] = snip_test.z
                stats_list2['S'].values[instance] = snip_test.s
                stats_list2['VAR(S)'].values[instance] = snip_test.var_s
                stats_list2['slope'].values[instance] = snip_test.slope

            else:
                stats_list2['trend'].values[instance] = 'Not enough data'

        #print(stats_list2)
        datalist.append(stats_list2)  # this is used if you want to enter different data frames in a list

    ''' need to find way to store it in Excel '''


def mk_col_slope(Data, YearCol, LocCol, window, TH, alpha=0.1):
    length = Data[LocCol].shape[0]
    start_index = Data[YearCol].values[window - 1]
    final_index = Data[YearCol].values[length - 1] + 1

    Year = pd.Series(range(start_index, final_index))

    iterations = length - (window - 1)
    stats_list2 = pd.DataFrame(index=range(0, iterations),
                               columns=['Year', LocCol])

    for instance in range(0, iterations):
        stats_list2['Year'].values[instance] = Year[instance]

    for instance in range(0, iterations):
        snip = Data[LocCol].loc[instance:instance + window - 1]
        if missing_values(snip, window, TH):
            snip_test = MK.original_test(snip, alpha)
            stats_list2[LocCol].values[instance] = snip_test.slope

        else:
            stats_list2[LocCol].values[instance] = 'Not enough data'

    #print(stats_list2)
    return stats_list2
    #datalist = pd.merge(datalist, stats_list2, on='Year', how='outer')


def mk_col_trend(Data, YearCol, LocCol, window, TH, alpha=0.1):
    length = Data[LocCol].shape[0]
    start_index = Data[YearCol].values[window - 1]
    final_index = Data[YearCol].values[length - 1] + 1

    Year = pd.Series(range(start_index, final_index))

    iterations = length - (window - 1)
    stats_list2 = pd.DataFrame(index=range(0, iterations),
                               columns=['Year', LocCol])

    for instance in range(0, iterations):
        stats_list2['Year'].values[instance] = Year[instance]

    for instance in range(0, iterations):
        snip = Data[LocCol].loc[instance:instance + window - 1]
        if missing_values(snip, window, TH):
            snip_test = MK.original_test(snip, alpha)
            stats_list2[LocCol].values[instance] = snip_test.trend

        else:
            stats_list2[LocCol].values[instance] = 'Not enough data'

    #print(stats_list2)
    return stats_list2


def merge_frame(data, window, threshold):
    sample_list = pd.DataFrame(index=range(0, data.shape[0] - (window - 1)))
    year = pd.Series(data['NAME'][0+(window - 1):])
    year.reset_index(drop=True, inplace=True)
    sample_list.insert(0, 'Year', year)

    for entry in columns:
        prev = mk_col_slope(data, 'NAME', entry, window, threshold)
        sample_list = pd.merge(sample_list, prev, on='Year', how='outer')

    return sample_list


def merge_frame_trend(data, window, threshold):
    sample_list = pd.DataFrame(index=range(0, data.shape[0] - (window - 1)))
    year = pd.Series(data['NAME'][0+(window - 1):])
    year.reset_index(drop=True, inplace=True)
    sample_list.insert(0, 'Year', year)

    for entry in columns:
        prev = mk_col_trend(data, 'NAME', entry, window, threshold)
        sample_list = pd.merge(sample_list, prev, on='Year', how='outer')

    return sample_list


merged_list_trend = merge_frame_trend(df, 30, 10)

merged_list_w30_md10 = merge_frame(df, 30, 10)
merged_list_w50_md10 = merge_frame(df, 50, 10)
merged_list_w30_md20 = merge_frame(df, 30, 20)
merged_list_w50_md20 = merge_frame(df, 50, 20)


'''
for parameter sen's slope
merged_list_w30_md10 = merge_frame(df, 30, 10)
merged_list_w50_md10 = merge_frame(df, 50, 10)
merged_list_w30_md20 = merge_frame(df, 30, 20)
merged_list_w50_md20 = merge_frame(df, 50, 20)

writer = pd.ExcelWriter('AllDataP4.xlsx', engine='xlsxwriter')
workbook = writer.book
header_format = workbook.add_format({'bold': True})
start_2_md10 = merged_list_w30_md10.shape[0]+3
start_2_md20 = merged_list_w30_md20.shape[0]+3

format1 = workbook.add_format({'font_color': '#006100'})  # green
format2 = workbook.add_format({'bg_color':   '#ffcccb', 'border': 1})  # red fill
format3 = workbook.add_format({'font_color': '#9C0006'})  # red
format4 = workbook.add_format({'bg_color':   '#C6EFCE', 'border': 1})  # green fill
format5 = workbook.add_format({'bg_color':   '#D3D3D3', 'border': 1})  # grey fill 

merged_list_w30_md10.to_excel(writer, sheet_name='Sheet1', index=False, startrow=1)
worksheet = writer.sheets['Sheet1']
worksheet.write(0, 0, "Window: 30, Missing value tolerance: 10%", header_format)
merged_list_w50_md10.to_excel(writer, sheet_name='Sheet1', index=False, startrow=1+(merged_list_w30_md10.shape[0]+3))
worksheet.write((merged_list_w30_md10.shape[0]+3), 0, "Window: 50, Missing value tolerance: 10%", header_format)
worksheet.conditional_format(2, 1, merged_list_w30_md10.shape[0]+1, merged_list_w30_md10.shape[1],
                             {'type': 'cell', 'criteria': 'equal to',
                             'value': '"Not enough data"', 'format': format3})
worksheet.conditional_format(2, 1, merged_list_w30_md10.shape[0]+1, merged_list_w30_md10.shape[1],
                             {'type': 'cell', 'criteria': 'not equal to',
                             'value': '"Not enough data"', 'format': format1})

worksheet.conditional_format(merged_list_w30_md10.shape[0]+5, 1,
                             start_2_md10+merged_list_w50_md10.shape[0]+1, merged_list_w30_md10.shape[1],
                             {'type': 'cell', 'criteria': 'not equal to',
                              'value': '"Not enough data"', 'format': format4})


merged_list_w30_md20.to_excel(writer, sheet_name='Sheet2', index=False, startrow=1)
worksheet = writer.sheets['Sheet2']
worksheet.write(0, 0, "Window: 30, Missing value tolerance: 20%", header_format)
merged_list_w50_md20.to_excel(writer, sheet_name='Sheet2', index=False, startrow=1+(merged_list_w30_md20.shape[0]+3))
worksheet.write((merged_list_w30_md20.shape[0]+3), 0, "Window: 50, Missing value tolerance: 20%", header_format)
worksheet.conditional_format(2, 1, merged_list_w30_md20.shape[0]+1, merged_list_w30_md20.shape[1],
                             {'type': 'cell', 'criteria': 'equal to',
                             'value': '"Not enough data"', 'format': format3})
worksheet.conditional_format(2, 1, merged_list_w30_md20.shape[0]+1, merged_list_w30_md20.shape[1],
                             {'type': 'cell', 'criteria': 'not equal to',
                             'value': '"Not enough data"', 'format': format1})


merged_list_trend.to_excel(writer, sheet_name='Trend', index=False, startrow=1)
worksheet = writer.sheets['Trend']
worksheet.conditional_format(2, 1, merged_list_trend.shape[0]+1, merged_list_trend.shape[1],
                             {'type': 'cell', 'criteria': 'equal to',
                             'value': '"no trend"', 'format': format5})
worksheet.conditional_format(2, 1, merged_list_trend.shape[0]+1, merged_list_trend.shape[1],
                             {'type': 'cell', 'criteria': 'equal to',
                             'value': '"increasing"', 'format': format4})
worksheet.conditional_format(2, 1, merged_list_trend.shape[0]+1, merged_list_trend.shape[1],
                             {'type': 'cell', 'criteria': 'equal to',
                             'value': '"decreasing"', 'format': format2})                             

writer.save()
'''


'''
worksheet.conditional_format(0, 0, 0, 5,
                             {'type': 'text', 'criteria': 'not containing',
                              'value': "99", 'format': format3})
worksheet.conditional_format(start_2_md10, 0, start_2_md10, 5,
                             {'type': 'text', 'criteria': 'not containing',
                              'value': "99", 'format': format3})

worksheet.conditional_format(0, 0, 0, 5,
                             {'type': 'text', 'criteria': 'not containing',
                              'value': "99", 'format': format3})
worksheet.conditional_format(start_2_md20, 0, start_2_md20, 5,
                             {'type': 'text', 'criteria': 'not containing',
                              'value': "99", 'format': format3})

worksheet.conditional_format(2, merged_list_w30_md10.shape[0]+1, 1, merged_list_w30_md10.shape[1],
                             {'type': 'cell', 'criteria': 'equal to',
                             'value': '"Not enough data"', 'format': format3})

worksheet.conditional_format(2, merged_list_w30_md10.shape[0]+1, 1, merged_list_w30_md10.shape[1],
                             {'type': 'cell', 'criteria': 'equal to',
                             'value': '"Not enough data"', 'format': format3})
'''
