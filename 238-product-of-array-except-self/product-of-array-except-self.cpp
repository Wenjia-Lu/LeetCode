class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        // keep running product
        int n = nums.size();
        vector<int> reverse(n);

        int m = n - 1;
        reverse[m] = 1;

        while(m > 0){
            reverse[m-1] = reverse[m] * nums[m];
            m--;
        }

        vector<int> sol(n);
        m = 1;
        for(int i = 0; i < n; i++){
            sol[i] = reverse[i] * m;
            m *= nums[i];
        }

        return sol;
    }
};