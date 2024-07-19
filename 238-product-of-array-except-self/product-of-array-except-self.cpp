class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        // keep running product
        int n = nums.size();
        vector<int> sol(n);

        sol[--n] = 1;

        while(n > 0){
            sol[n-1] = sol[n] * nums[n];
            n--;
        }

        n = 1;
        for(int i = 0; i < nums.size(); i++){
            sol[i] *= n;
            n *= nums[i];
        }

        return sol;
    }
};