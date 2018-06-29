#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 29 08:14:01 2018

@author: newchama
"""

import tushare as ts

import numpy as np
import pandas as pd
import statsmodels.api as sm
import seaborn as sns

start_date = '2017-06-26'
end_date = '2018-06-26'

#hs300 = ts.get_hs300s()
#close_price_list = []
#symbol_dict = {}
#
#for i in range(len(hs300)):
#    code = hs300['code'][i]
#    name = hs300['name'][i]
#    df = ts.get_k_data(code,start_date, end_date)
#    if len(df)==246:
#        print(name)
#        close_price_list.append(df['close'])
#        symbol_dict[code] = name

n = len(close_price_list)
result_lst = []

for i in range(0,n):
    stock1 = close_price_list[i]
    for j in range(0,n):
        stock2 = close_price_list[j]
        result = sm.tsa.stattools.coint(stock1, stock2)
        result_lst.append((i,j,result))

#stock1 = ts.get_k_data('600000',start_date, end_date)['close']
#stock2 = ts.get_k_data('600036',start_date, end_date)['close']
#
#result = sm.tsa.stattools.coint(stock1, stock2)