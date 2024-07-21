class Solution {
public:
    bool isSubsequence(string s, string t) {
        if(!s.size()) return true;

        int j = 0;
        for (size_t i = 0; i < t.size(); i++){
            if (t[i] == s[j]) j++;
            if (j >= s.size()) return true;
        }
        return false;
    }
};