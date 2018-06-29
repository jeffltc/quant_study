#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 29 07:36:07 2018

@author: newchama
"""

import tushare as ts

from statsmodels.tsa.stattools import adfuller


hs300 = ts.get_hs300s()
start = '2010-01-01'
end = '2018-05-01'
stock_lst = []

for i in range(len(hs300)):
    code = hs300['code'][i]
    name = hs300['name'][i]
    print(name)
    df = ts.get_k_data(code,start,end)
    if len(df) >0 :
        print(adfuller(df['close']))
        print(adfuller(df['close'])[0] < adfuller(df['close'])[4]['5%'])
        if adfuller(df['close'])[0] < adfuller(df['close'])[4]['5%']:
            stock_lst.append((name,code))



