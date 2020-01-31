#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 12:05:00 2020

@author: gmiravalles
"""

import pandas as pd
# https://github.com/quantopian/pyfolio
import pyfolio as pf
import yfinance as yf

cartera = ['YPF','GGAL','AMZN','AAPL','TLT','SHY','IEF']
data = pd.DataFrame(columns=cartera)

for ticker in cartera:
    data[ticker] = yf.download(ticker,period='10y')['Adj Close']

data = data.pct_change().dropna().mean(axis=1)
print(data.describe())

#pf.create_full_tear_sheet(data)