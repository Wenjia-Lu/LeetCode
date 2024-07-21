class Solution {
public:
    double findMaxAverage(vector<int>& nums, int k) {
        int p1 = 0;
        double curr = 0;
        for(; p1 < k; p1++){
            curr += nums[p1];
        }

        double ma = curr;
        p1 = 0;
        while(p1 + k < nums.size()){
            curr = curr + nums[p1 + k] - nums[p1++];
            ma = max(ma, curr);
        }

        return ma/k;
    }
};