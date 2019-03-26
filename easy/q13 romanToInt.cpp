/* 
Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.
*/

class Solution {
public:
    int romanToInt(string s) {
        int num = 0;
        int index = 0;
        char prev = s[0];
        
        // create a map to easily find the corr. values
        map<char, int> romanMap;
        romanMap['I'] = 1;
        romanMap['V'] = 5;
        romanMap['X'] = 10;
        romanMap['L'] = 50;
        romanMap['C'] = 100;
        romanMap['D'] = 500;
        romanMap['M'] = 1000;
        
        // go through each char in s
        while (index < s.length()) {
            
            char cur = s[index];
            num += romanMap[cur];
            
            if (((cur == 'V') || (cur == 'X')) && (prev == 'I')) {
                num-=2;
            }
            
            else if (((cur == 'L') || (cur == 'C')) && (prev == 'X')) {
                num-=20;
            }
            
            else if (((cur == 'D') || (cur == 'M')) && (prev == 'C')) {
                num-=200;
            }   
            
            prev = cur;
            index++;
        }
        
        return num;
    }
};