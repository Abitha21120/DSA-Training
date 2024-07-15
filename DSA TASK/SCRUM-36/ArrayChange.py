def solution(inputArray):
    # Initialize the count of moves
    moves = 0
    
    # Iterate through the array starting from the second element
    for i in range(1, len(inputArray)):
        # If the current element is not greater than the previous element
        if inputArray[i] <= inputArray[i - 1]:
            # Calculate the number of moves needed to make the current element greater than the previous element
            needed_moves = inputArray[i - 1] - inputArray[i] + 1
            # Add the needed moves to the current element
            inputArray[i] += needed_moves
            # Increment the total count of moves
            moves += needed_moves
            
    return moves

# Example usage:
if __name__ == "__main__":
    inputArray = [1, 1, 1]  # Sample input
    result = solution(inputArray)
    
    # Print the result
    print(result)  # Output: 3
