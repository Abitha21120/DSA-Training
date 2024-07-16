def longest_consecutive_sequence(nums):
    """
    Function to find the length of the longest consecutive sequence in an unsorted array.
    
    :param nums: List of unsorted integers
    :return: Length of the longest consecutive sequence
    """
    if not nums:
        return 0

    # Convert the list to a set for O(1) lookups
    num_set = set(nums)
    longest_streak = 0

    for num in num_set:
        # Only check for the start of a sequence
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1

            # Check for consecutive numbers
            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1

            # Update the longest streak found
            longest_streak = max(longest_streak, current_streak)

    return longest_streak

# Example input
example_input = [100, 4, 200, 1, 3, 2]

# Function call and output
print(longest_consecutive_sequence(example_input))  # Output: 4
