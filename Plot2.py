import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from openpyxl import load_workbook
import xlsxwriter


def bar_plot(dftrial, region, xl_name):
    # dftrial = pd.read_excel(xl_name+'.xlsx')
    dftrial = dftrial.replace(to_replace='Not enough data', value=np.nan, regex=True)
    cols = dftrial.columns
    # standard = dftrial[cols[1:]].describe()

    df_new = pd.DataFrame(index=range(0, 200), columns=['warming1', 'warming2', 'warming3', 'warming4', 'warming5',
                                                        'noTrend', 'cooling1', 'cooling2', 'cooling3', 'cooling4', 'cooling5'])
    # year = pd.Series(dftrial['Year'].loc[348:])
    # year.reset_index(drop=True, inplace=True)
    year = pd.Series(range(1820, 2020))
    df_new.insert(0, 'Year', year)
    # df_new.insert(0, 'Year_group', year)
    df_new = df_new.set_index('Year')

    # dftrial = dftrial.set_index('Year')
    totals = dftrial.count(axis=1)  # number of non NaN values in each row (each year)
    totals = totals.loc[1820:]

    dfTrial_trans = dftrial.loc[1820:].transpose()
    year_cols = dfTrial_trans.columns

    '''
    get count of number of non NaN
    create new DF with this size OR add to df IF value is between so and so
    calculate percentages directly and transfer to new DF
    '''

    for col in year_cols:
        warming1 = 0
        warming2 = 0
        warming3 = 0
        warming4 = 0
        warming5 = 0
        cooling1 = 0
        cooling2 = 0
        cooling3 = 0
        cooling4 = 0
        cooling5 = 0
        noTrend = 0
        current_total = dfTrial_trans[col].count().sum()
        current_year = dfTrial_trans[col].tolist()
        for val in current_year:
            if 0 < val <= 0.25:
                warming1 = warming1 + 1
            if 0.25 < val <= 0.5:
                warming2 = warming2 + 1
            if 0.5 < val <= 1:
                warming3 = warming3 + 1
            if 1 < val <= 1.5:
                warming4 = warming4 + 1
            if val > 1.5:
                warming5 = warming5 + 1
            if 0 > val >= -0.25:
                cooling1 = cooling1 + 1
            if -0.25 > val >= -0.5:
                cooling2 = cooling2 + 1
            if -.5 > val >= -1:
                cooling3 = cooling3 + 1
            if -1 > val >= -1.5:
                cooling4 = cooling4 + 1
            if val < -1.5:
                cooling5 = cooling5 + 1
            if val == 0:
                noTrend = noTrend + 1

        if current_total != 0:
            cooling1 = (cooling1 / current_total) * 100
            cooling2 = (cooling2 / current_total) * 100
            cooling3 = (cooling3 / current_total) * 100
            cooling4 = (cooling4 / current_total) * 100
            cooling5 = (cooling5 / current_total) * 100
            noTrend = (noTrend / current_total) * 100
            warming1 = (warming1 / current_total) * 100
            warming2 = (warming2 / current_total) * 100
            warming3 = (warming3 / current_total) * 100
            warming4 = (warming4 / current_total) * 100
            warming5 = (warming5 / current_total) * 100
        if current_total == 0:
            noTrend = 100

        df_new['cooling1'][col] = cooling1
        df_new['cooling2'][col] = cooling2
        df_new['cooling3'][col] = cooling3
        df_new['cooling4'][col] = cooling4
        df_new['cooling5'][col] = cooling5
        df_new['noTrend'][col] = noTrend
        df_new['warming1'][col] = warming1
        df_new['warming2'][col] = warming2
        df_new['warming3'][col] = warming3
        df_new['warming4'][col] = warming4
        df_new['warming5'][col] = warming5

    dftotals = pd.DataFrame(index=range(1820, 2020))
    dftotals.insert(0, 'Totals', totals)
    '''
    # number of non NaN per year
    ax0 = dftotals['Totals'].plot()
    ax0.set_title('Number of non NaN per Year')
    plt.xlim(1820, 2020)
    plt.xticks([1820, 1860, 1900, 1940, 1980, 2020])
    plt.ylim(0, 830)
    plt.show()
    '''
    warming1_vals = np.array(df_new['warming1'].values.tolist())
    warming2_vals = np.array(df_new['warming2'].values.tolist())
    warming3_vals = np.array(df_new['warming3'].values.tolist())
    warming4_vals = np.array(df_new['warming4'].values.tolist())
    warming5_vals = np.array(df_new['warming5'].values.tolist())
    noTrend_vals = np.array(df_new['noTrend'].values.tolist())

    cooling1_vals = np.array(df_new['cooling1'].values.tolist())
    cooling2_vals = np.array(df_new['cooling2'].values.tolist())
    cooling3_vals = np.array(df_new['cooling3'].values.tolist())
    cooling4_vals = np.array(df_new['cooling4'].values.tolist())
    cooling5_vals = np.array(df_new['cooling5'].values.tolist())

    fig, ax1 = plt.subplots(figsize=(10, 9))
    N = len(warming1_vals)
    ind = np.arange(N)
    ind = range(1820, 2020)
    width = 1
    p1 = plt.bar(ind, warming5_vals, width, color='darkred')
    p2 = plt.bar(ind, warming4_vals, width, bottom=warming5_vals, color='firebrick')
    p3 = plt.bar(ind, warming3_vals, width,
                 bottom=[sum(x) for x in zip(warming4_vals, warming5_vals)], color='indianred')
    p4 = plt.bar(ind, warming2_vals, width,
                 bottom=[sum(x) for x in zip(warming3_vals, warming4_vals, warming5_vals)],
                 color='salmon')
    p5 = plt.bar(ind, warming1_vals, width,
                 bottom=[sum(x) for x in zip(warming2_vals, warming3_vals, warming4_vals, warming5_vals)],
                 color='lightsalmon')
    p6 = plt.bar(ind, noTrend_vals, width,
                 bottom=[sum(x) for x in zip(warming1_vals, warming2_vals, warming3_vals, warming4_vals, warming5_vals)],
                 color='white')
    p7 = plt.bar(ind, cooling1_vals, width,
                 bottom=[sum(x) for x in zip(noTrend_vals, warming1_vals, warming2_vals, warming3_vals, warming4_vals, warming5_vals)],
                 color='paleturquoise')
    p8 = plt.bar(ind, cooling2_vals, width,
                 bottom=[sum(x) for x in zip(cooling1_vals, noTrend_vals, warming1_vals, warming2_vals, warming3_vals, warming4_vals, warming5_vals)],
                 color='lightskyblue')
    p9 = plt.bar(ind, cooling3_vals, width,
                 bottom=[sum(x) for x in zip(cooling2_vals, cooling1_vals, noTrend_vals, warming1_vals, warming2_vals, warming3_vals, warming4_vals, warming5_vals)],
                 color='skyblue')
    p10 = plt.bar(ind, cooling4_vals, width,
                 bottom=[sum(x) for x in zip(cooling3_vals, cooling2_vals, cooling1_vals, noTrend_vals, warming1_vals, warming2_vals, warming3_vals, warming4_vals, warming5_vals)],
                 color='steelblue')
    p11 = plt.bar(ind, cooling5_vals, width,
                 bottom=[sum(x) for x in zip(cooling4_vals, cooling3_vals, cooling2_vals, cooling1_vals, noTrend_vals, warming1_vals, warming2_vals, warming3_vals, warming4_vals, warming5_vals)],
                 color='darkblue')
    plt.xlim(1819, 2020)
    plt.xticks(range(1820, 2021, 20))
    plt.ylabel('Percentage', fontsize=11)
    plt.xlabel('Year', fontsize=11)
    plt.legend(labels=['>1.5', '1/1.5', '.5/1', '.25/.5', '0/.25',
                       '0', '-.25/0', '-.5/-.25', '-1/-.5', '-1.5/-1', '<-1.5'], bbox_to_anchor=(-0.1, -.025, 1.2, -.025),
               ncol=11, mode='expand', fontsize=11)

    ax2 = ax1.twinx()
    plt.plot(dftotals['Totals'], linewidth=2, color='black')
    plt.ylim(0, 830)
    plt.ylabel('Number of sites with data', fontsize=11)
    plt.show()

    fig = ax1.get_figure()
    fig.savefig(region + xl_name[-12:] + '.png')
