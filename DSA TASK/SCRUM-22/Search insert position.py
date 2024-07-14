class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        # Initialize left and right pointers
        l, r = 0, len(nums)
        
        # Binary search loop
        while l < r:
            # Calculate middle index
            mid = (l + r) >> 1  # Equivalent to (l + r) // 2
            
            # Check if target is found or where it should be inserted
            if nums[mid] >= target:
                r = mid  # Move the right boundary to search in the left half
            else:
                l = mid + 1  # Move the left boundary to search in the right half
        
        # Return the insertion index
        return l

# Read input
nums = list(map(int, input().split()))
target = int(input())

# Create an instance of Solution class
solution = Solution()

# Call searchInsert method and print the result
print(solution.searchInsert(nums, target))
