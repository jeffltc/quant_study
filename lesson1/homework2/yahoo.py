#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 05:20:45 2018

@author: newchama
"""

import pandas as pd
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import pandas_datareader.data as web
from sklearn import cluster, covariance, manifold




from pandas_datareader import data
import fix_yahoo_finance as yf
yf.pdr_override() 

import numpy as np

import tushare as ts 

hs300 = ts.get_hs300s()

quotes = []
symbol_dict = {}
start_date = '2017-06-26'
end_date = '2018-06-26'

for i in range(len(hs300)):
    code = hs300['code'][i]
    name = hs300['name'][i]
    df = ts.get_k_data(code,start_date, end_date)
    if len(df)==246:
        print(name)
        quotes.append(df)
        symbol_dict[code] = name

symbols, names = np.array(sorted(symbol_dict.items())).T

#quotes = []
#start_date = '2017-06-26'
#end_date = '2018-06-26'
#
#for code in hs300['code']:
#    print(code)
#    df = ts.get_k_data(code,start_date, end_date)
#    if not df.empty:
#        quotes.append(df)
#
#close_price_list = []
#open_price_list = []
#
#for i in range(0,len(quotes)):
#    if len(quotes[i]) == 246:
#        close_price_list.append(quotes[i]['close'])
#        open_price_list.append(quotes[i]['open'])


#
#close_prices = np.vstack([q for q in close_price_list])
#open_prices = np.vstack([q for q in open_price_list])
#




## The daily variations of the quotes are what carry most information
#variation = close_prices - open_prices
#
#
## #############################################################################
## Learn a graphical structure from the correlations
#edge_model = covariance.GraphLassoCV()
#
## standardize the time series: using correlations rather than covariance
## is more efficient for structure recovery
#X = variation.copy().T
#X /= X.std(axis=0)
#edge_model.fit(X)
#
#
## #############################################################################
## Cluster using affinity propagation
#
#_, labels = cluster.affinity_propagation(edge_model.covariance_)
#n_labels = labels.max()
#
#for i in range(n_labels + 1):
#    print('Cluster %i: %s' % ((i + 1), ', '.join(names[labels == i])))