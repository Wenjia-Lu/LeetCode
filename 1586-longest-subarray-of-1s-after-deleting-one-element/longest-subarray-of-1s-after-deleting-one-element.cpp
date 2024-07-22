class Solution {
public:
int longestOnes(vector<int>& nums, int k) {
        int l = 0;
        int ct = 0;
        int best = 0;
        int z = 0;
        for(size_t r = 0; r < nums.size(); r++){

            if (nums[r] == 1){
                ct++;
            }
            else { // num == 0
                z++;
            }

            if (z > k) { // at 3rd zero
                if (nums[l] == 0){
                    z--;
                } else {
                    ct--;
                }
                l++;
            }

            best = max(best, ct + min(k, z));
        }

        return best;
    }

    int longestSubarray(vector<int>& nums) {
        return longestOnes(nums, 1) - 1;
    }
};