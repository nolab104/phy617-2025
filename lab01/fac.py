# Compute the factorial of a number
n = 5 # this is the number whose factorial we want to compute
f = 1 # initialize f to this.. we will store the factorial in f.
for i in range(n):
    f = f*(i+1)
# output the factorial
print(f)
