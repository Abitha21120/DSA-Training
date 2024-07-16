#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int i = 0;
        for (int j = 1; j < nums.size(); j++) {
            if (nums[j] != nums[i]) {
                nums[i + 1] = nums[j];
                i++;
            }
        }
        return i + 1;
    }
};

int main() {
    vector<int> nums = {1,2,2,3,3,3,4}; 
    Solution sol;
    int newLength = sol.removeDuplicates(nums);
    
    cout << "The array after removing duplicates:" << endl;
    for (int i = 0; i < newLength; i++) {
        cout << nums[i] << " ";
    }
    cout << endl;
    cout << "New length: " << newLength << endl;

    return 0;
}
