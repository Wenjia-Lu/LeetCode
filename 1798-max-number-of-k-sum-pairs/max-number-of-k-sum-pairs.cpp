class Solution {
public:
    int maxOperations(vector<int>& nums, int k) {
        unordered_map<int, int> map;
        int count = 0;
        for(int n : nums){
            if(map[k - n]){
                count++;
                map[k-n] --; 
            }
            else {
                map[n]++;
            }
        }
        return count;
    }
};