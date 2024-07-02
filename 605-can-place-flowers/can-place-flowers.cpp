class Solution {
public:
    bool isValid(vector<int>& flowerbed, size_t i){
        if( i == 0 || flowerbed[i-1] == 0){
            if (i == flowerbed.size() - 1 || flowerbed[i+1] == 0){
                return true;
            }
        }
        return false;
    }
    
    bool canPlaceFlowers(vector<int>& flowerbed, int n) {
        if (n == 0) return true;
        for(size_t i = 0; i < flowerbed.size(); i++){
            if (flowerbed[i] == 0 && isValid(flowerbed, i)) {
                flowerbed[i] = 1;
                n--;
                if(!n) return true;
            }
        }

        return false;
    }
};