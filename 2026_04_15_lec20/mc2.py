import numpy as np 
import matplotlib.pyplot as plt 

N = 1000000

x = 0
y = 0
xIn = []
xOut = []
yIn = []
yOut = []

for i in range(N):
    dx = np.random.random()-0.5
    dy = np.random.random()-0.5
    if np.abs(x + dx) < 0.5 and np.abs(y + dy) < 0.5:
        x = x + dx
        y = y + dy
    if x**2.0 + y**2.0 < 0.25:
        xIn.append(x)
        yIn.append(y)
    else:
        xOut.append(x)
        yOut.append(y)
     
myPi = 4*len(xIn)/(len(xIn)+len(xOut))
print("{:.8f}".format(myPi))
xIn = np.asarray(xIn)
xOut = np.asarray(xOut)
yIn = np.asarray(yIn)
yOut = np.asarray(yOut)

th = np.linspace(0, 2*np.pi,1001)
plt.plot(0.5*np.cos(th), 0.5*np.sin(th),"-k")

plt.plot(xIn,yIn,'.', alpha = 0.01)
plt.plot(xOut,yOut,'.', alpha = 0.01)
plt.axis("square")
plt.xlim(-0.5,0.5)
plt.ylim(-0.5,0.5)
plt.show()
