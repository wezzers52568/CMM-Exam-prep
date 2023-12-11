import math

x = 0.5
n = 5

# get exact value using 
#intrinsic python function
ex_v = math.e**0.5

# initialise sum
e_to_x = 0

# do iteration n times (from i=0 to i=n-1)
for i in range(n):
    e_to_x = e_to_x + x**i/math.factorial(i)
    print(i,e_to_x,(e_to_x-ex_v) / ex_v)

# compute error
true_rel_error = (e_to_x-ex_v) / ex_v

print('numerical result',e_to_x)
print('exact value', ex_v)
print('true relative error',true_rel_error)



