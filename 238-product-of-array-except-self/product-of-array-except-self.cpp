class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        // keep running product
        int n = nums.size();
        int reverse[n];
        vector<int> sol(n);

        reverse[--n] = 1;

        while(n > 0){
            reverse[n-1] = reverse[n] * nums[n];
            n--;
        }

        n = 1;
        for(int i = 0; i < nums.size(); i++){
            sol[i] = reverse[i] * n;
            n *= nums[i];
        }

        return sol;
    }
};