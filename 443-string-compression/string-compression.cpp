class Solution {
public:
    int compress(vector<char>& chars) {
        string s;
        char currC = chars[0];
        int currCount = 0;
        s += chars[0];

        // a a b b c c c
        // 
        for (size_t p = 0; p < chars.size(); p++){

            if(currC != chars[p]) {

                if(currCount > 1) s += to_string(currCount);

                s += chars[p];
                currCount = 1;
                currC = chars[p];
            }
            else {  
                currCount ++;
            }
        }
        if(currCount > 1 ) s += to_string(currCount);
        chars.assign(s.begin(), s.end());
        return (int)chars.size();
    }
};