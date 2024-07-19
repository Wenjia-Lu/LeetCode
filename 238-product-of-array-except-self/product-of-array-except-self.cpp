class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        // keep running product
        vector<int> forward(nums.size()); 
        vector<int> reverse(nums.size());

        int head = 0;
        int tail = nums.size() -1;

        forward[head] = 1; reverse[tail] = 1;

        while(tail > 0){
            // forward[1] = forward[0] * nums[0] = 1 * nums[0];
            forward[head+1] = forward[head] * nums[head];
            reverse[tail-1] = reverse[tail] * nums[tail];

            head++; tail--;
        }

        vector<int> sol(nums.size());
        for(int i = 0; i < sol.size(); i++){
            sol[i] = forward[i] * reverse[i];
        }

        return sol;
    }
};