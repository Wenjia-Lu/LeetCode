class Solution {
public:
    bool eq(const string &tmp, const string &str){
        if (str.size() % tmp.size() != 0) return false;
        for(size_t i = 0; i < str.size(); i++){
            if ( tmp[i % tmp.size()] != str[i]) return false;
        }
        return true;
    }

    string gcdOfStrings(string str1, string str2) {
        string ans;
        string tmp;
        size_t i =0;
        string &s = str2;
        if (str1.size() < str2.size()){
            string &s = str1;
        }
        while(i < s.size()){
            tmp += s[i++];
            
            // t divides s calc
            if (eq(tmp, str1) && eq(tmp, str2)){
                ans = tmp;
            }
        }
        return ans;
    }
};