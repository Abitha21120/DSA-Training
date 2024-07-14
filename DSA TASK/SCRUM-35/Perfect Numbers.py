def is_perfect_number(N):
    # Initialize sum of factors
    sum_of_factors = 0
    
    # Iterate over all numbers from 1 to N-1
    for i in range(1, N):
        # If i is a factor of N, add it to the sum_of_factors
        if N % i == 0:
            sum_of_factors += i
    
    # Check if the sum of factors is equal to the number itself
    if sum_of_factors == N:
        return 1  # The number is perfect
    else:
        return 0  # The number is not perfect

# Example usage
N1 = 6
print(is_perfect_number(N1))  # Output: 1

N2 = 10
print(is_perfect_number(N2))  # Output: 0
