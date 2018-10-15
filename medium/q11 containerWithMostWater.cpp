/*
Given n non-negative integers a1, a2, ..., an , where each represents a 
point at coordinate (i, ai). n vertical lines are drawn such that the two 
endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together 
with x-axis forms a container, such that the container contains the most water.
*/

class Solution {
public:
    int maxArea(vector<int>& height) {
        int start;
        int end;
        int product;
        int distance = 1;
        int max = 0;
        
        for(int a = 0; a < height.size(); a++) {
            start = height[a];
            
            
            while (a+distance < height.size()) {
                end = height[a+distance];
                if (start < end) {
                    product = start;
                }
                else {
                    product = end;
                }
                product *= distance;
                
                if (product > max) {
                    max = product;
                }
                distance++;
            }
            distance = 1;
        }

        return max;
        
    }
};