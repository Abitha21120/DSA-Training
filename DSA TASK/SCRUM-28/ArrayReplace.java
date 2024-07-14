import java.util.Arrays;

public class ElementReplacer {
    public static int[] solution(int[] inputArray, int elemToReplace, int substitutionElem) {
        // Iterate through each element in the input array
        for (int i = 0; i < inputArray.length; i++) {
            // If the current element matches elemToReplace, replace it with substitutionElem
            if (inputArray[i] == elemToReplace) {
                inputArray[i] = substitutionElem;
            }
        }
        // Return the modified array
        return inputArray;
    }

    public static void main(String[] args) {
        // Example input
        int[] inputArray1 = {1, 2, 1};
        int elemToReplace1 = 1;
        int substitutionElem1 = 3;
        System.out.println(Arrays.toString(solution(inputArray1, elemToReplace1, substitutionElem1))); // Output: [3, 2, 3]

        // Additional test cases
        int[] inputArray2 = {4, 5, 6, 4, 4};
        int elemToReplace2 = 4;
        int substitutionElem2 = 7;
        System.out.println(Arrays.toString(solution(inputArray2, elemToReplace2, substitutionElem2))); // Output: [7, 5, 6, 7, 7]

        int[] inputArray3 = {0, 0, 0};
        int elemToReplace3 = 0;
        int substitutionElem3 = 1;
        System.out.println(Arrays.toString(solution(inputArray3, elemToReplace3, substitutionElem3))); // Output: [1, 1, 1]

        int[] inputArray4 = {9, 8, 7, 6};
        int elemToReplace4 = 10;
        int substitutionElem4 = 5;
        System.out.println(Arrays.toString(solution(inputArray4, elemToReplace4, substitutionElem4))); // Output: [9, 8, 7, 6] (no changes)
    }
}
