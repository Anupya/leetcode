/*
q27: Given an array nums and a value val, remove all 
instances of that value in-place and return the new length.
*/

class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int length = nums.size();
        int counter = 0;
        
        // modify nums
        for (int a = 0; a < nums.size(); a++) {
            
            if (nums[a] == val) {
                length--;
            }
            else {
                nums[counter] = nums[a];
                counter++;
            }
        }
        
        return length;
    }
};