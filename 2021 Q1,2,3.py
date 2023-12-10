# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 14:03:34 2023

@author: s2204344
"""
import sympy as sym
import numpy as np

#Q1a
a = 12
b=1500

p = [1, 2*a, 3*b, a*b, b**2]
roots = np.roots(p)

print(roots)

omega_r = np.real(roots)
omega_j = np.imag(roots)

print()
print('omega_r is', np.unique(omega_r))
print()
print('omega_j is', omega_j[omega_j < 0])

#Q1b

A_j = 0.1
phi_j = np.pi/8

omega_j_2 = np.min(abs(omega_j))
omega_r_2 = -np.min(abs(omega_r))


def func(t): 
      
    return abs(A_j*np.exp(omega_r_2*t)*np.cos(omega_j_2*t+phi_j))

def calculate(lower_limit, upper_limit, interval_limit ): 
      
    interval_size = (float(upper_limit - lower_limit) / interval_limit) 
    sum = func(lower_limit) + func(upper_limit); 
   
    # Calculates value till integral limit 
    for i in range(1, interval_limit ): 
        if (i % 3 == 0): 
            sum = sum + 2 * func(lower_limit + i * interval_size) 
        else: 
            sum = sum + 3 * func(lower_limit + i * interval_size) 
      
    return ((float( 3 * interval_size) / 8 ) * sum ) 


integral = calculate(0, 10, 3000)
work = integral * 100
print()
print('work done', work)


#Q2a

m = 7850
L = 0.9
E = 200 * 10**9
I = 3.255 * 10**-11

def secant_2(f, a, b, iterations):
    c = np.zeros(iterations)
    for i in range(iterations):
        c = a - f(a)*(b - a)/(f(b) - f(a))
        if abs(f(c)) < 1e-13:
            return c
        else: 
            a = b
            b = c
    return c

def f(Beta): 
    return np.cosh(Beta)* np.cos(Beta) + 1

def naive(f, a, b, step_size): 
    array = []
    for i in range(int((b-a)/step_size)):
        f_a = f(a)
        if f_a < 0.001 and f_a > -0.001:
            array.append(round(a, 3))
            array_2 = np.unique(array)
        a = a + step_size
    
    return array_2



zeros = naive(f, 0.1, 10, 0.0001)
print(zeros)

sec = []
for i in range (4):
    sec_2 =round(secant_2(f, 2*i -2, 2*i, 100), 3)
    sec.append(np.unique(sec_2))



sec = np.unique(np.abs(sec))
print(sec)

def g(Beta):
    T = (m*L**3)/(E*I)
    return np.sqrt(Beta**4/T)/(2*np.pi)


frequencies = g(sec)
print(frequencies)
