def find_pairs_with_sum(nums, target):
    # Create an empty dictionary to store seen elements
    seen = {}
    # Create an empty list to store pairs that sum up to the target
    pairs = []

    # Iterate through each number in the array
    for num in nums:
        # Calculate the complement needed to reach the target sum
        complement = target - num
        # Check if the complement is already in the seen dictionary
        if complement in seen:
            # If yes, add the pair (current number, complement) to the pairs list
            pairs.append((num, complement))
        # Add the current number to the seen dictionary
        seen[num] = True

    # Return the list of pairs
    return pairs

# Example usage:
nums = [1, 2, 3, 4, 5]
target = 5
result = find_pairs_with_sum(nums, target)
print(result)  # Output: [(4, 1), (3, 2)]
