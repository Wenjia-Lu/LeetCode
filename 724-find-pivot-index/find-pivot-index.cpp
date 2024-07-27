class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        int n = nums.size();
        vector<int> leftSums(n);
        vector<int> rightSums(n);

        leftSums[0] = 0;
        rightSums[n - 1] = 0;

        for(size_t i = 0; i < n - 1; ++i){
            leftSums[i+1] = leftSums[i] + nums[i];
        }
        for(size_t i = n-1; i > 0; --i){
            rightSums[i-1] = rightSums[i] + nums[i];
        }

        for(size_t i = 0; i < n; ++i){
            if(leftSums[i] == rightSums[i]){
                return i;
            }
        }
        
        return -1;

    }
};