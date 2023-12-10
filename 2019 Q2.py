# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 10:08:16 2023

@author: s2204344
"""

import numpy as np
import math
import matplotlib.pyplot as plt
import sympy as sym
from scipy import optimize

print('Q2a')
 
#Q2a
# Function to perform calculations 
def calculate(func, lower_limit, upper_limit, interval_limit ): 
      
    interval_size = (float(upper_limit - lower_limit) / interval_limit) 
    sum = func(lower_limit) + func(upper_limit); 
   
    # Calculates value till integral limit 
    for i in range(1, interval_limit ): 
        if (i % 3 == 0): 
            sum = sum + 2 * func(lower_limit + i * interval_size) 
        else: 
            sum = sum + 3 * func(lower_limit + i * interval_size) 
      
    return ((float( 3 * interval_size) / 8 ) * sum )

def f(p):
    inside = lambda x: np.sin(x)*np.cos(p*x)
    return calculate(inside, 0, np.pi, 1000)


def fprime(p):
    inside = lambda x: -x*np.sin(x) *np.sin(p*x) 
    return calculate(inside, 0, np.pi, 1000)

def fsecond(p):
    inside = lambda x: -x**2*np.sin(x)*np.cos(p*x)
    return calculate(inside, 0, np.pi, 1000)

def quadratic_approx(x, x0, f, fprime, fsecond):
    return f(x0)+fprime(x0)*(x-x0)+0.5*fsecond(x0)*(x-x0)**2



def newton(x0, fprime, fsecond, maxiter=100, eps=0.0001):
    x=x0
    for i in range(maxiter):
        xnew=x-(fprime(x)/fsecond(x))
        if xnew-x<eps:
            return xnew
            print('converged')
            break
        x = xnew
    return x

p_min = newton(1.5, fprime, fsecond, 100, 0.0001)
print(p_min)

print()
print('Q2b')
#Q2b

f = lambda x: np.sin(x)*np.cos(p_min*x)

x = optimize.newton(f, np.pi/2)
x_2 = optimize.newton(f, np.pi)
x_3 = optimize.newton(f, 3)
print(x, x_3, x_2)
