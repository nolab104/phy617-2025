import numpy as np
import matplotlib.pyplot as plt

# this is our exponential fuinction from a previous lecture
def my_exp(x,N): 
    ex = 0 
    for q in range(N):    
        f = 1
        for i in range(q): 
            f = f * (i +1) 
        ex = ex + x**q/f
    return ex

# Let us compare the output of our function (fixed number of Taylor series terms) 
# with the numpy implementation
x = np.linspace(0,2,21) # x is a numpy array with values from 0, 0.1, 0.2, ..., 2.0 

exNumpy = np.exp(x) # elementwise exponential of x using numpy
exMyExp = my_exp(x,5) # elementwise exponential of x using our function

# Let us plot both
plt.plot(x,exNumpy,label="using numpy") # labelling plots is useful. 
plt.plot(x,exMyExp, label = "my exp")
plt.xlabel("x")
plt.ylabel("exp(x)")
plt.legend()
plt.show()