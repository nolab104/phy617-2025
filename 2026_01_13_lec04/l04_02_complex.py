import numpy as np 
import matplotlib.pyplot as plt 

# Using complex numbers with numpy
# the notation for sqrt(-1) is 1j

# This is how one defines a complex number. 
z = 1 + 2*1j # I personally prefer 1 + 2*1j to 1 + 2j
print(z)

# Demonstrating a few simple numpy functions
x = np.linspace(-4*np.pi, 4*np.pi,100)
s = np.sin(x)
c = np.cos(x)
ce = np.exp(1j*x) # complex exponential
# rce = 0.5* (ce + np.conj(ce))
rce = np.real(ce) # should be equal to cos(x)
ice = np.imag(ce) # should be equal to sin(x)

plt.plot(x, c)
plt.plot(x,rce, "o") # the "o" tells pyplot to use circles instead of lines in the plot
plt.plot(x, s)
plt.plot(x,ice, "o")
plt.xlabel("x")
plt.show()
