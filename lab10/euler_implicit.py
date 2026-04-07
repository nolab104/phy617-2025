import numpy as np
import matplotlib.pyplot as plt

# Write down the equation for first order kinetic decay of a quantity x with a rate constant of 50/s. At time t = 0, x = 1.0. Determine the decay curve of x in the range of times between 0 seconds to 5 seconds using (1) the forward Euler method and (2) the implicit Euler method. What is the typical value of h you need to use in each case for the method to work?

# rate constant in the ODE RHS
k = 50

def f(t, x):
    # RHS of the ODE
    return -k * x

def fi(t, x, x0, h):
    # this is the fuction whose zero we should locate for the implicit Euler
    return x - x0 - h * f(t, x)

def fiDer(t, x, h):
    # derivative of the function whose root we need to determine (for Newton Method)
    return 1 + k * h

def newton(tCurrent, xPrevious, h , eps):
    x = xPrevious  # initial gues value of x
    n = 0  # to keep count of number of iterations
    while True:
        n = n + 1  # add one.. first iteration 1, second 2, third 3 and so on
        xn = x - fi(tCurrent, x, xPrevious,h) / fiDer(
            tCurrent, x,h
        )  # the Newton Raphson update function
        if (
            np.abs(xn - x) <= eps
        ):  # check stopping criterion; if true, just return the value of xn and exit.
            print("N-R Converged in {:d} steps".format(n))
            return xn
        x = xn  # if not converged, current xn becomes the starting point for the next iteration


def euler(t0, x0, h, N):
    t = np.zeros(N + 1)
    xe = np.zeros(N + 1) # to store results from forward Euler
    xi = np.zeros(N + 1) # to store results from backward/implicit Euler
    # store the initial values
    t[0] = t0
    xe[0] = x0
    xi[0] = x0
    for i in range(1, N+1):
        t[i] = t[0] + i * h
        xe[i] = xe[i - 1] + f(t[i - 1], xe[i - 1]) * h
        xi[i] = newton(t[i], xi[i - 1],h,  1e-5)
    return t, xe, xi

# Solution and plotting. Modify as required
h = 0.01
t, xe, xi = euler(0, 1.0, h, int(np.ceil(5/h)))
plt.semilogy(t, xi, label="implicit")
plt.semilogy(t, xe, label="explicit")
# print(np.polyfit(t[:10], np.log(xi[:10]), 1))
# print(np.polyfit(t[:10], np.log(xe[:10]), 1))
plt.legend()
plt.show()
