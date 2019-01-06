import bs4 as bs
import datetime as dt
import os #to save new directories for us in python
import pandas as pd
import pandas_datareader.data as web
import requests
import pickle   #saves the tickers in a file so we do not have to extract data from web everytime which takes memory


'''=======================================Purpose of this py file is to scrape the list of S&P 500 companies tickers from WikiPedia page==================================='''

def save_sp500_ticker():
    resp = requests.get('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'); #this gives us permission to access the data
    soup = bs.BeautifulSoup(resp.text,'lxml')  #this allows us to get the text of the resp (hence resp.text) and have it with parser = 'lxml'
    # I have seen people use 'html' instead of 'lxml'
    table = soup.find('table',{'class':"wikitable sortable"}); #find just finds the first table with this class which satisfies this condition
    tickers = [];
    for row in table.findAll('tr')[1:]: #findAll finds all tags with tr. we purposely added [1:] because first row is just heading and we removed it
        ticker = row.findAll('td')[0].text #only care about ticker which is in first column
        tickers.append(ticker)

    '''In python, tickers like BKB.K needs to be saved as BKB-K or else you get error'''
    for tick in tickers:
        if '.' in tick:
            index = tickers.index(tick) #getting tickers index
            tick = tick.replace('.','-') #replacing '.' with '-'
            tickers[index] = tick #adding new ticker name

    '''This allows you not to having search WikiPedia again and again'''
    with open('sp500tickers.pickle','wb') as file: #lets you create a pickle file (file) and write (wb) in it
        pickle.dump(tickers,file) #you put ticker in it
    #print(tickers)
    return tickers
    
'''when you trying to create pickle file for the first time, uncomment the function line below save_sp500_ticker()'''
#save_sp500_ticker();

def get_data(reload_sp500 = False):
    if reload_sp500: #if reload_sp500 is true, then we need to create tickers by doing above function
        tickers = save_sp5save_sp500_ticker();
    else:
        with open('sp500tickers.pickle','rb') as file:  #we will read the pickle file directly
            tickers = pickle.load(file); #loads pickle file

    '''Now we will create a folder (directory) to save all the prices of all the stocks in S&P 500'''

    if not os.path.exists('stock_dfs'):  #if folder doesn't exists, this creates it
        os.makedirs('stock_dfs')

    start = dt.datetime(2002,1,1);
    end = end = dt.datetime.today()   #to get todays date
    end = end.date();

    for ticker in tickers:
        if not os.path.exists('stock_dfs/{}.csv'.format(ticker)):
            print(ticker)
            df = web.DataReader(ticker,'yahoo',start,end);
            df.to_csv('stock_dfs/{}.csv'.format(ticker));
        else:
            print('Already have {}'.format(ticker));

#get_data()

def compile():
    '''Objective of this function is to compile all the Adj Close prices of each stock in one csv file'''

    if not os.path.exists('sp500_joined_closes.csv'):
        with open('sp500tickers.pickle','rb') as file:  #we will read the pickle file directly
            tickers = pickle.load(file);

        main_df = pd.DataFrame();  #create an empty dict

        for count,ticker in enumerate(tickers):
            df = pd.read_csv('stock_dfs/{}.csv'.format(ticker))[['Date','Adj Close']] #only extracting two columns
            df.set_index('Date',inplace=True)  #removes initial index col 0,1,2,....,504
            df.rename(columns = {'Adj Close':'{}'.format(ticker)},inplace = True) #without inplace = true, name won't change

            '''Placing prices in one dict called main_df'''
            if main_df.empty:
                main_df = df
            else:
                main_df = main_df.join(df,how = 'outer')

            if count%10 ==0:
                print(count)

        print(main_df.head(20))
        main_df.to_csv('sp500_joined_closes.csv');
        return main_df

    else:
        print('The csv file sp500_joined_closes.csv already exists so no need to compile\n')
        main_df = pd.read_csv('sp500_joined_closes.csv',parse_dates=True,index_col=0);
        print(main_df.head(20));

#compile()
