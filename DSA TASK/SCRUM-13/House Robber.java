public class HouseRobber {
    public int rob(int[] nums) {
        // Edge case: if there are no houses, return 0
        if (nums == null || nums.length == 0) {
            return 0;
        }
        
        // Edge case: if there is only one house, return the amount in that house
        if (nums.length == 1) {
            return nums[0];
        }

        // Array to store the maximum amount that can be robbed up to the current house
        int[] dp = new int[nums.length];

        // Initialize the first two values of dp array
        dp[0] = nums[0];
        dp[1] = Math.max(nums[0], nums[1]);

        // Fill in the dp array
        for (int i = 2; i < nums.length; i++) {
            // Either rob this house and add its value to the max robbed up to the house before the previous one,
            // or skip this house and take the max robbed up to the previous house
            dp[i] = Math.max(dp[i-1], nums[i] + dp[i-2]);
        }

        // The last element of dp array contains the maximum amount that can be robbed
        return dp[dp.length - 1];
    }

    public static void main(String[] args) {
        HouseRobber hr = new HouseRobber();

        // Example input 1
        int[] nums1 = {1, 2, 3, 1};
        System.out.println(hr.rob(nums1)); // Output: 4

        // Example input 2
        int[] nums2 = {2, 7, 9, 3, 1};
        System.out.println(hr.rob(nums2)); // Output: 12
    }
}
