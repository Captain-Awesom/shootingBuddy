# Start Date 2022.05.25
# Hours accumulated.  1.75
# Make a normal distribution generator. Done 2022.05.26
# Generated an Array of normally distributed random numbers. Done 2022.05.26
# Analyze a round of shooting, 30 arrows to get the statistical variables to feed into distribution.
# Make outputs of numbers to mimic shooting buddy.

# import required libraries

import random
from scipy.stats import norm
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb

#old plot

# Creating the distribution
#data = np.arange(1, 10, 0.01)
#pdf = norm.pdf(data, loc=5.3, scale=1)

# Visualizing the distribution
#sb.set_style('whitegrid')
#sb.lineplot(x=data, y=pdf, color='black')
#plt.xlabel('Heights')
#plt.ylabel('Probability Density')
#plt.show()

random_number = random.randint(1, 10)
print(random_number)

print(np.random.normal(5, 1.5, size=(10, 3)))

mu, sigma = 5, 1.5 # mean and standard deviation
s = np.random.normal(mu, sigma, 1000)
count, bins, ignored = plt.hist(s, 30, density=True)
plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) *np.exp( - (bins - mu)**2 / (2 * sigma**2) ),linewidth=2, color='r')
plt.show()


input()
exit()
