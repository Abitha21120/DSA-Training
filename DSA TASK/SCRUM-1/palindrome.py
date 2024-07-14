def is_palindrome(text):
  """
  Checks if a given string is a palindrome.

  Args:
      text: The string to check.

  Returns:
      True if the text is a palindrome, False otherwise.
  """

  # Make the text lowercase and remove all non-alphanumeric characters.
  text = ''.join(char.lower() for char in text if char.isalnum())

  # Check if the text is the same forwards and backwards.
  return text == text[::-1]

# Test cases
print(is_palindrome("racecar"))  # Output: True
print(is_palindrome("hello"))    # Output: False
print(is_palindrome("A man, a plan, a canal: Panama"))  # Output: True (ignoring punctuation)
