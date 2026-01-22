import numpy as np
import matplotlib.pyplot as plt

# A program to find the minimum of the sin function in a given domain.


def my_minimum(a):
    m = a[0]  # to store the minimum value
    minLoc = 0  # to store the location of the minimum
    for i in range(len(a)):
        if m > a[i]:
            m = a[i]
            minLoc = i
    return m, minLoc


def f(x):
    return np.sin(x)


def fDer(x):
    return np.cos(x)


def bisection(a, b, eps):
    n = 0
    # f(a) and f(b) should have opposite signs
    while np.abs(a - b) > eps:
        n = n + 1
        c = 0.5 * (a + b)  # this point lies midway between a and b
        # compare the sign of f(a), f(b) and f(c)
        fc = f(c)
        if fc == 0:  # for now, avoid this trivial case
            break
        elif fc * f(a) < 0: # decide which half interval to retain
            b = c
        else:
            a = c
    print("Bisection Method Converged in {:d} steps".format(n))
    return c


def newton(x0, eps):
    x = x0  # initial value of x
    xn = x + 100 * eps  # so that the while loop starts the first time
    n = 0  # to keep count of number of iterations
    while True:
        n = n + 1  # add one.. first iteration 1, second 2, third 3 and so on
        xn = x - f(x) / fDer(x)  # the Newton Raphson update function
        if (
            np.abs(xn - x) <= eps
        ):  # check stopping criterion; if true, just return the value of xn and exit.
            print("N-R Converged in {:d} steps".format(n))
            return xn
        x = xn  # if not converged, current xn becomes the starting point for the next iteration


# Bisection method
minValB = bisection(2.5, 3.5, 1e-12)
print("Bisection: {:.12f}".format(minValB))

# Newton
minValNR = newton(2.5, 1e-12)
print("N-R: {:.12f}".format(minValNR))

# The numpy value
print("Numpy: {:.12f}".format(np.pi))
