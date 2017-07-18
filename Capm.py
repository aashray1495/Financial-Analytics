#Calculating Expected Return(CAPM) of a stock
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas_datareader import data as wb

ticks = ['PG', '^GSPC']
dat=pd.DataFrame()

for t in ticks:
	dat[t]= wb.DataReader(t, data_source='yahoo', start='2010-2-2')['Adj Close']

#beta is covariance of stock and market upon variance of market
sec_ret = np.log(dat/dat.shift(1))  
cov = sec_ret.cov() * 250
cov_with_mkt=cov.iloc[0,1]

mkt_var = sec_ret['^GSPC'].var() * 250

PG_beta = cov_with_mkt/mkt_var

print('Beta of PG is:', PG_beta)

PG_expected_ret = 0.025 + PG_beta * 0.05 #Risk free return=2.5%, Risk premium=0.05% for PG


print('Expected Return(CAPM) of PG is:', PG_expected_ret)


