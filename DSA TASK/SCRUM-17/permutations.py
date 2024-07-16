def permute(nums):
  """
  This function generates all permutations of a list of distinct integers.

  Args:
      nums: A list of distinct integers.

  Returns:
      A list of all possible permutations of the input list.
  """
  results = []
  def dfs(current_perm, remaining):
    if not remaining:
      results.append(current_perm.copy())
      return
    for num in remaining:
      current_perm.append(num)
      dfs(current_perm, [n for n in remaining if n != num])
      current_perm.pop()
  dfs([], nums)
  return results

# Example usage
input_list = [1, 2, 3]
permutations = permute(input_list)
print(permutations)
