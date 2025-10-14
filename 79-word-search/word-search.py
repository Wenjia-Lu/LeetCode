class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ans = [False]
        def dfs(r,c,word):
            if ans[0] == True:
                return

            if word == "":
                ans[0] = ans[0] or True
                return
            
            if not (0 <= r < len(board)) or not (0 <= c < len(board[0])):
                ans[0] = ans[0] or False
                return 

            if board[r][c] != "ZZZ" and board[r][c] == word[0]:
                board[r][c] = "ZZZ"
                dfs(r-1,c,word[1:])
                dfs(r+1,c,word[1:])
                dfs(r,c-1,word[1:])
                dfs(r,c+1,word[1:])
                board[r][c] = word[0]

            else:
                ans[0] = ans[0] or False
                return 


        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == word[0]:
                    dfs(r,c,word)
                    if ans[0]:
                        return True
        return False
        
                
        