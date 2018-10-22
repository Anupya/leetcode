/*
Given a sorted array nums, remove the duplicates in-place 
such that each element appear only once and return the new 
length.
*/
class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int length = 1;
        
        if (nums.size() == 0) {
            return 0;
        }
        for (int a = 1; a < nums.size(); a++) {
            if (nums[a-1] == nums[a]) {
                nums.erase (nums.begin()+a);
                a--;
            }
            else {
                length++;
            }
        }
        return length;
    }
};