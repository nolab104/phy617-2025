import numpy as np
import matplotlib.pyplot as plt 

# NOTE THAT HERE, WE ARE ONLY EVALUATING THE INTERPOLANT AT INTERMEDIATE X POINTS. 
# WE ARE NOT CALCULATING THE COEFFICIENTS OF THE POLYNOMIAL ITSELF. 

def interpolant(xData, yData, x):
    # Evaluate the Lagrange interpolating polynomial
    l = 0
    N = len(xData) # this equals n + 1 in our analysis 
    for j in range(N): # 0 to n
        lj = 1.0
        for m in range(N): # 0 to n
            if m!=j: 
                lj = lj*(x - xData[m])/(xData[j] - xData[m])
        l = l + yData[j]*lj
    return l

# Determine the polynomial interpolant for the given data using the Lagrange method
yData = np.array([-22.50, -8.03, 4.78, 2.22, -5.45])
xData = np.array([-2,-1,0,1,2])

# Plot the interpolant together with the data
x = np.linspace(-3,3, 1024)
y = interpolant(xData, yData, x)
plt.plot(xData,yData,'s', label = "Data")
plt.plot(x,y, label = "Interpolant")
plt.legend()
plt.xlabel("x")
plt.ylabel("y")
plt.show()



