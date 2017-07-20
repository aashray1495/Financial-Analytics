#Predicting Option Price and viability using Euler Discretization
import numpy as np  
import pandas as pd  
from pandas_datareader import data as web  
from scipy.stats import norm 
import matplotlib.pyplot as plt 

#S-stock price; K-strike price(offered to buyer); r-risk free rate; stdev; T-time horizion(in yrs)

ticker = 'PG'  
data = pd.DataFrame()
data[ticker] = web.DataReader(ticker, data_source='google', start='2007-1-1', end='2017-3-21')['Close']

ticks = ['PG']
dat=pd.DataFrame()

for t in ticks:
	dat[t]= wb.DataReader(t, data_source='yahoo', start='2007-1-1')['Adj Close']


log_ret = np.log(1 + data.pct_change())

stdev=log_ret.std()* 250 ** 0.5

r=0.025

stdev = stdev.values#Converting stdev into numpy arrays
T = 1.0 
t_intervals = 250 
delta_t = T / t_intervals 

iterations = 10000  

#Normalizaing data 
Z = np.random.standard_normal((t_intervals + 1, iterations))  #Defining dimension of Matrix
S = np.zeros_like(Z) 
S0 = data.iloc[-1]  
S[0] = S0

#Applying Formula
for t in range(1, t_intervals + 1):
    S[t] = S[t-1] * np.exp((r - 0.5 * stdev ** 2) * delta_t + stdev * delta_t ** 0.5 * Z[t])

plt.figure(figsize=(10, 6))
plt.plot(S[:, :10]);