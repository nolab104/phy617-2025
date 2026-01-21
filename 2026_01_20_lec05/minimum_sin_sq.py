import numpy as np 
import matplotlib.pyplot as plt 

# A program to find the minimum of the sin function in a given domain. 

def my_minimum(a):
    m = a[0] # to store the minimum value
    minLoc = 0 # to store the location of the minimum
    for i in range(len(a)):
        if m > a[i]:
            m = a[i]
            minLoc = i
    return m, minLoc

# If we need a better estimate of the minimum, we need to use more samples
N = 10000000 # the program becomes noticeably slow when we use several million samples
x = np.linspace(-np.pi/3, np.pi/6,N)
y = np.sin(2*x)
minVal , minLoc = my_minimum(np.abs(y))

print(minVal)
print(x[minLoc])

