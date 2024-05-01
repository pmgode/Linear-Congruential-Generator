import numpy as np
import matplotlib.pyplot as plt
import math as math
import random
class LCG:
    def __init__(self, seed=1, a=16807, c=0, m=2**31 - 1):
        self.seed = seed
        self.a = a
        self.c = c
        self.m = m

    def next(self):
        self.seed = (self.a * self.seed + self.c) % self.m
        return self.seed
def uniform_lcg(a, b, lcg):
  #  lcg.seed = seed  # Set the seed value
    return a + (b - a) * (lcg.next() / float(lcg.m))

def exponential_lcg(lcg):
    return -1 * math.log(1 - (lcg.next() / float(lcg.m)))

# Generate random numbers using LCG
lcg = LCG()
#seed_value = 10;
uniform_values_lcg = np.array([uniform_lcg(0, 2, lcg) for _ in range(500)])
exponential_values_lcg = np.array([exponential_lcg(lcg) for _ in range(500)])
print(uniform_values_lcg)
print(exponential_values_lcg)


# Generate random numbers using Python's default random number generator
uniform_values_default = np.array([random.uniform(0, 2) for _ in range(500)])
exponential_values_default = np.array([random.expovariate(1) for _ in range(500)])

# Visual inspection: Histograms
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plt.hist(uniform_values_lcg, bins=30, alpha=0.5, label='LCG')
plt.hist(uniform_values_default, bins=30, alpha=0.5, label='Default RNG')
plt.title('Uniform Distribution for 500 samples')
plt.legend()

plt.subplot(1, 2, 2)
plt.hist(exponential_values_lcg, bins=30, alpha=0.5, label='LCG')
plt.hist(exponential_values_default, bins=30, alpha=0.5, label='Default RNG')
plt.title('Exponential Distribution for 500 samples')
plt.legend()

plt.show()

# Summary statistics
print("Mean of uniform distribution (LCG):", np.mean(uniform_values_lcg))
print("Mean of uniform distribution (Default RNG):", np.mean(uniform_values_default))
print("Variance of uniform distribution (LCG):", np.var(uniform_values_lcg))
print("Variance of uniform distribution (Default RNG):", np.var(uniform_values_default))

print("Mean of exponential distribution (LCG):", np.mean(exponential_values_lcg))
print("Mean of exponential distribution (Default RNG):", np.mean(exponential_values_default))
print("Variance of exponential distribution (LCG):", np.var(exponential_values_lcg))
print("Variance of exponential distribution (Default RNG):", np.var(exponential_values_default))

# Quantile-Quantile (Q-Q) plot
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
stats.probplot(uniform_values_lcg, dist="uniform", plot=plt)
plt.title('Uniform Distribution (LCG) Q-Q Plot')

plt.subplot(1, 2, 2)
stats.probplot(exponential_values_lcg, dist="expon", plot=plt)
plt.title('Exponential Distribution (LCG) Q-Q Plot')

plt.show()
