# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 18:30:17 2023

@author: lisan
"""
#2018

#2a - find general solution to differential equation
import sympy as sp 
import numpy as np
# Define the symbols
x, w, T_a, y_0 = sp.symbols('x,w,T_a, y_0')
y = sp.Function('y')(x)

# Define the differential equation
#sp.diff - function
#sp.Derivative - class 
y = (T_a/w)*sp.cosh((w/T_a)*x)+y_0-(T_a/w)
diff_eq = sp.diff(y,x)
diff2a_eq = sp.diff(y,x, x)
diff2b_eq = (w/T_a) *sp.sqrt((1+(sp.diff(y,x))**2))
 
# Find the general solution
solution_1 = sp.solve(diff2a_eq, x)
solution_2 = sp.solve(diff2b_eq, x)

# Display the general solution
print("General Solution:")
print(solution_2)

if solution_1 == solution_2:
    print('TRUE')
else: 
    print('FALSE')
     

 
