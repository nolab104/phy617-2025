import numpy as np
import matplotlib.pyplot as plt

# print("lists")
# l1 = [1,2,3]
# l2 = [3,4,5]

# print(l1 + l2)

    
# print("arrays")

# a1 = np.array([1,2,3])
# a2 = np.array([3,4,5])

# print(a1 + a2)

print("exponential using numpy")
x = np.linspace(0,2,21)
print(x)
ex = np.exp(x)
print(ex)

plt.plot(x,ex)
plt.show()