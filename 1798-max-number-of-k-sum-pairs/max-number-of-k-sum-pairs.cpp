class Solution {
public:
    int maxOperations(vector<int>& nums, int k) {
        sort(nums.begin(), nums.end());
        int p1 = 0;
        int p2 = nums.size() -1;
        int count =0;
        while (p1 < p2){
            int n = nums[p1] + nums[p2];
            if (n > k){
                p2--;
            }
            else if (n < k){
                p1++;
            }
            else {
                count++;
                p1++; p2--;
            }
        }

        return count;
    }
};