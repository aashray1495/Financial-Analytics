#Predicting Gross Profit
import numpy as np
import matplotlib.pyplot as plt

rev_m=170 #All values are in millions
rev_stddev=20
iterations=1000

rev=np.random.normal(rev_m, rev_stddev, iterations)

plt.figure(figsize=(15,6))
plt.plot(rev)
plt.title('Revenue')
plt.show()

COGS = - (rev*np.random.normal(0.6,0.1))#60% cost of COGS with 10% Standard Deviation
plt.figure(figsize=(15,6))
plt.plot(COGS)
plt.title('COGS')
plt.show()

print('Mean:', COGS.mean())
print('Standard Deviation:', COGS.std())

#Difference between Rev and COGS gives Gross Profit

GP= rev+COGS
plt.figure(figsize=(15,6))
plt.plot(GP)
plt.title('Gross Profit')
plt.show()


print('Gross Profit Mean:', GP.mean())
print('Gross Profit Standard Deviation:', GP.std())
print('Max Profit:', max(GP))
print('Min Profit:', min(GP))

plt.figure(figsize=(15,6))
plt.hist(GP, bins=20, normed=True)
plt.title('Gross Profit Histogram')#Note Normal Distribution
plt.show()