# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 09:37:06 2020

@author: emc1977
"""

def inverse_quadratic_interpolation(f, x0, x1, x2, max_iter=20000000, tolerance=1e-5):
    steps_taken = 0
    while steps_taken < max_iter and abs(x1-x0) > tolerance: # last guess and new guess are v close
        fx0 = f(x0)
        fx1 = f(x1)
        fx2 = f(x2)
        L0 = (x0 * fx1 * fx2) / ((fx0 - fx1) * (fx0 - fx2))
        L1 = (x1 * fx0 * fx2) / ((fx1 - fx0) * (fx1 - fx2))
        L2 = (x2 * fx1 * fx0) / ((fx2 - fx0) * (fx2 - fx1))
        new = L0 + L1 + L2
        x0, x1, x2 = new, x0, x1
        steps_taken += 1
    return x0, steps_taken
 
f = lambda x: x**4+24*x**3+4500*x**2+18000*x+1500**2
 
root, steps = inverse_quadratic_interpolation(f, 4.3, 4.4, 4.5)
print ("root is:", root)
print ("steps taken:", steps)

#2021 paper - Q1a, no real roots therefore must use inverse quadratic interpolation technique 


