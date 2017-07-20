#Predicting Option Price and viability using Black-Scholes-Merton Formula
import numpy as np
import pandas as pd
from scipy.stats import norm
from pandas_datareader import data as wb

#s-stock price; k-strike price(offered to buyer); r-risk free rate; stddev; t-time horizion(in yrs)

#Evaluating 2 important parameters: d1 and d2
def d1(s, k, r, stddev, t):
	return(np.log(s/k) + (r + stddev **2 /2)/ (stddev * np.sqrt(t)))

def d2(s, k, r, stddev, t):
	return(np.log(s/k) + (r - stddev **2 /2)/ (stddev * np.sqrt(t)))

#Applying BSM
def BSM(s,k,r,stddev,t):
	return(s *norm.cdf(d1(s,k,r,stddev,t))) - (k*np.exp(-r*t)*norm.cdf(d2(s,k,r,stddev,t)))

ticks = ['PG']
dat=pd.DataFrame()

for t in ticks:
	dat[t]= wb.DataReader(t, data_source='yahoo', start='2007-1-1')['Adj Close']


s = dat.iloc[-1]

log_ret = np.log(1 + data.pct_change())

stddev=log_ret.std()* 250 ** 0.5

r=0.025
k=110
t = 1

print('d1',d1(s, k, r ,stddev, t))
print('d2',d2(s, k, r ,stddev, t))
print('Resultant Returns:',BSM(s, k, r ,stddev, t))
