import numpy as np
import matplotlib.pyplot as plt

def bisection_method(f,a,b,tol):
    n=0
    ## f(a) and f(b) must have opposite signs
    if f(a)*f(b) >= 0:
        print("Bisection method fails.")
        return None
    ## check the tolerance
    while (b-a)/2.0 > tol:
        n=n+1
        midpoint = (a+b)/2.0
        if f(midpoint) == 0:
            break # found exact solution
        elif f(a)*f(midpoint) < 0:
            b = midpoint # root is in left half
        else:
            a = midpoint # root is in right half
    return midpoint,n # return midpoint as best estimate of root   

def newton_raphson_method(f, df, x0, tol):
    n = 0
    x_n = x0
    while True:
        x_n1 = x_n - f(x_n)/df(x_n) # update step
        if abs(x_n1 - x_n) < tol:
            break# check for convergence
        n += 1
        x_n = x_n1
    return x_n1,n

def secant_method(f, x0, x1, tol):
    n = 0
    x_prev = x0
    x_curr = x1
    
    while True:
        # Calculate the Secant update
        # x_next = x_curr - f(x_curr) * (x_curr - x_prev) / (f(x_curr) - f(x_prev))
        # Calculate step size
        # Equivalent to f(x_n)/df(x_n) in Newton's, but slope is approximated
        if f(x_curr) - f(x_prev) == 0: 
            break # Avoid division by zero
            
        x_next = x_curr - f(x_curr) * ((x_curr - x_prev) / (f(x_curr) - f(x_prev)))
        
        # Check for convergence 
        if abs(x_next - x_curr) < tol:
            break
            
        n += 1
        
        x_prev = x_curr
        x_curr = x_next
        
    return x_curr, n
# --- 1. Define the Function ---
def f(x):
    R = 2.0
    return 1 - x - np.exp(-R * x)
def df(x):
    return - x + np.exp(-2 * x)

# --- 2. Setup Variables ---
a, b = 0.1, 1.0      # Search interval 
tolerance = 0.0001   

solution_bisection,steps_bisection= bisection_method(f, a, b, tolerance)
solution_nr,steps_nr = newton_raphson_method(f,df,0.5, tolerance)
solution_secant,steps_secant = secant_method(f,0.5,0.6,tolerance)  

print(f"Bisection Result: x = {solution_bisection :.4f} (in {steps_bisection} steps)")
print(f"Newton-Raphson Result: x = {solution_nr :.4f} (in {steps_nr} steps)")
print(f"Secant Result: x = {solution_secant :.4f} (in {steps_secant} steps)")
