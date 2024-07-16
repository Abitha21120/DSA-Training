def is_perfect_number(N):
    """
    Function to check if a number is perfect.
    
    :param N: Integer to be checked
    :return: 1 if the number is perfect, otherwise 0
    """
    if N <= 1:
        return 0
    
    # Initialize sum of factors
    sum_of_factors = 0

    # Iterate through all potential factors
    for i in range(1, N):
        if N % i == 0:
            sum_of_factors += i

    # Check if the sum of factors excluding N is equal to N
    if sum_of_factors == N:
        return 1
    else:
        return 0

# Example 1
example_input1 = 6
print(is_perfect_number(example_input1))  # Output: 1

# Example 2
example_input2 = 10
print(is_perfect_number(example_input2))  # Output: 0
