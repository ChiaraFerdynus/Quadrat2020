import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from openpyxl import load_workbook
import xlsxwriter
import Plot2

''' BU '''
BU_Q = ['merged_BU_30w_10md', 'merged_BU_30w_20md', 'merged_BU_30w_25md',
        'merged_BU_20w_10md', 'merged_BU_20w_20md', 'merged_BU_20w_25md',
        'merged_BU_50w_10md', 'merged_BU_50w_20md', 'merged_BU_50w_25md']

FU_Q = ['merged_FU_30w_10md', 'merged_FU_30w_20md', 'merged_FU_30w_25md',
        'merged_FU_20w_10md', 'merged_FU_20w_20md', 'merged_FU_20w_25md',
        'merged_FU_50w_10md', 'merged_FU_50w_20md', 'merged_FU_50w_25md']

OW_Q = ['merged_OW_30w_10md', 'merged_OW_30w_20md', 'merged_OW_30w_25md',
        'merged_OW_20w_10md', 'merged_OW_20w_20md', 'merged_OW_20w_25md',
        'merged_OW_50w_10md', 'merged_OW_50w_20md', 'merged_OW_50w_25md']

for sheet in OW_Q:
    name = sheet[-12:]
    df = pd.read_excel(sheet + '.xlsx')
    df = df.set_index('Year')

    df_info = pd.read_excel('NewInfo1.xlsx')
    df_info = df_info.set_index('Unnamed: 0')
    df_infoT = df_info.transpose()

    groups = df_infoT.groupby('country').groups     # groups['CANADA'][1] = index of second element in Canada list
    countries = [*groups]   # list of countries

    America = ['CANADA', 'UNITED STATES']
    Europe = ['AUSTRIA-HUNGARY', 'FINLAND', 'GERMANY', 'HUNGARY', 'NORWAY', 'EUROPEAN RUSSIA', 'SWEDEN', 'SWITZERLAND']
    Asia = ['CHINA', 'JAPAN', 'ASIAN RUSSIA']
    year = pd.Series(range(1820, 2020))

    america_df = pd.DataFrame(index=range(0, 200))
    america_df.insert(0, 'Year', year)
    america_df = america_df.set_index('Year')

    europe_df = pd.DataFrame(index=range(0, 200))
    europe_df.insert(0, 'Year', year)
    europe_df = europe_df.set_index('Year')

    asia_df = pd.DataFrame(index=range(0, 200))
    asia_df.insert(0, 'Year', year)
    asia_df = asia_df.set_index('Year')

    for country in America:
        for index in groups[country]:
            snip = df[index].loc[1820:].copy()
            america_df[index] = snip
    Plot2.bar_plot(america_df, 'America', name)

    for country in Europe:
        for index in groups[country]:
            snip = df[index].loc[1820:].copy()
            europe_df[index] = snip
    Plot2.bar_plot(europe_df, 'Europe', name)

    for country in Asia:
        for index in groups[country]:
            snip = df[index].loc[1820:].copy()
            asia_df[index] = snip
    Plot2.bar_plot(asia_df, 'Asia', name)

    Plot2.bar_plot(df, 'Global', name)


# writer = pd.ExcelWriter('BU_asia_df.xlsx', engine='xlsxwriter')
# workbook = writer.book
# asia_df.to_excel(writer)
# writer.save()
# writer.close()

