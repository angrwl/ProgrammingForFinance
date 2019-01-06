import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import os
from dateutil.relativedelta import relativedelta
import pandas_datareader.data as web

plt.style.use('ggplot')

end = dt.datetime.today()   #to get todays date
end = end.date()  # to remove unnecessary hours, mins, seconds, ms
start = end + relativedelta(months = -6, days = 0)  #how many months/days we want to go back from current date
# relativedelta is very useful because it only includes business days

stock = 'AAPL'
data = web.DataReader(stock,'yahoo',start,end)
'''print(data.head())''' #head gives you first 5 data and tail gives you last 5 data
'''data.to_csv('{}.csv'.format(stock))''' #to create a csv file with name of the stock
'''This is to read csv file in python using pandas'''
df = pd.read_csv('{}.csv'.format(stock), parse_dates=True, index_col=0) #index_col = 0 removes unnecessary first column
# print(df.head())
# print(df[['Open','Close']].head()) printing only two rows and there first 5 values each

df['Adj Close'].plot()
plt.show()
