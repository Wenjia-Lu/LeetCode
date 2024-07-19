class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        // keep running product
        int n = nums.size();
        vector<int> sol(n);

        int m = n -1;
        sol[m] = 1;

        while(m > 0){
            sol[m-1] = sol[m] * nums[m];
            m--;
        }

        m = 1;
        for(int i = 0; i < n; i++){
            sol[i] *= m;
            m *= nums[i];
        }

        return sol;
    }
};