#Markov Portfolio Optimization - Efficient Frontier Problem
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas_datareader import data as wb

assets = ['PG', '^GSPC']
pf=pd.DataFrame()

for a in assets:
	pf[a]= wb.DataReader(a, data_source='yahoo', start='2010-2-2')['Adj Close']

log_ret = np.log(pf/pf.shift(1))  
log_ret.mean() * 250
log_ret.cov() * 250
log_ret.corr()

#Setting sum of weights equal to 1
num_assets = len(assets)
weights = np.random.random(num_assets)
weights /= np.sum(weights)
print('Weights are ', weights) 

#Expected Portfolio Return
expr = np.sum(weights*log_ret.mean()) * 250
#Expected Portfolio Variance
expv = np.dot(weights.T, np.dot(log_ret.cov()*250, weights))
#Expected Portfolio Volatility
expvl = np.sqrt(expv)

#Efficient Frontier Code
pf_ret = []
pf_vol = []

for x in range(1000):
	weights=weights = np.random.random(num_assets)
    weights /= np.sum(weights)
    pf_ret.append(np.sum(weights*log_ret.mean()) * 250)
    pf_vol.append(np.sqrt(np.dot(weights.T, np.dot(log_ret.cov()*250, weights))))

#Creating numpy arrays for both
pf_ret=np.array(pf_ret)
pf_vol=np.array(pf_vol)    

Portfolios=pd.DataFrame({'Return': pf_ret, 'Volatility': pf_vol})
Portfolios.plot(x='Volatility', y='Return', kind='scatter', figsize(10,5))
plt.xlabel('Expected Volatility')
plt.ylabel('Expected Return')
