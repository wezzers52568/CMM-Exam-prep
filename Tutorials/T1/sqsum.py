# Return the sum of 
# square of first n 
# natural numbers 
def squaresum(n) : 
  
    # Iterate i from 1  
    # to n finding  
    # the square of i and 
    # add to sum. 
    sm = 0
    for i in range(1, n+1) :
        if (not(i%2) == 0):
            sm = sm + (i * i) 
            
    return sm 
  
# Main Program 
n = 20
sum_numbers = squaresum(n)
print(sum_numbers) 
