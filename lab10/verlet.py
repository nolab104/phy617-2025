# Set up the differential equation of motion of a 1 kg point mass in a one-dimensional harmonic oscillator potential centered around x = 0 with a force constant k = 12.0 N/m. At time t = 0, the mass is at a point x0 = -1 m and moves with a velocity u0 = 0.1 m/s. Numerically determine the variation of position x with time using (1) the Verlet method and (2) by converting the system to a system of two first order ODEs. Plot your results. In each case, also track the total energy at every step and plot it versus time.

import numpy as np
import matplotlib.pyplot as plt


"""
System of equations
x'' = -kx
Let us define x' = p and x = q
can be converted to 
p' = -kq
q' = p
Now we have a vector x = [p,q] 
"""

# Setting up the problem
x0 = -1 # initial position
u = 0.1 # initial velocity
k = 12.0 # force constant
h = 0.025 # interval
N = 100000 # Number of steps

def f_RK4(t, x):
    return np.array([-k * x[1], x[0]])

def f_VV(t, x):
    return -k*x

X = np.zeros([2, N])
t = np.zeros(N)
x = np.zeros(N)
v = np.zeros(N)

t[0] = 0

# for RK4
X[0, 0] = u  # initial velocity
X[1, 0] = x0
# for Velocity Verlet
x[0] = x0
v[0] = u

for i in range(1, N):
    t[i] = t[i - 1] + h
    # RK4 step    
    F1 = h * f_RK4(t[i - 1], X[:, i - 1])
    F2 = h * f_RK4(t[i - 1] + h / 2.0, X[:, i - 1] + F1 / 2.0)
    F3 = h * f_RK4(t[i - 1] + h / 2.0, X[:, i - 1] + F2 / 2.0)
    F4 = h * f_RK4(t[i - 1] + h, X[:, i - 1] + F3)
    X[:, i] = X[:, i - 1] + (F1 + 2 * F2 + 2 * F3 + F4) / 6.0

    # Velocity Verlet step
    x[i] = x[i - 1] + v[i - 1] * h + 0.5 * f_VV(t[i - 1], x[i - 1]) * h**2.0
    v[i] = v[i - 1] + 0.5 * h * (f_VV(t[i - 1], x[i - 1]) + f_VV(t[i], x[i]))

# Kinetic and potential energies
K_RK4 = 0.5 * X[0, :] ** 2.0
U_RK4 = 0.5 * k * X[1, :] ** 2.0
K_VV = 0.5 * v**2.0
U_VV = 0.5 * k * x**2.0
# plt.plot(t, x[1, :])
# plt.plot(t, x[0, :])
# plt.plot(t, K)
# plt.plot(t, U)
plt.plot(t, K_RK4 + U_RK4)
plt.plot(t, K_VV + U_VV, alpha = 0.1)
plt.show()
