class Solution {
public:
    bool isV(char c){
        switch(c){
            case 'a':
                return true;
            case 'e':
                return true;
            case 'i':
                return true;
            case 'o':
                return true;
            case 'u':
                return true;
        }
        return false;
    }
    int maxVowels(string s, int k) {
        int ct = 0;
        for(size_t i = 0; i < k; i++){
            if (isV(s[i])) ct++;
        }
        int m = ct;
        for(size_t i = 0; i + k < s.size(); i++){
            if (isV(s[i])) ct --;
            if (isV(s[i + k])) ct ++;
            m = max(ct, m);
            if ( m == k) return m;
        }

        return m;
    }
};