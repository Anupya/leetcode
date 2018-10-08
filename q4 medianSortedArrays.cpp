/*

There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

*/

class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        std::vector<int> new_arr;
        
        int i = 0;
        int j = 0;
        int m = nums1.size();
        int n = nums2.size();
        
        while (i<m && j<n) {
            if (nums1[i] < nums2[j]){
                new_arr.push_back(nums1[i]);
                std::cout << nums1[i] << endl;
                i++;
            }   
            else {
                new_arr.push_back(nums2[j]);
                std::cout << nums2[j] << endl;
                j++;
            }
        }
        
        //append remaining elements in nums1 to new_arr
        if (i<m) {
            for (int a =i; a < m; a++) {
                new_arr.push_back(nums1[a]);
            }
        }
        
        if (j<n) {
            for (int b =j; b < n; b++) {
                new_arr.push_back(nums2[b]);
                std::cout << nums2[b] << endl;
            }
        }
        
        double new_median = 0;
        // divisible by 2, then average the 2 middle indices
        if ((m+n) % 2 == 0) {
            int lower = new_arr[((m+n)/2)-1];
            int higher = new_arr[((m+n)/2)];
            new_median = (lower+higher)/2;
            
            if ((lower%2==0 && higher%2==0) || (lower%2!=0 && higher%2!=0)){
                return new_median;
            }
            else {
                return new_median + 0.5;
            }
        }
        
        // if not, pick the middle index
        else {
            new_median = new_arr[((m+n)/2)];
            return new_median;
            std::cout << new_median << endl;
        }
        
    }
};