import pymannkendall as MK
import pandas as pd
import numpy as np
from openpyxl import load_workbook
import xlsxwriter

FU = pd.read_excel("NewFormat_Freezeup.xlsx")
BU = pd.read_excel("NewFormat_Breakup.xlsx")
OW = pd.read_excel("NewFormat_OW.xlsx")

columns = OW.columns[1:]  # drop first one (bc it is the Year)


def missing_values(snip, window, threshold):
    missing = snip.isnull().sum()
    percent = (missing/window)*100
    if percent > threshold:
        return 0
    else:
        # print(missing, percent)
        return 1


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


def merge_frame_slope(data, window, threshold):
    sample_list = pd.DataFrame(index=range(0, data.shape[0] - (window - 1)))
    year = pd.Series(data['YEAR'][0+(window - 1):])
    year.reset_index(drop=True, inplace=True)
    sample_list.insert(0, 'Year', year)

    for entry in columns:
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


# 30 year window, 10% tolerance

# 30 year window, 20% tolerance

# 30 year window, 25% tolerance

# 20 year window, 10% tolerance

# 20 year window 20% tolerance

# 20 year window, 25% tolerance

# 50 year window 10% tolerance

# 50 year window 20% tolerance

# 50 year window 25% tolerance

'''
writer = pd.ExcelWriter('Z_FU_50w_25md.xlsx', engine='xlsxwriter')
workbook = writer.book
Z_FU_50w_25md.to_excel(writer, index=False)
writer.save()
writer.close()

'''
