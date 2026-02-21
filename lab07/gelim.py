import numpy as np
import matplotlib.pyplot as plt

A0 = np.array(
    [
        [0.0, 1.0, 2.0, 1.0],
        [1.0, 2.0, 1.0, 1.0],
        [2.0, 7.0, 8.0, 1.0],
        [3.0, 1.0, 1.0, 1.0],
    ]
)
b = np.array([4, 5, 18, 6])

# this converts b to a column vector
b = np.reshape(b, [len(b), 1])

# augmented matrix
A = np.hstack([A0, b])

N = A.shape[0]
m = np.zeros([N,N])
row = np.arange(N)
lastCol = A.shape[1] - 1

# Obtaining an upper triangular form
for k in range(N):

    # Partial Pivoting with the first nonzero element
    if A[k, k] == 0:
        for l in range(k + 1, N):
            if A[l, k] != 0:
                # just swap with the first suitable column
                A[[k,l]] = A[[l,k]]
                print("Swapped rows {:d} and {:d}".format(k + 1, l + 1))
                break

    m[k,k] = 1.0
    # this index keeps track of the diagonal position, below which we want zeros
    for i in range(k + 1, N):
        # this is the multiplication factor needed to eliminate elements below A[k,k]
        m[i, k] = A[i, k] / A[k, k]
        
        for j in range(k, A.shape[1]):
            # perform the elimination step
            A[i, j] = A[i, j] - m[i, k] * A[k, j]

# Back substitution
x = np.zeros(N)
for i in range(N - 1, -1, -1):  # backwards loop
    x[i] = A[i, lastCol]
    for j in range(i + 1, N):  # loop over previously calculated x[i]
        x[i] = x[i] - A[i, j] * x[j]
    x[i] = x[i] / A[i, i]

print(x)
