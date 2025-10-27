class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        perRow = []
        res = 0
        above, below = -1, -1
        for s in bank:
            ones = s.count("1")
            if ones == 0:
                continue
            if above == -1:
                above = ones
            else:
                below = ones
                res += above * below
                above = below
        return res