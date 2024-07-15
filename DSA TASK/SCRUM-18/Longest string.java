public class LongestWordFinder {
    public static String solution(String text) {
        // Split the text by non-letter characters to get the words
        String[] words = text.split("[^a-zA-Z]+");

        // Variable to keep track of the longest word found
        String longestWord = "";

        // Iterate through each word in the array
        for (String word : words) {
            // If the current word is longer than the longest word found so far, update longestWord
            if (word.length() > longestWord.length()) {
                longestWord = word;
            }
        }

        // Return the longest word found
        return longestWord;
    }

    public static void main(String[] args) {
        // Example input
        String text1 = "Ready, steady, go!";
        System.out.println(solution(text1)); // Output: steady

        // Additional test cases
        String text2 = "Find the longest word in this sentence!";
        System.out.println(solution(text2)); // Output: sentence

        String text3 = "A quick brown fox jumps over the lazy dog.";
        System.out.println(solution(text3)); // Output: jumps

        String text4 = "Simple test case.";
        System.out.println(solution(text4)); // Output: Simple
    }
}
