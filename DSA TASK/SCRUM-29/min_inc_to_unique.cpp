#include <bits/stdc++.h>
using namespace std;
using namespace std;

class Solution {
public:
    int minIncrementForUnique(vector<int>& nums) {
        if(nums.empty()) return 0;
        
        sort(nums.begin(), nums.end());
        int moves = 0;
        
        for(int i = 1; i < nums.size(); ++i) {
            if(nums[i] <= nums[i - 1]) {
                int increment = nums[i - 1] - nums[i] + 1;
                nums[i] += increment;
                moves += increment;
            }
        }
        
        return moves;
    }
};

int main() {
    Solution solution;
    
    vector<int> nums1 = {1, 2, 2};
    cout << "Output 1: " << solution.minIncrementForUnique(nums1) << endl; // Output: 1

    vector<int> nums2 = {3, 2, 1, 2, 1, 7};
    cout << "Output 2: " << solution.minIncrementForUnique(nums2) << endl; // Output: 6
    
    return 0;
}
