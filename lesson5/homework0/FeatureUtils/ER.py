#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  3 13:10:42 2018

@author: zhangjue
"""

import pandas as pd
import matplotlib.pyplot as plt
import tushare as ts



#ER = Change/Volatility
#
#Change = ABS(Close - Close (10 periods ago))
#
#Volatility = Sum10(ABS(Close - Prior Close))
#Volatility is the sum of the absolute value of the last ten price changes (Close - Prior Close). 


data = ts.get_k_data('600000',start='2010-01-01', end='2016-01-01')
data = pd.DataFrame(data)

n = 10

def ER(data,n = 10):
     change = data['close'].diff(n).abs()
     t_change =  data['close'].diff(1).abs()
     volatility = (t_change).rolling(min_periods=10, window=10).sum()
     ER = pd.Series(change/volatility,name='Efficiency Ratio')
     data = data.join(ER)
     return data 