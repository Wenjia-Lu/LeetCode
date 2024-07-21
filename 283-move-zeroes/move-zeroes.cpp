class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        size_t p1 = 0;
        size_t p2 = 0;
        for(size_t p2 = 0; p2 < nums.size(); p2++){
            if (nums[p2] != 0){
                swap(nums[p1], nums[p2]);
                p1++;
            }
        }
    }
};