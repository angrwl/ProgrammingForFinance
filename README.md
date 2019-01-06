# Programming For Finance 

The credit for these codes goes to youtube series **Programming for Finance** developed by **Sentdex** 
who taught me how to interpretate finance data and how to make use of modules such as `pandas, beautifulsoup, pickle` 
to make your life much easier while writing strategies. 

The link to his youtube series is: 

https://www.youtube.com/watch?v=2BrpKpWwT2A&list=PLQVvvaa0QuDcOdF96TBtRtuQksErCEBYZ 

## Advice 

I will advice you to only download by `py` files and now the `csv` files in the folder named `stocks_df` because those 
are the stock data for every **S&P500** stock and it has a large memory and when you will run by python files, you will download them 
yourself on your computer. 

If you do not want to download so many csv files, you can just get them straight from **yahoo api** 
by using `web.DataReader(ticker,'yahoo',start_date,end_date)` command which is written in one if not all of my files. 

Further more, when plotting **candlestick_ohlc** graphs, he uses module `matplotlib.finance` which has not depreceated, hence I would 
advice you to download (if not already done so) the module `mpl_finance` by doing the command `pip install mpl_finance` on the terminal 
of a windows computer. And then on py file, write `from mpl_finance import candlestick_ohlc`

## More Info

The folder named `Practices_few_episodes` is me myself trying to understand what is going on in his starting few episodes 

I hope his work helps you and motivates you to go into Algorithmic trading as it has to me. 
