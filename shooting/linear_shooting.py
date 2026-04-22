import numpy as np 
import matplotlib.pyplot as plt 

# equation y'' = -y; y(0) = 1.0, y(1) = 1/e
# The solution is simple.. y = exp(-t)
# the goal here is to solve two different intiial conditions, then determine the correct linear combination that works. 

def fRHS(t,y):
    return -y

def RK4step(t,y,h):
    # hope this is self explanatory
    F1 = fRHS(t,        y)
    F2 = fRHS(t + h/2,  y + h/2 * F1)
    F3 = fRHS(t + h/2,  y + h/2 * F2)
    F4 = fRHS(t + h,    y + h   * F3)
    return y + (h/6) * (F1 + 2*F2 + 2*F3 + F4)

# using the notation used in class
a = 0.0
alpha = 1.0
b = 1.0
beta = np.exp(-1)

# do all the IVP's simultaneously: I took this from Kincaid & Cheney. 
# You can also solve them separately using RK4 and then take a linear combination... same result. 
x0 = np.array([a,alpha, alpha,0,1])
def f(x):
    return np.array(
        [1, x[3], x[4], fRHS(x[0], x[1], x[3]), fRHS(x[0], x[2], x[4])]
    )

# number of points
N = 10
# interval
t = np.linspace(a,b,N)
h = t[1]-t[0]
x = np.zeros([N,5])
x[0,:] = x0

# this is the simultaneous RK4 step
for i in range(1,N):
    x[i,:] = RK4step(t,x[i-1,:],h)

l = (beta - x[-1,4])/(x[-1,3]-x[-1,4]) # lambda in notes
print(l)

plt.plot(t,np.exp(-t), label = r"actual solution")
plt.plot(t,x[:,3],'s', label = r"$x_1(t)$")
plt.plot(t,x[:,4],'s', label = r"$x_1(t)$")
plt.plot(t,l*x[:,3] + (1-l)*x[:,4],'o', label = r"$\lambda x_1(t) + (1-\lambda)x_2(t)$")
plt.legend()
plt.xlabel("t")
plt.ylabel("x")
plt.show()







