#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 17:12:35 2020

@author: gmiravalles
"""

import yfinance as yf
import matplotlib.pyplot as plt

#bajo datos en data
ticker = "GGAL.BA"
data = yf .download(ticker, period='20y')
print(data.head(4))

print('\n--Describe--\n', data.describe())
print('\n--Columns--\n', data.columns)

#plot de datos en data
plt .style.use('dark_background')
plt.rcParams['figure.figsize'] = [12.0, 5]
plt.yscale('log')
data['Adj Close'].plot(kind='line',title='GGAL en pesos')
