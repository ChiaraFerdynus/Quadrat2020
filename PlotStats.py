from cycler import cycler
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from openpyxl import load_workbook
import xlsxwriter

'''All this hard coded shit is so messy, my apologies'''
''' This script creates teh 3x3 plot (along with others) of the number of sites per year'''

BU = pd.read_excel('BU_stats.xlsx')
FU = pd.read_excel('FU_stats.xlsx')
OW = pd.read_excel('OW_stats.xlsx')

BU.set_index('Year', inplace=True)
FU.set_index('Year', inplace=True)
OW.set_index('Year', inplace=True)

# general plot showing the distribution of values
ax0 = BU['30w_20md'].plot()
ax0.grid()
ax0.set_ylabel('Number of sites with data')
# ax0.text(.1, .8, 'Total:\n' + str(int(BU['30w_20md'].sum())),
#          bbox={'facecolor': 'white', 'alpha': 1, 'pad': 10}, transform=ax0.transAxes)
plt.xlim(1472, 2020)
plt.ylim(0, 700)
plt.show()
# fig0 = ax0.get_figure()
# fig0.savefig('BU_30_20_all.png')
'''
# narrowing it down to the obvious peak
seg1 = BU['30w_10md'].loc[1900:2019]
seg1_1 = BU['30w_20md'].loc[1900:2019]
seg1_2 = BU['30w_25md'].loc[1900:2019]

# BREAK UP
ax30 = BU[['30w_10md', '30w_20md', '30w_25md']].loc[1860:2019].plot(color=['blue', 'red', 'green'])
ax30.legend(labels=['10%', '20%', '25%'], loc='upper left')
ax30.grid()
ax30.set_ylabel('Number of sites with data')
ax30.set_title('Breakup: 30 year window')
plt.xlim(1860, 2020)
plt.xticks([1860, 1900, 1940, 1980, 2020])
plt.show()
fig30 = ax30.get_figure()
fig30.savefig('BU_30w_line_log.png')

ax20 = BU[['20w_10md', '20w_20md', '20w_25md']].loc[1860:2019].plot(color=['blue', 'red', 'green'])
ax20.legend(labels=['10%', '20%', '25%'], loc='upper left')
ax20.grid()
ax20.set_ylabel('Number of sites with data')
ax20.set_title('Breakup: 20 year window')
plt.xlim(1860, 2020)
plt.xticks([1860, 1900, 1940, 1980, 2020])
plt.show()
fig20 = ax20.get_figure()
fig20.savefig('BU_20w_line_log.png')

ax50 = BU[['50w_10md', '50w_20md', '50w_25md']].loc[1860:2019].plot(color=['blue', 'red', 'green'])
ax50.legend(labels=['10%', '20%', '25%'], loc='upper left')
ax50.grid()
ax50.set_ylabel('Number of sites with data')
ax50.set_title('Breakup: 50 year window')
plt.xlim(1860, 2020)
plt.xticks([1860, 1900, 1940, 1980, 2020])
plt.show()
fig50 = ax50.get_figure()
fig50.savefig('BU_50w_line_narrow.png')

ax25 = BU[['50w_25md', '30w_25md', '20w_25md']].loc[1860:2019].plot(color=['magenta', 'cyan', 'black'])
ax25.legend(labels=['50 year window', '30 year window', '20 year window'], loc='upper left')
ax25.grid()
ax25.set_ylabel('Number of sites with data')
ax25.set_title('Breakup: 25% tolerance')
plt.show()
fig25 = ax25.get_figure()
fig25.savefig('BU_25md_line_narrow.png')

'''

'''
x_axis = range(1900, 2020)
y_axis = []
i = 0
for each in seg1:
    y_axis.append(each)

# fig1 = ax1.get_figure()
# fig1.savefig('BU_30_10_narrow.png')

# bar chart to show individual heights
segment2 = BU['30w_10md'].loc[1977:1995]
ax2 = segment2.plot.bar()
ax2.set_title('Number of data points per year (BU, 30w, 10md)')
ax2.set_ylabel('Data points')
totals = []
for i in ax2.patches:
    totals.append(i.get_height())

for i in ax2.patches:
    ax2.text(i.get_x()-.1, i.get_height()+4,
             str(int(i.get_height())), fontsize=7, color='black')

plt.show()

# fig = ax2.get_figure()
# fig.savefig('BU_30w_10md.png')
'''


