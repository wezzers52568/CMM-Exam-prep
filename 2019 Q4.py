# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 12:36:43 2023

@author: s2204344
"""
from scipy import optimize
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize
import sympy as sym
from sympy import Eq
import math
#Q4
theta = np.radians([-30, 0, 30])
R = [6870, 6728, 6615]

C = sym.Symbol('C')
e = sym.Symbol('e')
alpha = sym.Symbol('alpha')


f_1 = sym.Eq(R[0], C/(1+e*sym.sin(theta[0]+alpha))) 
f_2 = sym.Eq(R[1], C/(1+e*sym.sin(theta[1]+alpha)))
f_3 = sym.Eq(R[2], C/(1+e*sym.sin(theta[2]+alpha)))

variables = sym.nsolve((f_1, f_2, f_3), (C, e, alpha), (6800, 0.017, 0))


C = float(variables[0])
e = float(variables[1])
alpha = float(variables[2])

print(C, e, alpha)

def R(theta):
    return C/(1+e*math.sin(theta + alpha))





def gsection(ftn, xl, xm, xr, tol = 1e-9):
   
    
    
    gr1 = 1 + (1 + np.sqrt(5))/2
    #
    # successively refine x.l, x.r, and x.m
    fl = ftn(xl)
    fr = ftn(xr)
    fm = ftn(xm)
    while ((xr - xl) > tol):
        if ((xr - xm) < (xm - xl)):
            y = xm + (xr - xm)/gr1
            fy = ftn(y)
            if (fy >= fm):
                xl = xm
                fl = fm
                xm = y
                fm = fy
            else:
                xr = y
                fr = fy
        else:
            y = xm - (xm - xl)/gr1
            fy = ftn(y)
            if (fy <= fm):
                xr = xm
                fr = fm
                xm = y
                fm = fy
            else:
                xl = y
                fl = fy     
    return(xm, ftn(xm))

theta = gsection(R, 0, 1.56, 3.14)
print(np.degrees(theta[0]), theta[1])