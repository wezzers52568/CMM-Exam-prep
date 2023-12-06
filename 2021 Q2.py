# importing modules
import numpy as np
import matplotlib.pyplot as plt
import math

# ------------------------------------------------------
# inputs

# functions that returns dy/dx
# i.e. the equation we want to solve: dy/dx = - y
def model(y,x):
    dydx = 10*(y**(2)) - y**(3)
    return dydx

# initial conditions
x0 = 0
y0 = 0.02
# total solution interval
x_final = 25
# step size
h = 0.01
# ------------------------------------------------------

# ------------------------------------------------------
# Euler method

# number of steps
def ignition(x0, y0, x_final, h):
    n_step = math.ceil(x_final/h)

# Definition of arrays to store the solution
    y_eul = np.zeros(n_step+1)
    x_eul = np.linspace(x0, x_final, n_step+1)

# Initialize first element of solution arrays 
# with initial condition
    y_eul[0] = y0



# Apply Euler method n_step times
    for i in range(n_step):
    # compute the slope using the differential equation
        slope = model(y_eul[i], x_eul[i]) 
    # use the Euler method
        y_eul[i+1] = y_eul[i] + h * slope  
        if slope == 0:
            position = i*h
            break
    
    
    return position

Four_position = int(4/h)
five_position = int(5/h)
ten_position = int(10/h)

print(ignition(x0, 0.02, x_final, h))
print(ignition(x0, 0.01, x_final, h))
print(ignition(x0, 0.005, x_final, h))


plt.figure(figsize = (12,8))

def euler(x0, y0, x_final, h):
    n_step = math.ceil(x_final/h)

# Definition of arrays to store the solution
    y_eul = np.zeros(n_step+1)
    x_eul = np.linspace(x0, x_final, n_step+1)

# Initialize first element of solution arrays 
# with initial condition
    y_eul[0] = y0



# Apply Euler method n_step times
    for i in range(n_step):
    # compute the slope using the differential equation
        slope = model(y_eul[i], x_eul[i]) 
    # use the Euler method
        y_eul[i+1] = y_eul[i] + h * slope  
    
    plt.plot(x_eul, y_eul)
    return

h_max = 0.02
h_range = int(h_max/h)

for i in range(1, h_range): 
    euler(x0, y0, x_final, i)
    
    

"""print(Four_position)
print(y_eul[Four_position])
print(y_eul[five_position])
print(y_eul[ten_position])"""

# ------------------------------------------------------
"""
# ------------------------------------------------------
# super refined sampling of the exact solution 
# n_exact linearly spaced numbers
# only needed for plotting reference solution

# Definition of array to store the exact solution
n_exact = 1000
x_exact = np.linspace(0,x_final,n_exact+1) 
y_exact = np.zeros(n_exact+1)

# exact values of the solution
for i in range(n_exact+1):
    y_exact[i] = y0 * math.exp(-x_exact[i])
# ------------------------------------------------------

# ------------------------------------------------------
# print results on screen
print ('Solution: step x y-eul y-exact error%')
for i in range(n_step+1):
    print(i,x_eul[i],y_eul[i], y0 * math.exp(-x_eul[i]),
            (y_eul[i]- y0 * math.exp(-x_eul[i]))/ 
            (y0 * math.exp(-x_eul[i])) * 100)
# ------------------------------------------------------

# ------------------------------------------------------
# print results in a text file (for later use if needed)
file_name= 'output_h' + str(h) + '.dat' 
f_io = open(file_name,'w') 
for i in range(n_step+1):
    s1 = str(i)
    s2 = str(x_eul[i])
    s3 = str(y_eul[i])
    s4 = s1 + ' ' + s2 + ' ' + s3
    f_io.write(s4 + '\n')
f_io.close()
# ------------------------------------------------------

# ------------------------------------------------------
# plot results
plt.plot(x_eul, y_eul , 'b.-',x_exact, y_exact , 'r-')
plt.xlabel('x')
plt.ylabel('y(x)')
plt.show()
# ------------------------------------------------------


"""