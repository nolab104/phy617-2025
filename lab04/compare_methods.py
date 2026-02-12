import numpy as np 
import matplotlib.pyplot as plt

def f(x):
    return np.exp(-x+2) - 1

def fDer(x):
    return -np.exp(-x+2)

def bisection(a, b, N):
    # n = 0
    # f(a) and f(b) should have opposite signs
    c = np.zeros(N)
    for n in range(N):
        # n = n + 1
        c[n] = 0.5 * (a + b)  # this point lies midway between a and b
        # compare the sign of f(a), f(b) and f(c)
        fc = f(c[n])
        if fc == 0:  # for now, avoid this trivial case
            break
        elif fc * f(a) < 0: # decide which half interval to retain
            b = c[n]
        else:
            a = c[n]
    return c

def newton(x0, N):
    x = np.zeros(N)
    x[0] = x0  # initial value of x
    for n in range(1,N):
        x[n] = x[n-1] - f(x[n-1]) / fDer(x[n-1])  # the Newton Raphson update function
        if (
            np.abs(x[n] - x[n-1]) == 0
        ):  
            x[n:] = x[n]
            break
    return x

def secant(x0, x1, N):
    x = np.zeros(N)
    x[0] = x0  # initial value of x
    x[1] = x1
    for n in range(2,N):
        fn1 = f(x[n-1])
        fn2 = f(x[n-2])
        x[n] = (x[n-2]*fn1 - x[n-1]*fn2) / (fn1-fn2)  # the Newton Raphson update function
        if (
            np.abs(x[n] - x[n-1]) == 0
        ):  
            x[n:] = x[n]
            break
            
    return x

# Bisection method
bis = bisection(0,3.5, 40)
# Newton
nr = newton(4, 40)
# secant
sec = secant(4,4.1, 40)


plt.plot(np.abs(bis), label = "Bisection")
plt.plot(np.abs(nr), label = "Newton-Raphson")
plt.plot(np.abs(sec), label = "Secant")
plt.legend()
plt.show()