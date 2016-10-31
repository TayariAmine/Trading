# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 22:33:26 2016

@author: Tayari
"""

import numpy  as np
import pandas as pd  
import math as m






#Moving Average  
def MA(df, n):  
    MA = pd.Series(pd.rolling_mean(df['close'], n), name = 'MA_' + str(n))  
    df = df.join(MA)  
    return df
# simple moving average change    
def SMAChange(df,n):
    C = df['close'] 
    MA = pd.rolling_mean(df['close'], n)
    SMAChange = pd.Series(100*(C-MA)/MA, name = 'SMAChange_' + str(n))
    df = df.join(SMAChange)
    return df


#Exponential Moving Average  , pandas implementation
def PD_EMA(df, n):  
    EMA = pd.Series(pd.ewma(df['close'], span = n, min_periods = n - 1), name = 'EMA_' + str(n))  
    df = df.join(EMA)  
    return df
#Exponential Moving Average
def ExpMA(df,n):
    EMA = [ema(df['close'][:i], n) for i in range(len(df['close']))]
    EMA_S = pd.Series([ema(df['close'][:i], n) for i in range(len(df['close']))], name = 'EMA_' + str(n), index=df.index)
    df = df.join(EMA_S)
    return df

#Volume Exponential Moving Average
def VWExpMA(df,n):
    VWEMA = [vwema(df['close'][:i],df['volume'][:i], n) for i in range(len(df['close']))]
    VEMA = [ema(df['volume'][:i], n) for i in range(len(df['volume']))]
    with np.errstate(divide='ignore'):
         VW=pd.Series(np.divide(np.asarray(VWEMA), np.asarray(VEMA)), name = 'VWEMA_' + str(n),  index=df.index)
    df = df.join(VW)
    return df

#Volume weighted Exponential Moving Average          
def vwema(data,volume,  window):
    c = 2.0 / (window + 1)
    if len(data) < window:
        current_ema =  0
    else:
        current_ema = data[-window]*volume[-window]
        for vp in data[-window+1:]*volume[-window+1:]:
            current_ema = (c * vp) + ((1 - c) * current_ema)
    return current_ema  
#Exponential Moving Average          
def ema(data, window):
    c = 2.0 / (window + 1)
    if len(data) < window:
        current_ema =  0
    else:
        current_ema = data[-window]
        for value in data[-window+1:]:
            current_ema = (c * value) + ((1 - c) * current_ema)
    return current_ema   

#Momentum  
def MOM(df, n):  
    M = pd.Series(df['Close'].diff(n), name = 'Momentum_' + str(n))  
    df = df.join(M)  
    return df

# Log returns n = 1, 2, 3, 4, 5, 10, 20
def LogRet(df, n):  
    M = df['close'] 
    N = df['close'].shift(n)  
    ROC = pd.Series(np.log(M / N), name = 'LogRet_' + str(n))  
    df = df.join(ROC)  
    return df

#Rate of Change  n = 1, 2, 3, 4, 5, 10, 20
def ROC(df, n):  
    M = df['Close'].diff(n)  
    N = df['Close'].shift(n)  
    ROC = pd.Series(M / N, name = 'ROC_' + str(n))  
    df = df.join(ROC)  
    return df

