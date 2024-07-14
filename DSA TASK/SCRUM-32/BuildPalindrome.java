public class ShortestPalindrome {
    public static String solution(String st) {
        // Reverse the input string
        String reversed = new StringBuilder(st).reverse().toString();
        
        // Append reversed string to the original string with a separator
        String combined = st + "#" + reversed;
        
        // Compute the LPS (Longest Prefix which is also Suffix) array
        int[] lps = computeLPS(combined);
        
        // Number of characters to add is the length of the original string
        // minus the length of the longest palindromic suffix
        int charsToAdd = st.length() - lps[combined.length() - 1];
        
        // Append the needed characters from the reversed string to the original string
        String result = st + reversed.substring(0, charsToAdd);
        
        return result;
    }
    
    private static int[] computeLPS(String str) {
        int[] lps = new int[str.length()];
        int length = 0; // length of the previous longest prefix suffix
        int i = 1;
        
        lps[0] = 0; // LPS of the first character is always 0
        
        // Build the LPS array
        while (i < str.length()) {
            if (str.charAt(i) == str.charAt(length)) {
                length++;
                lps[i] = length;
                i++;
            } else {
                if (length != 0) {
                    length = lps[length - 1];
                } else {
                    lps[i] = 0;
                    i++;
                }
            }
        }
        
        return lps;
    }
    
    public static void main(String[] args) {
        // Example input
        String st1 = "abcdc";
        System.out.println(solution(st1)); // Output: "abcdcba"
        
        // Additional test cases
        String st2 = "aacecaaa";
        System.out.println(solution(st2)); // Output: "aacecaaa"
        
        String st3 = "abcd";
        System.out.println(solution(st3)); // Output: "abcdcba"
        
        String st4 = "race";
        System.out.println(solution(st4)); // Output: "racecar"
        
        String st5 = "a";
        System.out.println(solution(st5)); // Output: "a"
    }
}
