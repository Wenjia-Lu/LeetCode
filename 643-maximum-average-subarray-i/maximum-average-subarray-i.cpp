class Solution {
public:
    double findMaxAverage(vector<int>& nums, int k) {
        int p1 = 0;
        int p2 = k;
        double curr = 0;
        for(size_t i = p1; i < p2; i++){
            curr += nums[i];
        }

        double max = curr;

        while(p2 < nums.size()){
            curr -= nums[p1++];
            curr += nums[p2++];
            if (curr > max) max = curr;
        }

        return max/k;
    }
};