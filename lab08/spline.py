import numpy as np
import matplotlib.pyplot as plt

def gsolve(A0,b):
    # Gaussian Elimination with scaled row pivoting

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

        # Partial Pivoting with Scaled Row Pivoting
        maxRow = k # this is the initial value for maxRow.. search from k onwards
        for l in range(k, N): # for each row, index k or greater
            if np.abs(A[maxRow,k])/np.max(np.abs(A[maxRow,k+1:])) < np.abs(A[l,k])/np.max(np.abs(A[l,k+1:])):
                maxRow = l
        # just swap with the row indexed by maxRow
        if maxRow != k:
            A[[k,maxRow]] = A[[maxRow,k]]
            print("Swapped rows {:d} and {:d}".format(k + 1, maxRow + 1))

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

    return x

def cubic_spline(x, y):
    # this function uses the values x and y to determine z. 
    n = len(x) - 1
    h = np.zeros(n + 1)
    b = np.zeros(n + 1)
    v = np.zeros(n + 1)
    u = np.zeros(n + 1)
    A = np.zeros([n + 1, n + 1])

    for i in range(n):
        print(i)
        if i < n:
            h[i] = x[i + 1] - x[i]
        if i >= 1:  # h numbering starts from 1
            u[i] = 2 * (h[i] + h[i - 1])
            b[i] = (6 / h[i]) * (y[i + 1] - y[i])
            v[i] = b[i] - b[i - 1]
            A[i, i] = u[i]
            A[i, i + 1] = h[i]
            if i >= 1:
                A[i, i - 1] = h[i - 1]
        print(A)
    A = A[1:-1, 1:-1]
    v = v[1:-1]
    # print(v.shape)
    z = gsolve(A, v)
    # print(z.shape)
    z = np.concatenate(([0.0], z, [0.0]))
    return z


def cubic_spline_evaluate(z, xi, yi, x):
    # this function evaluates the spline specified by z, xi and yi at a point x. 
    h = np.diff(xi)
    i = len(xi) - 2
    for j in range(len(xi) - 1):
        if x <= xi[0]:
            print("less than x[0]: ", x < xi[0])
            i = 0
            break
        elif x > xi[-2]:
            print("greater than x[end]: ", x > xi[-2])
            i = len(xi) - 2
            break
        if (x > xi[j]) and (x <= xi[j + 1]):
            print(x > xi[j])
            print(x <= xi[j + 1])
            i = j
            break
    print(x, xi[i])
    a = z[i] / (6 * h[i]) * (xi[i + 1] - x) ** 3.0
    b = z[i + 1] / (6 * h[i]) * (x - xi[i]) ** 3.0
    c = (yi[i + 1] / h[i] - z[i + 1] * h[i] / 6.0) * (x - xi[i])
    d = (yi[i] / h[i] - z[i] * h[i] / 6.0) * (xi[i + 1] - x)
    S = a + b + c + d
    return S


y = np.array([-4,-6, -8, 4.7, 2.3, -5, -4])
x = np.array([-3,-1.5, -1, 0, 1, 2.5, 3])

z = cubic_spline(x, y)
print(z)
xRange = np.linspace(-4,4, 1000)
yVals = np.zeros_like(xRange)
for ii in range(len(xRange)):
    yVals[ii] = cubic_spline_evaluate(z, x, y, xRange[ii])

plt.plot(x, y, "s")
plt.plot(xRange, yVals)
# plt.ylim(0,1)
plt.show()
