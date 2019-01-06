import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

'''Importing data from my old py file although infact i didn't use it in the end'''
import scraping as sp

'''===================================================https://youtu.be/PxUzcDJBEZ4========================================================'''

def visualize_data():
    '''Objective of this function is to calculate correlation between each stock and the
    draw a heatmap to visualize the data. More for asthetics purposes'''

    if not os.path.exists('sp500_correlation.csv'):
        df = pd.read_csv('sp500_joined_closes.csv',parse_dates=True,index_col=0); #this sets date as index and removes 0,1,..,504
        df_corr = df.corr()  #looks at correlation between different Adj Close data
        df_corr.to_csv('sp500_correlation.csv') #save a csv file
    else:
        df_corr = pd.read_csv('sp500_correlation.csv',parse_dates=True,index_col=0)

    #print(df_corr)
    data = df_corr.values  #represents the data as a numpy matrix instead of dataFrame layout
    #print(data[:5])

    '''Time to created our own heatmap - since there is not an inbuilt function
    in matplotlib, we have to kind of create our own'''

    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)  # 1 by 1 plot with this graph at position 1

    heatmap = ax.pcolor(data,cmap = plt.cm.RdYlGn); #here R=red, Y=yellow, G=green i.e colors for positive to negative sp500_correlation
    fig.colorbar(heatmap) #colorbar on the side which depicts our ranges
    rangeX = np.arange(data.shape[0])+0.5  #[0.5,1.5,2.5,.......,504.5]
    rangeY = np.arange(data.shape[1])+0.5   #[0.5,1.5,2.5,.......,504.5]
    ax.set_xticks(rangeX,minor = False)  #gives small ticks on x-axis every 0.5 etc and we want to remove the minor ticks (hence false)
    ax.set_yticks(rangeY,minor = False)  # same as above for y axis
    ax.invert_yaxis() #remove gap at the top of a matplotlib graph
    ax.xaxis.tick_top() #moves x axis from the bottom to the top of the chart

    '''Below are the x and y labels which are ought to be identical
    because we are looking at correlation tables but for completeness,
    let's define them as two separate variables anyway'''

    column_labels = df_corr.columns #first row essentially
    row_labels = df_corr.index #first column which is index

    ax.set_xticklabels(column_labels)
    ax.set_yticklabels(row_labels)
    plt.xticks(rotation = 90) #rotation the stock tickers 90* so that they are less squashed
    heatmap.set_clim(-1,1) #min and max of colorbar and since correlation only goes between (-1,1)
    plt.tight_layout()
    plt.title('Correlation heatmap of S&P500 stocks')
    #plt.savefig()
    plt.show()

    '''There is so much data, that to appreciate the graph fully, you need to
    zoom in at particular points '''

visualize_data()
