class Solution:
    def isPalindrome(self, s):
        return s == s[::-1]

    def partition(self, s: str) -> List[List[str]]:
        result = []
        curr = []
        def dfs(curr, word):
            if word == "":
                result.append(curr)
                return
            
            for i in range(1, len(word)+1):
                if self.isPalindrome(word[:i]):
                    dfs(curr + [word[:i]], word[i:])
    
        dfs([],s)
        return result


        