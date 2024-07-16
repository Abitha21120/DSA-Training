def find_divisors(N):
    # Initialize an empty list to store the divisors
    divisors = []

    # Loop through all numbers from 1 to the square root of N
    for i in range(1, int(N ** 0.5) + 1):
        if N % i == 0:  # Check if i is a divisor of N
            divisors.append(i)  # Add i to the list of divisors
            if i != N // i:
                divisors.append(N // i)  # Add the corresponding divisor

    # Sort the list of divisors in ascending order
    divisors.sort()
    
    return divisors

# Example usage:
if __name__ == "__main__":
    N = 10  # Sample input
    result = find_divisors(N)
    
    # Print the result
    print(" ".join(map(str, result)))  # Output: 1 2 5 10
