#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  4 12:58:42 2018

@author: zhangjue
"""


#Wilder started with a concept called True Range (TR), which is defined as the greatest of the following:
#
#Method 1: Current High less the current Low
#Method 2: Current High less the previous Close (absolute value)
#Method 3: Current Low less the previous Close (absolute value)

#Current ATR = [(Prior ATR x 13) + Current TR] / 14
#
#  - Multiply the previous 14-day ATR by 13.
#  - Add the most recent day's TR value.
#  - Divide the total by 14


import pandas as pd
import matplotlib.pyplot as plt
import tushare as ts

#def ATR(data,n):
#    for i in len(data)
#    
#    data = data.join(ATR)
#    return data


data = ts.get_k_data('600000',start='2010-01-01', end='2016-01-01')
data = pd.DataFrame(data)


# ATR
def ATR(data,n =1):
    TR_lst = [data.iloc[0]['high']-data.iloc[0]['low']]
    for i in range(1,len(data)):
        current_high = data.iloc[i]['high']
        current_low = data.iloc[i]['low']
        previous_close = data.iloc[i-1]['close']
        TR1 = current_high - current_low
        TR2 = current_high - previous_close
        TR3 = current_low - previous_close
        TR = max(TR1,TR2,TR3)
        TR_lst.append(TR)
    
    ATR = []
    
    for i in range(0,14):
        ATR.append(TR_lst[i])
    
    ATR.append(sum(ATR)/len(ATR))
        
    for i in range(15,len(TR_lst)):
        ATR.append((ATR[i-1]*13 + TR_lst[i])/14)
    ATR = pd.Series(ATR, name = 'Actual True Range') 
    data = data.join(ATR) 
    return data