'''
# FU
ax30 = FU[['30w_10md', '30w_20md', '30w_25md']].loc[1850:2019].plot(color=['blue', 'red', 'green'])
ax30.legend(labels=['10%', '20%', '25%'], loc='upper left')
ax30.grid()
ax30.set_ylabel('Number of sites with data')
ax30.set_title('Freezeup: 30 year window')
plt.show()
fig30 = ax30.get_figure()
fig30.savefig('FU_30w_narrow.png')

ax20 = FU[['20w_10md', '20w_20md', '20w_25md']].loc[1850:2019].plot(color=['blue', 'red', 'green'])
ax20.legend(labels=['10%', '20%', '25%'], loc='upper left')
ax20.grid()
ax20.set_ylabel('Number of sites with data')
ax20.set_title('Freezeup: 20 year window')
plt.show()
fig20 = ax20.get_figure()
fig20.savefig('FU_20w_narrow.png')

ax50 = FU[['50w_10md', '50w_20md', '50w_25md']].loc[1850:2019].plot(color=['blue', 'red', 'green'])
ax50.legend(labels=['10%', '20%', '25%'], loc='upper left')
ax50.grid()
ax50.set_ylabel('Number of sites with data')
ax50.set_title('Freezeup: 50 year window')
plt.show()
fig50 = ax50.get_figure()
fig50.savefig('FU_50w_narrow.png')

ax25 = FU[['50w_25md', '30w_25md', '20w_25md']].loc[1850:2019].plot(color=['magenta', 'cyan', 'black'])
ax25.legend(labels=['50 year window', '30 year window', '20 year window'], loc='upper left')
ax25.grid()
ax25.set_ylabel('Number of sites with data')
ax25.set_title('Freezeup: 25% tolerance')
plt.show()
fig25 = ax25.get_figure()
fig25.savefig('FU_25md_line_narrow.png')

'''


'''
# OPEN WATER

ax30 = OW[['30w_10md', '30w_20md', '30w_25md']].loc[1850:2019].plot(color=['blue', 'red', 'green'])
ax30.legend(labels=['10%', '20%', '25%'], loc='upper left')
ax30.grid()
ax30.set_ylabel('Number of sites with data')
ax30.set_title('Open water: 30 year window')
plt.show()
fig30 = ax30.get_figure()
fig30.savefig('OW_30w_line_1850_2019.png')

ax20 = OW[['20w_10md', '20w_20md', '20w_25md']].loc[1850:2019].plot(color=['blue', 'red', 'green'])
ax20.legend(labels=['10%', '20%', '25%'], loc='upper left')
ax20.grid()
ax20.set_ylabel('Number of sites with data')
ax20.set_title('Open water: 20 year window')
plt.show()
fig20 = ax20.get_figure()
fig20.savefig('OW_20w_line_1850_2019.png')

ax50 = OW[['50w_10md', '50w_20md', '50w_25md']].loc[1850:2019].plot(color=['blue', 'red', 'green'])
ax50.legend(labels=['10%', '20%', '25%'], loc='upper left')
ax50.grid()
ax50.set_ylabel('Number of sites with data')
ax50.set_title('Open water: 50 year window')
plt.show()
fig50 = ax50.get_figure()
fig50.savefig('OW_50w_line_1850_2019.png')

ax25 = OW[['50w_25md', '30w_25md', '20w_25md']].loc[1850:2019].plot(color=['magenta', 'cyan', 'black'])
ax25.legend(labels=['50 year window', '30 year window', '20 year window'], loc='upper left')
ax25.grid()
ax25.set_ylabel('Number of sites with data')
ax25.set_title('Open water: 25% tolerance')
plt.show()
fig25 = ax25.get_figure()
fig25.savefig('OW_25md_line_1850_2019.png')
'''
plt.rcParams['axes.prop_cycle'] = plt.cycler(color=["blue", "green", "red"])

