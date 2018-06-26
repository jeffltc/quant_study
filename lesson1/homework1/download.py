#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 23 10:03:45 2018

@author: newchama
"""

import tushare as ts

import sqlite3


df = ts.get_hist_data('hs300')
conn = sqlite3.connect('trade.db')
df.to_sql('trade',conn)


#存入数据库
#df.to_sql('sqlite:///trade.db', echo=True)

#追加数据到现有表
#df.to_sql('tick_data',engine,if_exists='append')