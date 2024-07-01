class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        size_t len = word1.size() + word2.size();
        char arr[len+1];
        
        size_t i = 0;
        size_t a = 0;
        size_t b = 0;
        while(i < len){
            if(a < word1.size()) arr[i++] = word1[a++];
            
            if(b < word2.size()) arr[i++] = word2[b++];
        } //
        arr[i] = '\0';
        return string(arr);
    }
};