#include<bits/stdc++.h>
using namespace std;

class Solution{
    public:
    int kth_element_of2_arrays(vector<int> nums1,vector<int> nums2,int k){

        int i=0;  //for 1st array
        int j=0;  //for 2nd array
        int cnt=0;
        while(i < nums1.size() && j < nums2.size()){

            if(nums1[i] > nums2[j]){
                cnt++;
                if(cnt == k) return nums2[j];
                j++; 
            }else{
                cnt++;
                if (cnt ==k) return nums1[i];
                i++;
                
            }

        }
        while(i < nums1.size()){
            cnt++;
            if (cnt ==k) return nums1[i];
            i++;
        }
        while(j < nums2.size()){
            cnt++;
            if (cnt ==k) return nums2[j];
            j++;
        }
        return -1;
    }
};

int main(){
    // test-case : 1
    vector<int> arr1={2,3,6,7,9};  
    vector<int> arr2={1,4,8,10};
    // tets-case : 2
    // vector<int> arr1={100, 112, 256, 349, 770};
    // vector<int> arr2={72, 86, 113, 119, 265, 445, 892};
    // test-case : 3
    // vector<int> arr1={1,3,5};  
    // vector<int> arr2={2,4,6,7,8,9};

    int k;
    cout<< "Enter value of k:";
    cin>>k;
    Solution sol;
    int answer=sol.kth_element_of2_arrays(arr1,arr2,k);

    cout<<"answer is : " << answer;
return 0;    
}