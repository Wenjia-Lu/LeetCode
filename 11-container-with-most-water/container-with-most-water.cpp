class Solution {
public:
    int maxArea(vector<int>& height) {
        int l = 0;
        int r = height.size() -1;
        int max = 0;
        int min = 0; int a= 0;
        while (l < r){
            if (height[l] < height[r]){
                min = height[l];
                l++;
            }
            else {
                min = height[r];
                r--;
            }
            a = (r - l + 1) * min;
            if (a > max) max = a;
        }
        return max;
    }
};