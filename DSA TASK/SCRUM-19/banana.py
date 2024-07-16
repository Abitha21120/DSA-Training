def min_eating_speed(piles, h):
    def can_finish(piles, speed, h):
        hours = 0
        for pile in piles:
            hours += (pile + speed - 1) // speed  # Ceiling division to count hours needed for each pile
        return hours <= h

    left, right = 1, max(piles)
    while left < right:
        mid = (left + right) // 2
        if can_finish(piles, mid, h):
            right = mid  # Try a smaller speed
        else:
            left = mid + 1  # Increase the speed
    
    return left

# Test cases
print("Test case 1:")
piles1 = [3, 6, 7, 11]
h1 = 8
print("Input:", piles1, "h =", h1)
print("Output:", min_eating_speed(piles1, h1))  # Expected output: 4

print("\nTest case 2:")
piles2 = [30, 11, 23, 4, 20]
h2 = 6
print("Input:", piles2, "h =", h2)
print("Output:", min_eating_speed(piles2, h2))  # Expected output: 23
