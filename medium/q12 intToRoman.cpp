class Solution {
public:
    // 1 to 3999
    // 509 = 5*100 + 0*10 + 9*1
    string intToRoman(int num) {
        
        string answer;
        
        // map to store (int, string) pairs
        map<int, string> roman = {{1000, "M"}, {500, "D"}, {100, "C"}, {50, "L"}, {10, "X"}, {5, "V"}, {1, "I"}};
        
        string original = to_string(num);
        
        int curDigit = 0;
        int tenMultiple = 10;
        int len = original.length();
        
        for (int i = len; i > 0; i--) {
            tenMultiple = pow(10, i-1);
            
            curDigit = num/tenMultiple;
            
            if (curDigit != 0) {
                int counter = curDigit;
                
                if ((curDigit >= 5) && (curDigit != 9)) {
                    answer.append(roman[5*tenMultiple]);
                    counter-=5;
                }
                
                for (int a = 0; a < counter; a++) {
                
                    if (curDigit == 4) {
                        answer.append(roman[1*tenMultiple]);
                        answer.append(roman[5*tenMultiple]);
                        break;
                    }
                    else if (curDigit == 9) {
                        answer.append(roman[1*tenMultiple]);
                        answer.append(roman[10*tenMultiple]);
                        break;
                    }

                    answer.append(roman[1*tenMultiple]);
                }
            }
            
            // 8 = 58 - 5*10
            num -= curDigit*tenMultiple;
            
            
        }
        
        return answer;
    }
};
