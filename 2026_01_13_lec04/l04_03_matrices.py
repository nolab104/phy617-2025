import numpy as np 
import matplotlib.pyplot as plt 

# this is how we define a 1D array or "vector"
v = np.array([1,2,3])
# this is how we define a 2D array or "matrix"
M = np.array([[1,2,3],[4,5,6],[7,8,9]])
# let us see how print works with them:
print(v)
print(M)

# this is the way to access individual elements. Remember that python indexing starts at zero. 
print(M[0,0])

# Matrix multiplication - this makes sense only when the dimensions match. 
print(M@v)
