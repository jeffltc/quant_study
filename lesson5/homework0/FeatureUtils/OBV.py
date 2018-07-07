#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  4 06:23:28 2018

@author: newchama
"""


#The On Balance Volume (OBV) line is simply a running total of positive and negative volume.
# A period's volume is positive when the close is above the prior close. 
# A period's volume is negative when the close is below the prior close.
#
#If the closing price is above the prior close price then: 
#Current OBV = Previous OBV + Current Volume
#
#If the closing price is below the prior close price then: 
#Current OBV = Previous OBV  -  Current Volume
#
#If the closing prices equals the prior close price then:
#Current OBV = Previous OBV (no change)


import pandas as pd
import matplotlib.pyplot as plt
import tushare as ts

#On Balance Volumn

def OBV(data, ndays = 1): 
    OBV = [data['volume'][0]]
    
    for i in range(1,len(data)):
        if data['close'].iloc[i] < data['close'].iloc[i-1]:
            current_OBV = OBV[i-1] - data['volume'].iloc[i]
        elif data['close'].iloc[i] == data['close'].iloc[i-1]:
            current_OBV = OBV[i-1]
        elif data['close'].iloc[i] > data['close'].iloc[i-1]:
            current_OBV = OBV[i-1] + data['volume'].iloc[i]
        OBV.append(current_OBV)
    
    OBV = pd.Series(OBV, name = 'On Balance Volumn') 
    data = data.join(OBV) 
    return data



# Retrieve  data from tushare:
data = ts.get_k_data('600000',start='2010-01-01', end='2016-01-01')
data = pd.DataFrame(data)
data = OBV(data,1)
