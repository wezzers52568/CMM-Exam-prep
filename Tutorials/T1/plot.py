# import libraries
import numpy as np
import math
import matplotlib.pyplot as plt

# create array x of coordinate in 0:2pi
n = 20
x = np.linspace(0, 2.0*math.pi, num=n)

# print array to check it is correct
print(x)

# create array y of sine values
y = np.sin(x)

plt.plot(x,y,'.')
plt.xlabel('x')
plt.ylabel('y=sin(x)')


plt.show()
