# Function that returns the sum of 
# square of first n natural numbers 
def squaresum_odd(n) : 
    # Initialise the sum to 0
    sm = 0
    # Iterate i from 1  
    # to n finding  
    # the square of i and 
    # add to sum. 
    for i in range(1, n+1) : 
        # Check if the current value 
        # of i is odd
        if(not (i % 2) == 0):
            sm = sm + (i * i) 
           
    return sm 
   
# Main Program 
# Specify n
n = 20
# Call the function squaresum_odd
sum_numbers = squaresum_odd(n)
# Print result on screen
print(sum_numbers) 
