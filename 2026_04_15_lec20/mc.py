import numpy as np 
import matplotlib.pyplot as plt 

N = 1000000
x = np.random.random(N)-0.5
y = np.random.random(N)-0.5
inCircle = x**2.0 + y**2.0 < 0.25

myPi = 4*np.count_nonzero(inCircle)/N
print("{:.8f}".format(myPi))
xIn = x[inCircle]
xOut = x[~ inCircle]
yIn = y[inCircle]
yOut = y[~ inCircle]

th = np.linspace(0, 2*np.pi,1001)
plt.plot(0.5*np.cos(th), 0.5*np.sin(th),"-k")

plt.plot(xIn,yIn,'.', alpha = 0.5)
plt.plot(xOut,yOut,'.', alpha = 0.5)
plt.axis("square")
plt.xlim(-0.5,0.5)
plt.ylim(-0.5,0.5)
plt.show()
