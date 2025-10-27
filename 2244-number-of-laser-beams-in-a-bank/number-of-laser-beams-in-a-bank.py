class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        perRow = []
        res = 0
        for s in bank:
            a = s.count("1")
            if a > 0:
                perRow.append(a)
        n = len(perRow)
        l, r = 0, 1
        while r < n:
            res += perRow[l] * perRow[r]
            l, r = r, r+1
        
        return res
        