def can_balance(weights):
    # Step 1: Calculate the total sum of the array
    total_sum = sum(weights)
    
    # If the total sum is odd, it's impossible to split into two equal sub-arrays
    if total_sum % 2 != 0:
        return False
    
    # Step 2: Iterate through the array and compute prefix sums
    target_sum = total_sum // 2
    current_sum = 0
    
    for weight in weights:
        current_sum += weight
        
        # If the current prefix sum equals half of the total sum, return true
        if current_sum == target_sum:
            return True
    
    # Step 3: If no valid split is found, return false
    return False

# Test cases
print("Test case 1:")
print("Input: [1, 2, 3, 4]")
print("Output:", can_balance([1, 2, 3, 4]))  # Expected output: True

print("\nTest case 2:")
print("Input: [1, 2, 3]")
print("Output:", can_balance([1, 2, 3]))  # Expected output: False
