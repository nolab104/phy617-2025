# Now, let us do something more involved, beyond what we can do by hand 
# Let us write a program that calculates exp(x)
e = 2.718281828459045235360287471352 

def f(x,N): # defines a function f that takes x and N as arguments
    # a function to evaluate the exp(x) Taylor series to N terms
    ex = 0 # initialize variable to store the value of exp(x)
    for q in range(N):    # display q - current term index
        # calculate factorial of q; store it in f
        f = 1
        for i in range(q): # remember that i goes from 0 to n-1
            f = f * (i +1) # i+1 goes from 1 to n as needed
        ex = ex + x**q/f
    return ex # the function returns the value ex

for i in range(1,16):
    print("{:3d} {:.8e}".format(i, f(3,i)))
