class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # mapping: 2,3,4,5 = a,d,g,j
        # a + (5-2) * 3 = a + 9 = j
        result = []
        def dfs(curr, i):
            if i == len(digits):
                result.append("".join(curr))
                return
            
            digit = int(digits[i])
            start = ord('a') + ((digit - 2) * 3)
            if digit > 7:
                start += 1
            end = start + 3
            if digit == 7 or digit == 9:
                end += 1
            for o in range(start, end):
                dfs(curr + [chr(o)], i+1)
        
        if digits == '':
            return []

        dfs([],0)
        return result


        