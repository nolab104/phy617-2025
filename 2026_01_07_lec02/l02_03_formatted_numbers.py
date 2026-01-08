# Formatted numbers in python
# It is possible to output numbers in scientific notation
x = 1268746857329857349587.28767 # a long number
# look at the syntax below carefully. 
# .3 indicates 3 decimal places; e indicates scientific notation
# remember that "e" does not mean "e raised to"
print("{:.3e}".format(x)) 
# observe that the number is rounded off to three decimal places, not truncated
