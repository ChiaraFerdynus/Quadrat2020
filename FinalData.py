import pymannkendall as MK
import pandas as pd
import numpy as np
from openpyxl import load_workbook
import xlsxwriter

'''
This script creates data sets of Q, Trend and Z value of BU, FU and OW
'''

FU = pd.read_excel("NewFormat_Freezeup.xlsx")
BU = pd.read_excel("NewFormat_Breakup.xlsx")
OW = pd.read_excel("NewFormat_OW.xlsx")

columns = OW.columns[1:]  # drop first one (bc it is the Year)

# determine percentage of missing values
def missing_values(snip, window, threshold):
    missing = snip.isnull().sum()
    percent = (missing/window)*100
    if percent > threshold:
        return 0
    else:
        # print(missing, percent)
        return 1


# determine Q value for single location
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

    # print(stats_list2)
    return stats_list2


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

    # print(stats_list2)
    return stats_list2


def mk_col_z(Data, YearCol, LocCol, window, TH, alpha=0.1):
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
            stats_list2[LocCol].values[instance] = snip_test.z

        else:
            stats_list2[LocCol].values[instance] = 'Not enough data'

    # print(stats_list2)
    return stats_list2

# create complete data frame of Q values for all locations
def merge_frame_slope(data, window, threshold):
    sample_list = pd.DataFrame(index=range(0, data.shape[0] - (window - 1)))
    year = pd.Series(data['YEAR'][0+(window - 1):])
    year.reset_index(drop=True, inplace=True)
    sample_list.insert(0, 'Year', year)

    for entry in columns:       # iterating over the locations
        prev = mk_col_slope(data, 'YEAR', entry, window, threshold)
        sample_list = pd.merge(sample_list, prev, on='Year', how='outer')

    return sample_list


def merge_frame_trend(data, window, threshold):
    sample_list = pd.DataFrame(index=range(0, data.shape[0] - (window - 1)))
    year = pd.Series(data['YEAR'][0+(window - 1):])
    year.reset_index(drop=True, inplace=True)
    sample_list.insert(0, 'Year', year)

    for entry in columns:
        prev = mk_col_trend(data, 'YEAR', entry, window, threshold)
        sample_list = pd.merge(sample_list, prev, on='Year', how='outer')

    return sample_list


def merge_frame_Z(data, window, threshold):
    sample_list = pd.DataFrame(index=range(0, data.shape[0] - (window - 1)))
    year = pd.Series(data['YEAR'][0+(window - 1):])
    year.reset_index(drop=True, inplace=True)
    sample_list.insert(0, 'Year', year)

    for entry in columns:
        prev = mk_col_z(data, 'YEAR', entry, window, threshold)
        sample_list = pd.merge(sample_list, prev, on='Year', how='outer')

    return sample_list

# --> these are all the parameter sets that have to be calculated for Fu, BU and OW (I did it manually step by step as it took quite long to run one set already)
# 30 year window, 10% tolerance

# 30 year window, 20% tolerance

# 30 year window, 25% tolerance

# 20 year window, 10% tolerance

# 20 year window 20% tolerance

# 20 year window, 25% tolerance

# 50 year window 10% tolerance

# 50 year window 20% tolerance

# 50 year window 25% tolerance

# --> this is how data frames from python can be stored in Excel
'''
writer = pd.ExcelWriter('Z_FU_50w_25md.xlsx', engine='xlsxwriter')
workbook = writer.book
Z_FU_50w_25md.to_excel(writer, index=False)
writer.save()
writer.close()

'''
