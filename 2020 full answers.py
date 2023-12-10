# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 10:38:39 2023

@author: s2204344
"""

#Q1a
import sympy as sym
from sympy import Symbol, Function
import numpy as np
from scipy import optimize
import math

x = sym.Symbol('x')
y = sym.Symbol('y')
w = sym.Symbol('w')
T_a = sym.Symbol('T_a')
y_0 = sym.Symbol('y_0')

y = (T_a/w) * sym.cosh((w*x)/T_a) + y_0 - T_a/w

dydx = sym.diff(y, x)

dydx2 = sym.diff(dydx, x)

lhs = sym.simplify(dydx2)

print(lhs)

rhs = sym.simplify(w/T_a * (1+(dydx)**2))**0.5

print(rhs)

zero = lhs - rhs
zero = sym.simplify(zero)

print(zero)

#Q1b

x = 50
y = 15
y_0 = 5 
w = 10 

def f(T_a):
    return (T_a/w) * np.cosh((w*x)/T_a) + y_0 - T_a/w - y


T_a = optimize.newton(f, 1000)
print(T_a)

def y(T_a):
    return (T_a/w) * sym.cosh((w*x)/T_a) + y_0 - T_a/w

y_dem = y(T_a)
print(y_dem)

print()
print()

#Q2a

g = 9.81
l = 9.81

def model1(x,y_1,y_2): #y_1 is theta, y_2 is omega
    f_1 = y_2
    f_2 = -g/l * np.sin(y_1)
    return [f_1 , f_2]

def model2(x,y_1,y_2): #y_1 is theta, y_2 is omega
    f_1 = y_2
    f_2 = -g/l * y_1
    return [f_1 , f_2]

def euler_system(model, x0, y0_1, y0_2, x_final, h):
    n_step = math.ceil(x_final/h)

    # Definition of arrays to store the solution
    y_1_eul = np.zeros(n_step+1)
    y_2_eul = np.zeros(n_step+1)
    x_eul = np.zeros(n_step+1)

    # Initialize first element of solution arrays 
    # with initial condition
    y_1_eul[0] = y0_1
    y_2_eul[0] = y0_2
    x_eul[0]   = x0 

    # Populate the x array
    for i in range(n_step):
        x_eul[i+1]  = x_eul[i]  + h

    # Apply Euler method n_step times
    for i in range(n_step):
        # compute the slope using the differential equation
        [slope_1 , slope_2] = model(x_eul[i],y_1_eul[i],y_2_eul[i]) 
        # use the Euler method
        y_1_eul[i+1] = y_1_eul[i] + h * slope_1
        y_2_eul[i+1] = y_2_eul[i] + h * slope_2

    return np.vstack((y_1_eul, y_2_eul))

x0 = 0
y0_1 = np.pi/4
y0_2 = 0
h = 0.001
t_10 = int(10/h)
t_20 = int(20/h)
t_30 = int(30/h)
x_final = 30
r = t_30


model_1 = euler_system(model1, x0, y0_1, y0_2, 30, h)

omega_1_10 = model_1[1,t_10]
omega_1_20 = model_1[1,t_20]
omega_1_30 = model_1[1,t_30]

theta_1_10 = model_1[0,t_10]
theta_1_20 = model_1[0,t_20]
theta_1_30 = model_1[0,t_30]
print('Omega values are', omega_1_10, ',', omega_1_20, 'and', omega_1_30, 'for non-linearised equation at 10, 20, and 30 seconds, respectively')
#print(t_10, t_20, t_30)
print('Theta values are', theta_1_10, ',', theta_1_20, 'and', theta_1_30, 'for non-linearised equation at 10, 20, and 30 seconds, respectively')
model_2 = euler_system(model2, x0, y0_1, y0_2, 30, h)

omega_2_10 = model_2[1,t_10]
omega_2_20 = model_2[1,t_20]
omega_2_30 = model_2[1,t_30]

theta_2_10 = model_2[0,t_10]
theta_2_20 = model_2[0,t_20]
theta_2_30 = model_2[0,t_30]

print()

print('Omega values are', omega_2_10, ',', omega_2_20, 'and', omega_2_30, 'for linearised equation at 10, 20, and 30 seconds, respectively')
#print(t_10, t_20, t_30)
print('Theta values are', theta_2_10, ',', theta_2_20, 'and', theta_2_30, 'for linearised equation at 10, 20, and 30 seconds, respectively')

print()
#Q2b
def period(model1, r, h, y0_1):
    
    x0 = 0
    y0_1 = y0_1
    y0_2 = 0
    h = 0.001
    model_1 = euler_system(model1, x0, y0_1, y0_2, 30, h)

    omega = [0]
    for i in range(1,r):
        if model_1[1, i] < 0.0005 and model_1[1, i] > -0.0005 and model_1[0, i] > 0:
            omega.append(i)
    
    period = omega[1]-omega[0]
    if period <= 2: 
        period = omega[2]-omega[0]
        
    period = period * h

    return period

print('Period (non-linear is', period(model1, r, h, np.pi/4))
print('Period (linear) is', period(model2, r, h,  np.pi/4))
print()
print('Period (nonlinear) if theta_0 is pi/2:', period(model1, r, h, np.pi/2))
print('Period (linear) if theta_0 is pi/2:', period(model2, r, h, np.pi/2))
print()
print('Period (nonlinear) if theta_0 is pi/4:', period(model1, r, h, np.pi/8))
print('Period (linear) if theta_0 is pi/4:', period(model2, r, h, np.pi/8))

print()

#Q3
P = 115000
B = 25500
n = 6
def g(i): 
    return  P*(i*((1+i)**n))/((1+i)**n -1)

def f(i):
    return P*(i*((1+i)**n))/((1+i)**n -1) - B

def fixedPointIteration(x0, e, N):
    print('\n\n*** FIXED POINT ITERATION ***')
    step = 1
    flag = 1
    condition = True
    while condition:
        x1 = g(x0)
        print('Iteration-%d, x1 = %0.6f and f(x1) = %0.6f' % (step, x1, f(x1)))
        x0 = x1

        step = step + 1
        
        if step > N:
            flag=0
            break
        
        condition = abs(f(x1)) > e

    if flag==1:
        print('\nRequired root is: %0.8f' % x1)
    else:
        print('\nNot Convergent.')


interest = optimize.newton(f, -0.1)

print('interest is', interest)
print()

#Q4
u = 1.8 * 10**3
m_0 = 160 * 10**3
q = 2.5 * 10**3

def func(x): 
      
    return u*np.log(m_0/(m_0-q*x)) 
  
# Function to perform calculations 
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
  
# driver function 
interval_limit = 1000
lower_limit = 0
upper_limit = 30

distance = calculate(lower_limit, upper_limit, interval_limit)
print('rocket traveled', distance)

#Q5
h = 1
b = 1
A = 0.01
g = 9.81
h_av = 0.5
v_2 = np.sqrt(2*g*h_av)
Q = A*v_2

#Volume calculations
Volume = np.pi * b**2 * h

t_0 = Volume/Q

t_desired = 2 * t_0

h_av_desired = Volume**2/(A**2*t_desired**2*2*g)

z = 2 * h_av_desired

def b(s):
    return z**3*s**2 + 3*z**2*s + 3*z - Volume/np.pi


s = optimize.newton(b, 100)
print('slope is', s)


