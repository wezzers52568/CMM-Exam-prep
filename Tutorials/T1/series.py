# importing modules
import numpy as np
import matplotlib.pyplot as plt
import math

N = 100
s = 0
pi_n = np.zeros(N)
nn = np.zeros(N)
error_true = np.zeros(N)
error_ext = np.zeros(N)


for i in range(1,N+1):
    pi_old = (s*6.0)**0.5
    s = s + 1.0/i**2.0
    pi_n[i-1] = (s*6.0)**0.5
    nn[i-1] = i 
    error_true[i-1] = np.absolute(pi_n[i-1] - np.pi)
    error_ext[i-1]  = np.absolute(pi_n[i-1] - pi_old) 
    print(i,pi_n[i-1],error_true[i-1],error_ext[i-1])

plt.figure()
plt.plot(nn,pi_n)

plt.figure()
plt.loglog(nn,error_true,'-b',nn,error_ext,'.r')

plt.show()
