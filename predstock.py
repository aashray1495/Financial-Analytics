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

daily_ret = np.exp(drift.values + stddev.values * norm.ppf(np.random.rand(t_int, itern)))#Daily Returns Formula

print('Daily Returns of PG is:', daily_ret)

S0 = dat.iloc[-1]#Setting 1st price equivalent to the latest price of the asset
price_list = np.zeros_like(daily_ret)#Creating matrix of 0s and using loop to insert values

for t in range(1, t_int):
	price_list[t]= price_list[t-1] + daily_ret[t]

plt.figure(figsize=(10,6))
plt.plot(price_list)
plt.show()

