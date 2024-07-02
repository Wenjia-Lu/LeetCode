class Solution {
public:
    bool isVowel(char c){
        if(c <= 'Z') c += 32;

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

    string reverseVowels(string s) {
        if(s.size() == 1) return s;

        char *front = &s[0];
        char *back = &s[s.size() - 1];

        while (front < back){
            char tmp;
            if (!isVowel(*front)) front++;
            if (!isVowel(*back)) back--;
            if(isVowel(*front) && isVowel(*back)) {
                tmp = *front;
                *front = *back;
                *back = tmp;
                front++;
                back--;
            }
            
        }
        return s;
    }
};