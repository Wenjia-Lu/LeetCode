class Solution {
public:
    double findMaxAverage(vector<int>& nums, int k) {
        int p1 = 0;
        double curr = 0;
        for(size_t i = 0; i < k; i++){
            curr += nums[i];
        }

        double ma = curr;

        while(p1 + k < nums.size()){
            curr += nums[p1 + k];
            curr -= nums[p1++];
            ma = max(ma, curr);
        }

        return ma/k;
    }
};