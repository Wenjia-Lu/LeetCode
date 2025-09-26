class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix[0])-1
        t, b = 0, len(matrix) - 1
        row = -1

        while t <= b:
            mid = t + (b-t)//2
            if matrix[mid][l] <= target <= matrix[mid][r]:
                row = mid
                break
            elif matrix[mid][r] < target:
                t = mid + 1
            elif matrix[mid][l] > target:
                b = mid - 1
        if row == -1:
            return False
        row = matrix[row]
        while l <= r:
            mid = l + (r-l)//2
            if row[mid] < target:
                l = mid + 1
            elif row[mid] > target:
                r = mid - 1
            else:
                return True
        return False
            
        