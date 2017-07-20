#Predicting Future stock price using Monte Carlo Simulation(Asset Pricing)
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm
from pandas_datareader import data as wb

ticks = ['PG']
dat=pd.DataFrame()

for t in ticks:
	dat[t]= wb.DataReader(t, data_source='yahoo', start='2007-1-1')['Adj Close']

log_ret = np.log(1 + data.pct_change())

u= log_ret.mean()

var = log_ret.var()

drift = u - (0.5*var)

stddev=log_ret.std()

t_int=1000
itern=10

daily_ret = np.exp(drift.values + stddev.values * norm.ppf(np.random.rand(t_int, itern)))


print('Predicted Daily Return of PG is:', daily_ret)

