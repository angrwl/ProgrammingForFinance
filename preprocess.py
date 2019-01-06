import numpy as np
import pandas as pd
import pickle
from collections import Counter


'''This sheet makes absolutely no sense to me ======================
    https://www.youtube.com/watch?v=zPp80YM2v7k&list=PLQVvvaa0QuDcOdF96TBtRtuQksErCEBYZ&index=11
'''
def process_data_for_labels(ticker = 'AAPL'):
    hm_days = 7;
    df = pd.read_csv('sp500_joined_closes.csv',parse_dates=True,index_col=0) #date is index
    tickers = df.columns.values
    df.fillna(0,inplace = True)  #replaces 'NaN' with 0

    for i in range(1,hm_days+1): #1 - 7
        '''You are trying to estimate the return of a stock ith day in the future
        by looking at change in price of today from ith day in the past i.e.
         price_2d_from_now = (past_2d_from_now_price - today_price)/today_price'''

        df['{}_{}d'.format(ticker,i)] = (df[ticker].shift(-i) - df[ticker]) / df[ticker] #gives a list

    #print(*[df['{}_{}d'.format(ticker,i)].head(20) for i in range(1,hm_days+1)])
    df.fillna(0,inplace = True)
    return tickers, df, hm_days
process_data_for_labels()

def buy_sell_hold(*args):
    cols = [c for c in args]
    requirement = 0.02
    for col in cols:
        if col > requirement:
            return 1
        if col < -requirement:
            return -1
        else:
            return 0

#print(buy_sell_hold(0.01,-0.03,0.1))

def extract_featuresets(ticker):
    tickers, df, hm_days = process_data_for_labels(ticker)

    df['{}_target'.format(ticker)] = list(map(buy_sell_hold,*[df['{}_{}d'.format(ticker,i)] for i in range(1,hm_days+1)]))
    vals = df['{}_target'.format(ticker)].values
    str_vals = (str(i) for i in vals)
    print('Data Spread: ', Counter(str_vals))
    df.fillna(0, inplace = True)

    df = df.replace([np.inf,-np.inf], np.nan);
    df.dropna(inplace=True) #it removes all rows with Nan in it

    df_vals = df[[ticker for ticker in tickers]].pct_change() #percentage change from yday value
    df_vals = df_vals.replace([np.inf,-np.inf],0);
    df_vals.fillna(0,inplace = True)

    X = df_vals.values  #values converts a dataFrame into numpy
    y = df['{}_target'.format(ticker)].values

    return X, y, df

print(extract_featuresets(ticker = 'AAPL'))
    #list1 = [('{}_{}d'.format(ticker,i)) for i in range(1,hm_days+1)]
    #list1.append('{}_target'.format(ticker))
    #print(list1)
    ##print(df[['{}_{}d'.format(ticker,i) for i in range(1,hm_days+1)].append('{}_target'.format(ticker))])
    #print(df[list1].tail(20))
#extract_featuresets(ticker = 'AAPL')






    #
