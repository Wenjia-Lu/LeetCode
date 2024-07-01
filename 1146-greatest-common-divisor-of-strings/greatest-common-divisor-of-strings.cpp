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
        char* p;
        str1.size() < str2.size() ? p = &str1[0] : p = &str2[0];
        while(i < str1.size() && i < str2.size()){
            tmp += *p;
            i++;
            p++;
            
            // t divides s calc
            if (eq(tmp, str1)&& eq(tmp, str2)){
                ans = tmp;
            }
        }
        return ans;
    }
};