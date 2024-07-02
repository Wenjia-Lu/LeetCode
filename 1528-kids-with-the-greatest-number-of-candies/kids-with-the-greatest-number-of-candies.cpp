class Solution {
public:
    vector<bool> kidsWithCandies(vector<int>& candies, int extraCandies) {
        int most = candies[0];
        for(size_t i = 1; i < candies.size(); i++){
            if (candies[i] > most) most = candies[i];
        }

        vector<bool> arr(candies.size());
        for(size_t i = 0; i < candies.size(); i++){
            if (candies[i] + extraCandies >= most) arr[i] = true;
        }

        return arr;

    }
};