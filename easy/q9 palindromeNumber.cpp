/* q9: Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.
*/

class Solution {
public:
    bool isPalindrome(int x) {
        string s1 = to_string(x);
        string s2 = to_string(x);
        int len = s2.length();
        for (int i = 0; i < s1.length(); i++) {
            s2[i] = s1[len-1-i];
        }
        if (s1 == s2) {
            return true;
        }
        return false;
    }
};