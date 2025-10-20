class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        ans = []
        ins = [0] * numCourses
        adjs = [[] for _ in range(numCourses)] # prereq -> courses

        for course, prereq in prerequisites:
            ins[course] += 1
            adjs[prereq].append(course)
        
        q = collections.deque()

        for i, deg in enumerate(ins):
            if deg == 0:
                q.append(i)
        
        print(q, ins, adjs)

        while q:
            prereq = q.popleft()
            ans.append(prereq)
            for course in adjs[prereq]:
                ins[course] -= 1
                if ins[course] == 0:
                    q.append(course)
        
        return ans if len(ans) == numCourses else []
                
        