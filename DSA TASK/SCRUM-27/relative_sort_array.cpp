#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> relativeSortArray(vector<int>& arr1, vector<int>& arr2) {
        unordered_map<int, int> order;
        for (int i = 0; i < arr2.size(); ++i) {
            order[arr2[i]] = i;
        }

        auto cmp = [&](int a, int b) {
            if (order.count(a) && order.count(b)) {
                return order[a] < order[b];
            }
            if (order.count(a)) {
                return true;
            }
            if (order.count(b)) {
                return false;
            }
            return a < b;
        };

        sort(arr1.begin(), arr1.end(), cmp);
        return arr1;
    }
};

int main() {
    Solution sol;

    vector<int> arr1_1 = {2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19};
    vector<int> arr2_1 = {2, 1, 4, 3, 9, 6};
    vector<int> result1 = sol.relativeSortArray(arr1_1, arr2_1);
    cout << "Output 1: ";
    for (int num : result1) {
        cout << num << " ";
    }
    cout << endl;

    vector<int> arr1_2 = {28, 6, 22, 8, 44, 17};
    vector<int> arr2_2 = {22, 28, 8, 6};
    vector<int> result2 = sol.relativeSortArray(arr1_2, arr2_2);
    cout << "Output 2: ";
    for (int num : result2) {
        cout << num << " ";
    }
    cout << endl;

    return 0;
}
