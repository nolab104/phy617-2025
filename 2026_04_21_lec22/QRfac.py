import numpy as np 
from pprint import pp, pprint

# QR factorization and calculation of eigenvalues

def factorize_QR(M):
    # QR factorization of a matrix using Gram Schmidt process
    u = np.zeros_like(M)
    Q = np.zeros_like(M)
    # Gram-Schmidt using the columns of M
    for k in range(M.shape[0]):
        u[:,k] = M[:,k].copy()
        for i in range(k):
            u[:,k] = u[:,k] - np.dot(M[:,k],Q[:,i])*Q[:,i]
            # np.linalg.norm is simply the L2 norm of the vector. 
        Q[:,k] = u[:,k]/np.linalg.norm(u[:,k])
    R = np.zeros_like(M)
    for i in range(M.shape[0]):
        for j in range(Q.shape[1]):
            R[j,i] = np.dot(M[:,i],Q[:,j])
    return Q, R


A0 = np.array(
    [
        [1.0,1.0,2.0],
        [1.0,2.0,0.0],
        [1.0,0.0,1.0]
    ]
)
A0 = np.double(np.array([[5, 0, 0], [1, 2, 1], [1, 1, 2]]))

Q0, R0 = factorize_QR(A0)

with np.printoptions(precision=4, suppress=True):
    print("Result of Gram-Schmidt process:")
    print(Q0) # matrix whose columns form an orthonormal basis.
    print("Check if Gram Schmidt result is orthogonal")
    print(Q0.T @ Q0) # check if the matrix is indeed orthogonal. 
    print("Check QR factorization:")
    print(Q0 @R0) # matrix whose columns form an orthonormal basis.

# For the eigenvalues, I am storing the matrix at each iteration in a list. 
A = []
# Storing the orthogonal matrix in the same fashion. 
Qi = []

# start with the original matrix
A.append(A0) 
# and its QR factorization
Qi.append(Q0)

# Perform the QR iteration for a specified number of iterations: 
for i in range(1,100):
    A.append(Qi[-1].T @ A[-1] @ Qi[-1])
    Q, R = factorize_QR(A[-1])
    Qi.append(Q) # store Q after each iteration... needed for eigenvectors. 


# suppress = True ensure that really small numbers (beyond displayed decimal places) are rounded off to zero. 
with np.printoptions(suppress=True): 
    print("======Computation of eigenvalues==============")
    print(f"Matrix A after iteration {i+1}:")
    print(A[-1])
    print(f"Diagonal elements of A iteration {i+1}:")
    print(np.diag(A[-1]))
    print("Eigenvalues computed using numpy")
    print(np.linalg.eig(A0)[0]) # calculate the eigenvalues using numpy