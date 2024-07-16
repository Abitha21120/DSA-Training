#include <iostream>
#include <unordered_map>
#include <string>
using namespace std;

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_map<char, int> charIndexMap;
        int maxLength = 0, start = 0;

        for (int end = 0; end < s.size(); ++end) {
            if (charIndexMap.find(s[end]) != charIndexMap.end()) {
                // Move the start point right after the last occurrence of the current character
                start = max(start, charIndexMap[s[end]] + 1);
            }
            charIndexMap[s[end]] = end;
            maxLength = max(maxLength, end - start + 1);
        }

        return maxLength;
    }
};

int main() {
    Solution sol;
    
    string input1 = "abcabcbb";
    cout << "Input: \"" << input1 << "\", Output: " << sol.lengthOfLongestSubstring(input1) << endl; // Expected output: 3


    return 0;
}
