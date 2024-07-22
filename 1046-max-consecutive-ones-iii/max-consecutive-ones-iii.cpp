class Solution {
public:
    int longestOnes(vector<int>& nums, int k) {
        int l = 0;
        int ct = 0;
        int best = 0;
        int z = 0;
        for(size_t r = 0; r < nums.size(); r++){
            nums[r] ? ct++ : z++;

            if (z > k) { // at 3rd zero
                !nums[l] ? z-- : ct--;
                l++;
            }

            best = max(best, ct + min(k, z));
        }

        return best;
    }
};