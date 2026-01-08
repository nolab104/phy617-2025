# Here we try repeating steps... a few of many ways to phrase the conditions

# print numbers from 1 to 10
# Use the for command when you know how many times a procedure needs to be repeated.
for i in range(10): # here, i takes 10 values: 0,1,2,...,9
    print(i+1) # i+1 takes values 1,2,3,...,10
# Note that any statements that need to be repeated within a for block need to be indented 
# (by either a tab or spaces)

# another way to do this (student favourite)
for i in range(1,11): # here, we are asking the range to take integer values 1<=i<11 
    print(i)

# yet another way of doing this
q = 1 # we initialize q with its starting value
while q<=10: # the loop repeats until q takes a value greater than 10. 
    # this is a more flexible way of doing this. 
    # But if the number of repeats is known, use a for loop. That is simpler
    # Use the condition q<=10 when we first print q, then add one
    print(q) 
    q = q + 1 # after 10 is printed, q becomes 11 in this step and the loop does not run further

q = 0 # we initialize q differently this time
while q<10: # the loop repeats until q takes a value greater than or equal to 10. 
    # Use the condition q<10 when we first add 1 to q, then print it
    q = q + 1 # first add one
    print(q) # then print
    # when q becomes equal to 10, the loop stops. 10 has already been printed.

