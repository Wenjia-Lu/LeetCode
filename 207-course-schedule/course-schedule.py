class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # create adj list (node : prereqs)
        # indegree []
        # create ans vector to store topological order of the courses
        # use queue: enqueue courses with indegree of 0


        # time: O(n * E)
        # space: O(n * E)
        adjs = [[] for _ in range(numCourses)] # prereq -> courses
        ins = [0] * numCourses
        ans = []
        for course, prereq in prerequisites: # O(E)
            ins[course] += 1
            adjs[prereq].append(course)

        q = collections.deque()
        for i, deg in enumerate(ins): # O(n)
            if deg == 0:
                q.append(i)
        
        while q: # O(n)
            prereq = q.popleft() # prereq has no incoming edges
            ans.append(prereq)
            for course in adjs[prereq]: # for each outgoing edge # O(E)
                ins[course] -= 1 # remove incoming from the dest node
                if ins[course] == 0: # new prereq spotted
                    q.append(course)

        return len(ans) == numCourses
        