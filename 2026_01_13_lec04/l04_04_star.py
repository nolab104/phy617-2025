import numpy as np 
import matplotlib.pyplot as plt 

# Generate the points (vertices)
theta = np.linspace(0, 4*np.pi, 5 + 1) # note that the sixth and first points are identical
x = np.cos(theta)
y = np.sin(theta)

# a rotation to align the star correctly
theta0 = 18*np.pi/180
# this is the matrix to affect such a rotation
R = np.array([[np.cos(theta0), -np.sin(theta0)],[np.sin(theta0), np.cos(theta0)]])
# Place the x and y rows one below the other
XY = np.array([x,y])
# matrix multiplication
XYrotated = R@XY

# visualize the star
plt.plot(XYrotated[0,:], XYrotated[1,:])
plt.axis("equal")
plt.show()