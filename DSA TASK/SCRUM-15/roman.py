def int_to_roman(num):
    # List of Roman numeral symbols and their values, sorted in descending order
    roman_numerals = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"),
        (1, "I")
    ]
    
    # Result string to build the Roman numeral
    result = ""
    
    # Iterate through the list of tuples
    for value, symbol in roman_numerals:
        # While the current value can be subtracted from num
        while num >= value:
            result += symbol  # Append the symbol to the result
            num -= value      # Subtract the value from num
    
    return result

# Test cases
print("Test case 1:")
print("Input: num = 3")
print("Output:", int_to_roman(3))  # Expected output: "III"

print("\nTest case 2:")
print("Input: num = 58")
print("Output:", int_to_roman(58))  # Expected output: "LVIII"
