class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        
        map< vector<char>, vector<string> > map;
        for(string str : strs){
            vector<char> c(26, 0);
            for(size_t i = 0; i < str.size(); i++){
                c[ str[i] - 'a' ] ++;
            }
            map[c].push_back(str);
        }
        vector< vector<string> > solution;
        for (auto kv : map){
            solution.push_back(kv.second);
        }
        return solution;
    }
};