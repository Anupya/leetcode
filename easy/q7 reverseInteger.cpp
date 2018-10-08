/*

Given a 32-bit signed integer, reverse digits of an integer.

*/


class Solution {
public:
    int reverse(int x) {
        string s = to_string(x);
        string copy = s;
        int len = s.length(); 
        int start = 0;
        
        if (x < 0) {
            start++;
        }
        
        for (int a = start; a < len; a++) {
            if (x < 0) {
                copy[a] = s[len-a];
            }
            else {
                copy[a] = s[len-a-1];
            }
        }
        
        try {
            return stoi(copy);
        }
        catch (out_of_range &e) {
            return 0;
        }      
        
    }
};