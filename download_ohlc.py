# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 22:34:37 2016

@author: Tayari
"""

from pandas.io.data import DataReader
import pandas as pd


def download_ohlc(tickers, start, end):
    #ohlc =  pd.DataFrame(columns=tickers)
    ohlc = {}
    for Symbol in tickers.iteritems():
        print ('Downloading data from Yahoo for %s Symbol', Symbol)
        data = DataReader(Symbol[1], 'yahoo', start, end)
        for item in ['Open', 'High', 'Low']:
            data[item] = data[item] * data['Adj Close'] / data['Close']
        data.rename(columns={'Open': 'open', 'High': 'high', 'Low': 'low','Adj Close': 'close', 'Volume': 'volume', 'Close':'Close'},inplace=True)
        data.drop(['Close'], axis=1,inplace=True)
        ohlc[Symbol[1]] = data
    print ('Finished downloading data')
    return ohlc