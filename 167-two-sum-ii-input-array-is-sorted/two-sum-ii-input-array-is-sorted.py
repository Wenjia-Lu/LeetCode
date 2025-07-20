class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        first = 0
        last = len(numbers) - 1

        n = numbers[first] + numbers[last]

        while n != target:
            print("n: ", n)
            if n > target:
                last -= 1
            else:
                first += 1
            print("first, last: ", first, " ", last)
            
            n = numbers[first] + numbers[last]
        
        return [first + 1, last + 1]
        