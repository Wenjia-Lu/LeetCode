class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        map<int, int> hash;

        priority_queue<int> freq; 
        for(int i = 0; i < k; i++){
            freq.push(0); // freq = [0, 0]
        }

        for(size_t i = 0; i < nums.size(); i++){
            int n = nums[i];
            hash[n] ++;
        }   

        for( auto kv : hash){
            freq.push(kv.second); // [2, 2, 3]
        }

        int min = 0;
        for(int i = 1 ; i < k; i++){
            freq.pop();
        }
        min = freq.top();

        vector<int> indices;
        indices.reserve((size_t)k);

        for( auto kv : hash){
            if (kv.second >= min) {
                indices.push_back(kv.first);
            }
        }
        
        return indices;
    } //
};