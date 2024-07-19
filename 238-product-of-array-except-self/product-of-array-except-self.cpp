class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        // keep running product
        // vector<int> forward(nums.size()); 
        int n = nums.size();
        vector<int> reverse(n);


        // int head = 0;
        int m = n - 1;
        // forward[head] = 1; 
        reverse[m] = 1;

        while(m > 0){
            // forward[1] = forward[0] * nums[0] = 1 * nums[0];
            // forward[head+1] = forward[head] * nums[head];
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