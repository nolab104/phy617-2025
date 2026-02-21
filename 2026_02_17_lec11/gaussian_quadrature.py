import numpy as np 
import matplotlib.pyplot as plt 
from scipy.special import roots_legendre

# Example to illustrate how a different choice of x_i could lead to a "better" interpolant

iColor = "#008BC7"
nodeColor = "#EF732A"
fColor = "#525252"


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


def f(x):
    return x**5 - x**4 + x**3 - x**2 - x + 1

def fInt(x):
    return x**6/6 - x**5/5+ x**4/4 - x**3/3 - x**2/2 + x


x = np.linspace(-1,1,1024)
y = f(x)

# Integration by Simpson's 3/8 rule
xDataSimpson = np.linspace(-1,1,4)
yDataSimpson = f(xDataSimpson)
intSimpson = np.sum(0.25*np.array([1,3,3,1])*yDataSimpson)
yInterpSimpson = interpolant(xDataSimpson, yDataSimpson, x)

# Integration by Gauss-Legendre Quadrature
xDataGQ, weights = roots_legendre(4)
yDataGQ = f(xDataGQ)
yInterpGQ = interpolant(xDataGQ, yDataGQ, x)
intGQ = np.sum(weights*yDataGQ)

print(fInt(1)-fInt(-1))
print(intGQ)
print(intSimpson)

# Plot: Gaussian Quadrature
plt.figure()
plt.plot(x, y, color = fColor, label = "f(x)", zorder = 10)
plt.plot(xDataGQ, yDataGQ,'s', color = nodeColor, label = "nodes", zorder = 11)
plt.plot(x,yInterpGQ, label="interpolant", color = iColor, zorder = 12)
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.axhline(0, zorder = 0, color= "k", alpha = 0.25)
plt.axvline(-1, zorder = 0, color= "k", alpha = 0.25)
plt.axvline(1, zorder = 0, color= "k", alpha = 0.25)
for xi in xDataGQ:
    plt.axvline(x = xi, linestyle = "--", color = nodeColor,  zorder = 0, alpha = 0.32)
plt.title("Gauss-Legendre Quadrature")
plt.savefig("gq.png", dpi = 300)

# Plot: Simpson's rule
plt.figure()
plt.plot(x, y, color = fColor, label = "f(x)", zorder = 10)
plt.plot(xDataSimpson, yDataSimpson,'s', color = nodeColor, label = "nodes", zorder = 11)
plt.plot(x,yInterpSimpson, label="interpolant", color = iColor, zorder = 12)
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.axhline(0, zorder = 0, color= "k", alpha = 0.25)
plt.axvline(-1, zorder = 0, color= "k", alpha = 0.25)
plt.axvline(1, zorder = 0, color= "k", alpha = 0.25)
for xi in xDataSimpson:
    plt.axvline(x = xi, linestyle = "--", color = nodeColor,  zorder = 0, alpha = 0.32)
plt.title("Simpson's 3/8 rule")
plt.savefig("simp38.png", dpi = 300)
plt.close()
