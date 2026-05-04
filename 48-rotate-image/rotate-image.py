class Solution:
    def calc(self, row, col, n):
        # flip across y=x

        # when n = 4
        # (3, 0) -> (0,0)
        # (3,1) -> (1,0)
        # (2,2) -> (2, 1)
        # (2, 3) -> (3, 1)
        # (1, 0) -> (0, 2)

        # when n = 3
        # (0,0) -> (0, 2)
        # (2, 0) -> (0, 0)
        # (0, 2) -> (2, 2)
        return (col, n - 1 - row)

    def rot(self, r, c, n, matrix):
        val = matrix[r][c] # 1
        for _ in range(4):
            # find new location
            # take number at new location
            # put down initial number
            r, c = self.calc(r,c,n) 
            print(f"new coordinate: ({r},{c})...")
            nextVal = matrix[r][c]
            matrix[r][c] = val
            print(f"receives {val}\n")
            val = nextVal

    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # (0,0), (0,1), (1,1)
        n = len(matrix)
        for r in range(n-1): # 1
            for c in range(r, n-1-r): # 
                print(f"!! starts rotation for coor({r},{c})")
                self.rot(r, c, n, matrix)


           

        