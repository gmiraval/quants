#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 12:46:53 2020

@author: gmiravalles
"""

import yfinance as yf
import matplotlib.pyplot as plt

ticker = "GGAL.BA"
data = yf .download(ticker, period='20y')
print(data.head(4))
print('\n--Describe--\n', data.describe())
print('\n--Columns--\n', data.columns)

variaciones =  data['Adj Close'].pct_change()*100

agrupados = variaciones.groupby(data.index.year).sum()
agrupados.plot(kind='bar',title='GGAL - Suma de Rendimientos/año')
plt .show()

agrupados = variaciones.groupby(data.index.dayofweek).mean()
agrupados.plot(kind='bar',title='GGAL - Rendimientos/Dia Semana')
plt .show()

data['Adj Close'].resample('W').last() 
variaciones =  data['Adj Close'].pct_change()*100
agrupados = variaciones.groupby(data.index.week).mean()
agrupados.plot(kind='bar',title='GGAL- Rendimientos/Semana del Año')
plt .show()