# Now, let us do something more involved, beyond what we can do by hand 
# Let us write a program that calculates exp(x)
e = 2.718281828459045235360287471352 
N = 5 # number of terms in the Taylor series to retain
x = 1 # value of x
ex = 0 # variable to store the value of exp(x)
for q in range(N):    # display q - current term index
    # calculate factorial of q; store it in f
    f = 1
    for i in range(q): # remember that i goes from 0 to n-1
        f = f * (i +1) # i+1 goes from 1 to n as needed
    ex = ex + x**q/f
print("Our computation using {:d} terms: {:.8e}".format(N,ex))
print("Using known value of e: {:.8e}".format(e**x)) # using the arithmetic operator for power
