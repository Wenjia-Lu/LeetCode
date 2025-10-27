class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        perRow = []
        res = 0
        for s in bank:
            a = s.count("1")
            if a > 0:
                perRow.append(a)
        n = len(perRow)
        for i in range(n-1):
            res += perRow[i] * perRow[i+1]
        
        return res
        