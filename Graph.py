# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 20:26:05 2023

@author: s2204344
"""
import numpy as np
import matplotlib.pyplot as plt
#numbers
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)



#Code to graph a function



plt.figure()
plt.plot(x, y, label = 'batman')
plt.title('insert title')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(which = 'major')
plt.grid(which = 'minor', linewidth = 0.4)

plt.minorticks_on()