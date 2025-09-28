class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        stack = []
        p1 = m-1
        p2 = n-1
        for i in range(m + n - 1, -1, -1):
            a = nums1[p1] if p1 > -1 else float('-inf')
            b = nums2[p2] if p2 > -1 else float('-inf')
            if a <= b:
                nums1[i] = b
                p2 -= 1
            else:
                nums1[i] = a
                p1 -= 1
        