import java.util.ArrayList;
import java.util.List;

public class PatternGenerator {

    public static List<Integer> pattern(int n) {
        List<Integer> result = new ArrayList<>();
        generatePattern(n, result, n, true);
        return result;
    }

    private static void generatePattern(int current, List<Integer> result, int initial, boolean decreasing) {
        // Add the current number to the result list
        result.add(current);

        // Base case: if the current number equals the initial value and we are increasing, stop recursion
        if (current == initial && !decreasing) {
            return;
        }

        // Recursive case
        if (decreasing) {
            // If we are decreasing, subtract 5 and check if we need to switch to increasing
            if (current - 5 <= 0) {
                generatePattern(current - 5, result, initial, false);
            } else {
                generatePattern(current - 5, result, initial, true);
            }
        } else {
            // If we are increasing, add 5
            generatePattern(current + 5, result, initial, false);
        }
    }

    public static void main(String[] args) {
        int n = 16;
        List<Integer> result = pattern(n);
        System.out.println(result); // Output: [16, 11, 6, 1, -4, 1, 6, 11, 16]
    }
}
