class Solution {
public:
    bool isSubsequence(string s, string t) {
        if(!s.size()) return true;

        int j = 0;
        int n = t.size();
        int m = s.size() - 1;
        for (size_t i = 0; i < n; i++){
            if (t[i] == s[j]) j++;
            if (j > m) return true;
        }
        return false;
    }
};