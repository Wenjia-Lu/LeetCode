class Solution:
    def generate(self, numRows: int, ans=None) -> List[List[int]]:
        if ans==None:
            if numRows == 1:
                return [[1]]
            ans = []
        if numRows == 1:
            ans.append([1])
            return
        curr = [1]
        self.generate(numRows - 1, ans)
        above = ans[-1]
        for i in range(len(above) - 1):
            curr.append(above[i] + above[i+1])
        curr.append(1)
        ans.append(curr)
        return ans


# recurrence: an = an-1 .append(curr)
'''
numRows = 3:
    ans = []
    curr = [1]
    above = recurse(numRows = 2, ans = [])
        numRows = 2:
            curr = [1]
            above = recurse(numRows = 1, ans = [])
            numRows = 1:
                ans = [[1]]
'''