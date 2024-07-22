class Solution {
public:
    int longestOnes(vector<int>& nums, int k) {
        int l = 0;
        int ct = 0;
        int best = 0;
        int z = 0;
        for(size_t r = 0; r < nums.size(); r++){

            if (nums[r]){
                ct++;
            }
            else { // num == 0
                z++;
            }

            if (z > k) { // at 3rd zero
                // if r is last element & [r] == 0

                // dont need this cuz on last loop anyway l "out of bound" doesnt matter
                // if (r == nums.size() - 1){
                //     best = max(best, ct + min(k, z));
                //     return best;
                // }

                while (nums[l++]){ // no boundck needed i think? cuz [r] must be 0
                    ct--;
                }

                // now l must be on a 0
                z--;
            }

            best = max(best, ct + min(k, z));
        }

        return best;
    }
};