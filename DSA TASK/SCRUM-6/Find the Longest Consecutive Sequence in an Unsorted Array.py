def longest_consecutive_sequence(nums):
    # Create a set from the input list to remove duplicates and allow O(1) lookups
    num_set = set(nums)
    longest_streak = 0

    # Iterate over the set
    for num in num_set:
        # Check if 'num' is the start of a sequence
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1

            # Increment the sequence length if the next consecutive number is found
            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1

            # Update the longest streak found
            longest_streak = max(longest_streak, current_streak)

    return longest_streak

# Example usage
example_input = [100, 4, 200, 1, 3, 2]
example_output = longest_consecutive_sequence(example_input)
print(example_output)  # Output: 4
