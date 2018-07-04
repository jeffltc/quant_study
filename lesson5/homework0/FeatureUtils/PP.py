#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  5 06:14:57 2018

@author: newchama
"""




#Pivot Point (P) = (High + Low + Close)/3
#
#Support 1 (S1) = (P x 2) - High
#
#Support 2 (S2) = P  -  (High  -  Low)
#
#Resistance 1 (R1) = (P x 2) - Low
#
#Resistance 2 (R2) = P + (High  -  Low)



import pandas as pd
import matplotlib.pyplot as plt
import tushare as ts

def PP(data,n = 1):
    P = (data['high'] + data['low'] + data['close'])/3
    S1 = P*2 - data['high']
    S2 = P - (data['high'] - data['low'])
    R1 = P*2 - data['low']
    R2 = P + (data['high'] - data['low'])
    PP = pd.DataFrame({'P':P,'S1':S1,'S2':S2,'R1':R1,'R2':R2})
    data = data.join(PP)
    return data


data = ts.get_k_data('600000',start='2010-01-01', end='2016-01-01')
data = pd.DataFrame(data)
data = PP(data)
