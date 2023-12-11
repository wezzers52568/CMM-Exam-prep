# Function that returns the sum of 
# square of first n natural numbers 
def squaresum_odd_alt(n) : 
    # Initialise the sum to 0
    sm = 0
    # Initialise the number counters
    i = 0
    n_odd = 1
    # Iterate with while
    while n_odd <= n:
      i += 1
      if(not (i % 2) == 0):
          sm = sm + (i * i)
          n_odd += 1
    return sm 
  
# Main Program 
# Specify n
n = 20
# Call the function squaresum_odd_alt
sum_numbers = squaresum_odd_alt(n)
# Print result on screen
print(sum_numbers) 
