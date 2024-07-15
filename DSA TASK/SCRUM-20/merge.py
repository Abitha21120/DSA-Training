def merge(intervals):
    # Step 1: Sort the intervals by their start time
    intervals.sort(key=lambda x: x[0])
    
    # Step 2: Initialize the result list with the first interval
    merged_intervals = [intervals[0]]
    
    for current in intervals[1:]:
        # Get the last interval in the result list
        last = merged_intervals[-1]
        
        # If the current interval overlaps with the last interval, merge them
        if current[0] <= last[1]:
            last[1] = max(last[1], current[1])
        else:
            # Otherwise, add the current interval to the result list
            merged_intervals.append(current)
    
    return merged_intervals

# Test case 1
intervals1 = [[1, 3], [2, 6], [8, 10], [15, 18]]
print("Test case 1:")
print("Input:", intervals1)
print("Output:", merge(intervals1))

# Test case 2
intervals2 = [[1, 4], [4, 5]]
print("\nTest case 2:")
print("Input:", intervals2)
print("Output:", merge(intervals2))
