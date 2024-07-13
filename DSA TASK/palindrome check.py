def is_palindrome(text):

  text = ''.join(char.lower() for char in text if char.isalnum())

  return text == text[::-1]


print(is_palindrome("racecar"))
print(is_palindrome("hello"))   
print(is_palindrome("A man, a plan, a canal: Panama")) 
