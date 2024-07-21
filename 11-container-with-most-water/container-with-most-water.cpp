class Solution {
public:
    int maxArea(vector<int>& height) {
        int l = 0;
        int r = height.size() -1;
        int max = 0;
        while (l < r){
            int min;
            if (height[l] < height[r]){
                min = height[l];
                l++;
            }
            else {
                min = height[r];
                r--;
            }
            int a = (r - l + 1) * min;
            if (a > max) max = a;
        }
        return max;
    }
};