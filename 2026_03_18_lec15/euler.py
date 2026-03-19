# DEMONSTRATION
# Solving a first order ODE initial value problem using Euler's method
import numpy as np 
import matplotlib.pyplot as plt 

# the RHS of the equation
def f(x,t): 
    return -2*x

# the actual solution
def F(t): 
    return np.exp(-2*t)

# step size 
h = 0.1
N = 10
t0 = 0
x0 = 1
t = t0 + np.arange(N)*h
x = np.zeros(N)
x[0] = x0

for i in range(1,N):
    x[i] = x[i-1] + h*f(x[i-1], t[i-1])

xCalc = F(t)
erx = (xCalc - x)/xCalc
plt.plot(t,x,'s')
plt.plot(t,xCalc)
plt.plot(t,erx)
plt.xlabel("t")
plt.ylabel("x")
plt.show()

