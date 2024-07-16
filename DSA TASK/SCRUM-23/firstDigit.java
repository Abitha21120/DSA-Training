public class LeftmostDigitFinder {
    public static char solution(String inputString) {
        // Iterate through each character in the string
        for (char c : inputString.toCharArray()) {
            // Check if the current character is a digit
            if (Character.isDigit(c)) {
                // Return the first digit found
                return c;
            }
        }
        // Return a placeholder character if no digit is found (assuming input will always contain a digit)
        return ' ';
    }

    public static void main(String[] args) {
        // Example inputs
        String input1 = "var_1__Int";
        System.out.println(solution(input1)); // Output: '1'

        String input2 = "q2q-q";
        System.out.println(solution(input2)); // Output: '2'

        String input3 = "0ss";
        System.out.println(solution(input3)); // Output: '0'

        // Additional test cases
        String input4 = "abc123";
        System.out.println(solution(input4)); // Output: '1'

        String input5 = "no_digits_here";
        System.out.println(solution(input5)); // Output: ' ' (assuming input always has digits)

        String input6 = "123abc";
        System.out.println(solution(input6)); // Output: '1'
    }
}
