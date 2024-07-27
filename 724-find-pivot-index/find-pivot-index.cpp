class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        int leftSum = 0;
        int rightSum = 0;
        for(int i : nums){
            rightSum += i;
        }

        for(size_t i = 0; i < nums.size(); ++i){
            if (leftSum == (rightSum - leftSum - nums[i])) return i;
            leftSum += nums[i];
        }

        return -1;

    }
};