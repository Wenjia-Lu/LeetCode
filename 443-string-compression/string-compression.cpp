class Solution {
public:
    int compress(vector<char>& chars) {
        
        size_t p1 = 0;
        size_t p2 = 0;
        size_t currLen = 0;
        char currChar = chars[0];
        string sLen;

        while(p2 <= chars.size()){
            if (p2 == chars.size() || chars[p2] != currChar) {
                p1++;
                if(currLen > 1){
                    // size_t k = 0;
                    // while(currLen){
                    //     chars[p1++] = '0' + (currLen % 10);
                    //     currLen /= 10;
                    //     k++;
                    // }
                    // reverse(chars.begin() + p1 - k, chars.begin() + p1);
                    sLen = to_string(currLen);
                    for(char c : sLen){
                        chars[p1++] = c;
                    }
                }
                if (p2 < chars.size()) {
                    currChar = chars[p2];
                    chars[p1] = currChar;

                } 
                currLen = 1;
            }
            else {
                currLen ++;
            }

            p2++;
        }


        // 
        while(p1 < chars.size()){
            chars.pop_back();
        }

        return (int)chars.size();
    }


};