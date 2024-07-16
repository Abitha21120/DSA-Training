import math

def smallest_divisor(nums, threshold):
    def division_sum(divisor):
        return sum(math.ceil(num / divisor) for num in nums)
    
    left, right = 1, max(nums)
    while left < right:
        mid = (left + right) // 2
        if division_sum(mid) <= threshold:
            right = mid  # Try a smaller divisor
        else:
            left = mid + 1  # Increase the divisor
    
    return left

# Test case
nums1 = [1, 2, 5, 9]
threshold1 = 6
print("Input: nums =", nums1, ", threshold =", threshold1)
print("Output:", smallest_divisor(nums1, threshold1))  # Expected output: 5
