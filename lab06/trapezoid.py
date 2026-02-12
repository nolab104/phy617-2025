import numpy as np
import matplotlib.pyplot as plt

# Given a disc of radius 4 and mass per unit area sqrt(r), determine its mass

def f(r):
    # this is the function we need to integrate with limits 0,4
    return 2 * np.pi * r * np.sqrt(r)

R = 4 # radius
a = 0 # lower limit of integration
b = R # upper limit of integration
N = 100 # upper limit of number of partitions

h = np.zeros(N) # a place to store the values of h used
nPartitions = np.arange(1, N + 1)  # number of partitions
I = np.zeros(N)  # store the integral value here for each value of h

for n in nPartitions:
    r = np.linspace(a, b, n + 1)
    h[n - 1] = (b - a) / n
    for i in range(1, n + 1):
        I[n - 1] = I[n - 1] + 0.5 * h[n - 1] * (f(r[i]) + f(r[i - 1]))

er = np.abs(128 * np.pi / 5 - I) # deviation of our integral from the true result
# a rough estimate of the slope
slope = (np.log10(er[30]) - np.log10(er[60])) / (np.log10(h[30]) - np.log10(h[60])) 
# should be around 2. 
print(slope)

# Plot the error versus step size h
plt.loglog(h, er)
plt.xlabel("h")
plt.ylabel("Error")
plt.grid()
plt.show()