fig, ax = plt.subplots(3, 3, figsize=(12, 10), sharex=True, sharey=True)
# BU 20 - 30 - 50
ax[0, 0].plot(range(1820, 2020), BU[['20w_10md', '20w_20md', '20w_25md']].loc[1820:2019])
ax[0, 0].grid()
ax[0, 0].set_title("Breakup", size=12.4)
ax[0, 0].set_ylabel('Number of sites with data')
ax[0, 0].text(.1, .7, '10%: ' + str(BU['20w_10md'].loc[1820:2019].sum())
              + '\n20%: ' + str(BU['20w_20md'].loc[1820:2019].sum())
              + '\n25%: ' + str(BU['20w_25md'].loc[1820:2019].sum()),
        bbox={'facecolor': 'white', 'alpha': 1, 'pad': 10}, transform=ax[0, 0].transAxes)

plt.xlim(1820, 2020)
plt.ylim(0, 850)
plt.xticks([1820, 1860, 1900, 1940, 1980, 2020])

ax[1, 0].plot(range(1820, 2020), BU[['30w_10md', '30w_20md', '30w_25md']].loc[1820:2019])
ax[1, 0].grid()
ax[1, 0].set_ylabel('Number of sites with data')
ax[1, 0].text(.1, .7, '10%: ' + str(int(BU['30w_10md'].loc[1820:2019].sum()))
              + '\n20%: ' + str(int(BU['30w_20md'].loc[1820:2019].sum()))
              + '\n25%: ' + str(int(BU['30w_25md'].loc[1820:2019].sum())),
        bbox={'facecolor': 'white', 'alpha': 1, 'pad': 10}, transform=ax[1, 0].transAxes)


ax[2, 0].plot(range(1820, 2020), BU[['50w_10md', '50w_20md', '50w_25md']].loc[1820:2019])
ax[2, 0].grid()
ax[2, 0].set_ylabel('Number of sites with data')
ax[2, 0].set_xlabel('Years')
ax[2, 0].text(.1, .7, '10%: ' + str(int(BU['50w_10md'].loc[1820:2019].sum()))
              + '\n20%: ' + str(int(BU['50w_20md'].loc[1820:2019].sum()))
              + '\n25%: ' + str(int(BU['50w_25md'].loc[1820:2019].sum())),
        bbox={'facecolor': 'white', 'alpha': 1, 'pad': 10}, transform=ax[2, 0].transAxes)


# FU 20 - 30 - 50
ax[0, 1].plot(range(1820, 2020), FU[['20w_10md', '20w_20md', '20w_25md']].loc[1820:2019])
ax[0, 1].grid()
ax[0, 1].set_title('Freezeup', size=12.4)
ax[0, 1].text(.1, .7, '10%: ' + str(int(FU['20w_10md'].loc[1820:2019].sum()))
              + '\n20%: ' + str(int(FU['20w_20md'].loc[1820:2019].sum()))
              + '\n25%: ' + str(int(FU['20w_25md'].loc[1820:2019].sum())),
        bbox={'facecolor': 'white', 'alpha': 1, 'pad': 10}, transform=ax[0, 1].transAxes)


ax[1, 1].plot(range(1820, 2020), FU[['30w_10md', '30w_20md', '30w_25md']].loc[1820:2019])
ax[1, 1].grid()
ax[1, 1].text(.1, .7, '10%: ' + str(int(FU['30w_10md'].loc[1820:2019].sum()))
              + '\n20%: ' + str(int(FU['30w_20md'].loc[1820:2019].sum()))
              + '\n25%: ' + str(int(FU['30w_25md'].loc[1820:2019].sum())),
        bbox={'facecolor': 'white', 'alpha': 1, 'pad': 10}, transform=ax[1, 1].transAxes)


ax[2, 1].plot(range(1820, 2020), FU[['50w_10md', '50w_20md', '50w_25md']].loc[1820:2019])
ax[2, 1].grid()
ax[2, 1].set_xlabel('Years')
ax[2, 1].legend(labels=['10%', '20%', '25%'], bbox_to_anchor=(0, -.08, 1, -.08), ncol=3, mode='expand', fontsize=12.4)
ax[2, 1].text(.1, .7, '10%: ' + str(int(FU['50w_10md'].loc[1820:2019].sum()))
              + '\n20%: ' + str(int(FU['50w_20md'].loc[1820:2019].sum()))
              + '\n25%: ' + str(int(FU['50w_25md'].loc[1820:2019].sum())),
        bbox={'facecolor': 'white', 'alpha': 1, 'pad': 10}, transform=ax[2, 1].transAxes)


