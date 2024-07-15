def find_minimum(arr):
  """Finds the minimum element in a given array of integers.

  Args:
      arr: A list of integers.

  Returns:
      The minimum element in the array, or None if the array is empty.
  """

  if not arr:  # Handle empty array gracefully
    return None

  minimum = arr[0]
  for num in arr:
    if num < minimum:
      minimum = num
  return minimum

# Example usage
arr = [1, 2, 3, 4, 5]
min_element = find_minimum(arr)
print("Minimum element:", min_element)  # Output: Minimum element: 1

# Test case for empty array
empty_arr = []
min_element = find_minimum(empty_arr)
print("Minimum element in empty array:", min_element)  # Output: Minimum element in empty array: None
