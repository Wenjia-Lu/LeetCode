class Solution {
public:
    bool eq(const string &s, const string &str, size_t len){
        size_t size = str.size();
        for(size_t i = 0; i < size; i++){
            if ( s[i % len] != str[i]) return false;
        }
        return true;
    }

    string gcdOfStrings(string str1, string str2) {
        size_t ans = 0;
        size_t len = 0;
        size_t sz = min(str1.size(), str2.size());
        while(len++ < sz){
            // t divides s calc
            if(str1.size() % len == 0 && str2.size() % len == 0 
                && eq(str2, str1, len) && eq(str1, str2, len)) {
                    ans = len;
                }
        }
        return str1.substr(0,ans);
    }
};