# OW 20 - 30 - 50
ax[0, 2].plot(range(1820, 2020), OW[['20w_10md', '20w_20md', '20w_25md']].loc[1820:2019])
ax[0, 2].grid()
ax[0, 2].set_title('Open Water Days', size=12.4)
ax[0, 2].text(1.06, 0.24, "20 Year Window", size=12.4, verticalalignment='bottom', horizontalalignment='right',
         transform=ax[0, 2].transAxes, rotation=-90)
ax[0, 2].text(.1, .7, '10%: ' + str(OW['20w_10md'].loc[1820:2019].sum())
              + '\n20%: ' + str(OW['20w_20md'].loc[1820:2019].sum())
              + '\n25%: ' + str(OW['20w_25md'].loc[1820:2019].sum()),
        bbox={'facecolor': 'white', 'alpha': 1, 'pad': 10}, transform=ax[0, 2].transAxes)


ax[1, 2].plot(range(1820, 2020), OW[['30w_10md', '30w_20md', '30w_25md']].loc[1820:2019])
ax[1, 2].grid()
ax[1, 2].text(1.06, 0.24, "30 Year Window", size=12.4, verticalalignment='bottom', horizontalalignment='right',
         transform=ax[1, 2].transAxes, rotation=-90)
ax[1, 2].text(.1, .7, '10%: ' + str(int(OW['30w_10md'].loc[1820:2019].sum()))
              + '\n20%: ' + str(int(OW['30w_20md'].loc[1820:2019].sum()))
              + '\n25%: ' + str(int(OW['30w_25md'].loc[1820:2019].sum())),
        bbox={'facecolor': 'white', 'alpha': 1, 'pad': 10}, transform=ax[1, 2].transAxes)


ax[2, 2].plot(range(1820, 2020), OW[['50w_10md', '50w_20md', '50w_25md']].loc[1820:2019])
ax[2, 2].grid()
ax[2, 2].set_xlabel('Years')
ax[2, 2].text(1.06, 0.24, "50 Year Window", size=12.4, verticalalignment='bottom', horizontalalignment='right',
         transform=ax[2, 2].transAxes, rotation=-90)
ax[2, 2].text(.1, .7, '10%: ' + str(int(OW['50w_10md'].loc[1820:2019].sum()))
              + '\n20%: ' + str(int(OW['50w_20md'].loc[1820:2019].sum()))
              + '\n25%: ' + str(int(OW['50w_25md'].loc[1820:2019].sum())),
        bbox={'facecolor': 'white', 'alpha': 1, 'pad': 10}, transform=ax[2, 2].transAxes)


'''
fig, ax = plt.subplots(3, 3, sharex=True)
ax[0, 0] = BU[['20w_10md', '20w_20md', '20w_25md']].loc[1860:2019].plot(color=['blue', 'red', 'green'])
ax[0, 0].legend(labels=['10%', '20%', '25%'], loc='upper left')
ax[0, 0].grid()
ax[0, 0].set_ylabel('Number of sites with data')
ax[0, 0].set_title('Breakup: 20 year window')
plt.xlim(1860, 2020)
plt.xticks([1860, 1900, 1940, 1980, 2020])

ax[0, 1] = BU[['30w_10md', '30w_20md', '30w_25md']].loc[1860:2019].plot(color=['blue', 'red', 'green'])
ax[0, 1].legend(labels=['10%', '20%', '25%'], loc='upper left')
ax[0, 1].grid()
ax[0, 1].set_ylabel('Number of sites with data')
ax[0, 1].set_title('Breakup: 30 year window')
plt.xlim(1860, 2020)
plt.xticks([1860, 1900, 1940, 1980, 2020])

ax[0, 2] = BU[['50w_10md', '50w_20md', '50w_25md']].loc[1860:2019].plot(color=['blue', 'red', 'green'])
ax[0, 2].legend(labels=['10%', '20%', '25%'], loc='upper left')
ax[0, 2].grid()
ax[0, 2].set_ylabel('Number of sites with data')
ax[0, 2].set_title('Breakup: 50 year window')
plt.xlim(1860, 2020)
plt.xticks([1860, 1900, 1940, 1980, 2020])


fig.savefig('3x3_1820_withXY_totals.png')
'''
plt.show()

