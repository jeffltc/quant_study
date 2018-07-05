#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  5 13:16:52 2018

@author: zhangjue
"""



import pandas as pd
import matplotlib.pyplot as plt
import tushare as ts




#Daily Closing Prices: 11,12,13,14,15,16,17
#First day of 5-day SMA: (11 + 12 + 13 + 14 + 15) / 5 = 13
#Second day of 5-day SMA: (12 + 13 + 14 + 15 + 16) / 5 = 14
#Third day of 5-day SMA: (13 + 14 + 15 + 16 + 17) / 5 = 15




data = ts.get_k_data('600000',start='2010-01-01', end='2016-01-01')
data = pd.DataFrame(data)

SMA = data['close'].rolling(min_periods=10, window=10).mean()





# http://stockcharts.com/school/doku.php?id=chart_school:technical_indicators:moving_averages
#EMA计算
#Initial SMA: 10-period sum / 10 
#Multiplier: (2 / (Time periods + 1) ) = (2 / (10 + 1) ) = 0.1818 (18.18%)
#EMA: {Close - EMA(previous day)} x multiplier + EMA(previous day). 
