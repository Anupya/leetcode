/*

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

*/


class Solution {
public:
    bool isValid(string s) {
        // count number of open brackets of each kind
        // keep track of current open bracket expecting a close bracket
        
        vector<int> openBrackets;
        
        // the vector will build like so [(, [, (, {, ... ]
        
        for (int i = 0; i < s.length(); i++) {
            
            if (((s[i] == '(') || (s[i] == '{')) || (s[i] == '[')) {
                openBrackets.push_back(s[i]);
            }
            
            else if (openBrackets.size() == 0) {
                return false;
            }
            
            else if (s[i] == '}') {
                
                if (openBrackets.back() != '{') {
                    return false;
                }
                else {
                    openBrackets.pop_back();
                }
            }
            
            else if ((s[i] == ']') && (openBrackets.back() == '[')) {
                
                openBrackets.pop_back();
            }
            
            else if ((s[i] == '}') && (openBrackets.back() == '{')) {
                
                openBrackets.pop_back();
            }
            
            else if ((s[i] == ')') && (openBrackets.back() == '(')) {
                
                openBrackets.pop_back();
            }
            
            else {
                
                return false;
            }

        }
        
        if (openBrackets.size () == 0) {
            return true;
        }
        
        else {
            return false;
        }
        
        
    }
};