class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        // keep running product
        vector<int> forward(nums.size()+2, 1); 
        vector<int> reverse(nums.size()+2, 1);

        int head = 0;
        int tail = nums.size() + 1; // - 1 + 2
        while(tail > 1){
            // forward[1] = forward[0] * nums[0] = 1 * nums[0];
            forward[head+1] = forward[head] * nums[head];
            reverse[tail-1] = reverse[tail] * nums[tail-2];

            head++; tail--;
        }

        vector<int> sol(nums.size());
        for(int i = 0; i < sol.size(); i++){
            sol[i] = forward[i] * reverse[i+2];
        }

        return sol;
    }
};