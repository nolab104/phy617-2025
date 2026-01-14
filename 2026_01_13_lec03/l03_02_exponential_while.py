# Now, let us do something more involved, beyond what we can do by hand 
# Let us write a program that calculates exp(x)
e = 2.718281828459045235360287471352 

def fac(n):
    # calculate factorial of q; store it in f
    f = 1
    for i in range(n): # remember that i goes from 0 to n-1
        f = f * (i +1) # i+1 goes from 1 to n as needed
    return f

def f2(x,tol): # defines a function f that takes x and N as arguments
    # a function to evaluate the exp(x) Taylor series to N terms
    ex = 0 # initialize variable to store the value of exp(x)
    converged = False
    q = 0 # this will be 
    while not converged:  
        term_q = x**q/fac(q) # current term of the series
        ex = ex + term_q
        converged = term_q < tol # is this accurate enough? 
        q = q + 1
    print("No. of terms: {:d}".format(q))
    return ex # the function returns the value ex


for i in range(1,7):
    print("{:3d} {:.8e}".format(i, f2(3,10**(-i))))
