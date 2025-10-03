class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        memo = [0] * (n+1)
        memo[1] = 1

        for i in range(2, n+1):
            if i % 2 == 0:
                memo[i] = memo[i//2]
            else:
                memo[i] = memo[i-1] + 1
        
        return memo
'''
num -> bin -> numOnes
0 = 0 = 0
1 = 01 = 1
2 = 10 = 1
3 = 11 = 2
4 = 100 = 1
5 = 101 = 2
6 = 110 = 2
7 = 111 = 3
8 = 1000 = 1
9 = 1001 = 2
10 = 1010 = 2
11 = 1011 = 3
12 = 1100 = 2
13 = 1101 = 3
14 = 1110 = 3
15 = 1111 = 4
16 = 10000 = 1

recurrence:
if num is odd:
    recurse(num - 1) + 1
else:
    recurse(num / 2)

dry run:
15: odd, so
    recurse(14) + 1
    14: even, so
        recurse(7)
        7: odd, so
            recurse(6) + 1
            6: even, so
                recurse(3)
                3: odd, so
                    recurse(2) + 1
                    2: even, so
                        recurse(1) = 1
'''