# import libraries
import numpy as np
import random

# create array of zeros with n elements
n = 20
x = np.zeros(n)

# print array to check it is correct
print(x)

# populate array with random numbers
random_min = 0
random_max = 10
for i in range(0,n):
    x[i] = random.uniform(random_min,random_max)

# print array to check it is correct
print(x)

# find array positions for which the value is between a and b
a = 5
b = 6
for i in range(0,n):
    if x[i] > a and x[i] < b:
       print(i)
