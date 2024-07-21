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
                    sLen = to_string(currLen);
                    for(char c : sLen){
                        chars[p1++] = c;
                    }
                }
                if (p2 < chars.size()) {
                    chars[p1] = chars[p2];
                    currChar = chars[p2];
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