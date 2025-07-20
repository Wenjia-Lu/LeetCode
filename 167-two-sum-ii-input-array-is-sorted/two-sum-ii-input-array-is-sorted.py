class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        a = 0
        b = len(numbers) - 1

        n = numbers[a] + numbers[b]

        while n != target:
            if n > target:
                b -= 1
            else:
                a += 1
            
            n = numbers[a] + numbers[b]
        
        return [a + 1, b + 1]
        