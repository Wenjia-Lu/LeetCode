class Solution {
public:
    // if is water, then add 1 to param
    int isWater(vector<vector<int>>& grid, int r, int c){
        if (r < 0 || r >= grid.size()) return 1;
        if (c < 0 || c >= grid[0].size()) return 1;
        return (grid[r][c] + 1 ) % 2;
    }

    int islandPerimeter(vector<vector<int>>& grid) {
        int param = 0;

        for(int r = 0; r < grid.size(); r++){
            for(int c = 0; c < grid[0].size(); c++){
                if (grid[r][c]){
                    param += isWater(grid, r-1, c);
                    param += isWater(grid, r+1, c);
                    param += isWater(grid, r, c-1);
                    param += isWater(grid, r, c+1);
                }
            }
        }
        return param;
    }
};