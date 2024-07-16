public class HouseRobber {

    // Function to find the maximum amount of money you can steal without robbing adjacent houses
    public static int rob(int[] nums) {
        // Edge case: if there are no houses, return 0
        if (nums == null || nums.length == 0) return 0;

        // Edge case: if there is only one house, return the money in that house
        if (nums.length == 1) return nums[0];

        // dp[i] will store the maximum amount of money that can be stolen up to the i-th house
        int[] dp = new int[nums.length];

        // Initialize the dp array
        dp[0] = nums[0];  // Maximum money up to the first house is just the money in the first house
        dp[1] = Math.max(nums[0], nums[1]);  // Maximum money up to the second house is the maximum of the first and second house

        // Fill the dp array
        for (int i = 2; i < nums.length; i++) {
            // For each house, we have two options:
            // 1. Skip the current house and take the maximum money up to the previous house
            // 2. Rob the current house and add its money to the maximum money up to the house before the previous house
            dp[i] = Math.max(dp[i - 1], nums[i] + dp[i - 2]);
        }

        // The last element of dp array contains the maximum money that can be stolen from all the houses
        return dp[dp.length - 1];
    }

    // Main method for testing
    public static void main(String[] args) {
        int[] nums1 = {1, 2, 3, 1};
        System.out.println("Maximum amount of money that can be stolen: " + rob(nums1));  // Output: 4

        int[] nums2 = {2, 7, 9, 3, 1};
        System.out.println("Maximum amount of money that can be stolen: " + rob(nums2));  // Output: 12
    }
}
