class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        perRow = []
        res = 0
        for s in bank:
            perRow.append(s.count("1"))
        n = len(perRow)
        for row, num in enumerate(perRow):
            nextRow = row + 1
            while nextRow < n:
                if perRow[nextRow] > 0:
                    res += num * perRow[nextRow]
                    break
                nextRow += 1
        return res
        