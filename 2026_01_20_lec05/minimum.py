import numpy as np 
import matplotlib.pyplot as plt 

# A program to find the smallest number from a set of numbers, and also its location. 
def my_minimum(a):
    m = a[0] # to store the minimum value
    minLoc = 0# to store the location of the minimum
    for i in range(len(a)): # len(a) is the length of the array a (number of elements)
        if m > a[i]:
            m = a[i]
            minLoc = i
    return m, minLoc

a = np.random.random(1000)
minVal , minLoc = my_minimum(a)

print(minVal)
print(minLoc)

# This can also be done using numpy.
print(np.min(a)) 
print(np.argmin(a))
