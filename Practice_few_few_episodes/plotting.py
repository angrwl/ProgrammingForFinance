import datetime as dt
import matplotlib.pyplot as plt
from mpl_finance import candlestick_ohlc   #old matplotlib.finance has depreceated
import matplotlib.dates as mdates
import pandas as pd
import os
from dateutil.relativedelta import relativedelta
import pandas_datareader.data as web

plt.style.use('ggplot')

df = pd.read_csv('AAPL.csv',parse_dates=True,index_col=0);
df['100ma'] = df['Close'].rolling(window = 10).mean() #calculating mean
#print(df.head())
# df.dropna(inplace = True) #to remove the first few rows where df['100ma'] = NaN

df_ohlc = df['Adj Close'].resample('10D').ohlc()
'''df_ohlc = df['Adj Close'].resample('10D').ohlc() is when you want prices every 10 days (10D)'''
print(df_ohlc.head()) #prints first 5
df_volume = df['Volume'].resample('10D').sum()

df_ohlc.reset_index(inplace = True)

'''we earlier set dates = index by doing
index_col = 0 in df, and now we want index to be normal again so we do
reset stuff - however if we just set data['Date'] = data.index
and hashtag the reset code, it works normally too'''

df_ohlc['Date'] = df_ohlc['Date'].map(mdates.date2num) #converts into format understood by matplotlib

ax1 = plt.subplot2grid((6,1), (0,0), rowspan=5, colspan=1) #second entry is where to start it off
ax2 = plt.subplot2grid((6,1), (5,0), rowspan=5, colspan=1,sharex = ax1) # sharex: if ax1 is zoomed, then so will ax2
ax1.xaxis_date()

candlestick_ohlc(ax1,df_ohlc.values, width=7, colorup='g')  # df.index is date and we have assigned it as index before
ax1.plot(df.index, df['100ma'])
ax2.fill_between(df_volume.index.map(mdates.date2num),df_volume.values,0,color = 'blue');
# df_volume.index = dates since we didnt reset index for df_volume (only df_ohlc)
plt.show()
