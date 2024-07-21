class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        // count n while moving nums
        // then put in the zeros
        size_t count = 0;
        size_t pn = 0;
        for(size_t i = 0; i < nums.size(); i++){
            if(nums[i]) {
                nums[pn] = nums[i];
                pn++;
            }
            else {
                count++;
            }
        }

        while(count--){
            nums[pn++] = 0;
        }
    }
};