from collections import Counter

def majorityElement(nums):
  """
  This function finds the majority element in a list of integers.

  Args:
      nums: A list of integers.

  Returns:
      The majority element, which appears more than ⌊n / 2⌋ times.
  """
  # Use a dictionary (Counter) to count element occurrences
  counts = Counter(nums)
  # Get the threshold (⌊n / 2⌋)
  threshold = len(nums) // 2
  # Find the element with a count exceeding the threshold
  for num, count in counts.items():
    if count > threshold:
      return num

# Example usage
nums = [3,2,3]
majority = majorityElement(nums)
print(majority)  # Output: 3
