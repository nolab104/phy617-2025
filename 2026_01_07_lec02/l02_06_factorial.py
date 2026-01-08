#A simple program to compute a factorial
n = 5 # this is the number whose factorial we want to compute
f = 1 # initialize the variable where we intend to store the factorial. 
# we plan to perform successive multiplications to update f, so start with 1. 
# we know how many times the loop has to run
# if n = 0, the loop simply does not run

for i in range(n): # remember that i goes from 0 to n-1
    f = f * (i +1) # i+1 goes from 1 to n as needed
print("{:d}! = {:d}".format(n,f))

# note how we can format multiple numbers at the same time and combine it with text. 
# remember how e represents scientific notation... here d represents an integer
