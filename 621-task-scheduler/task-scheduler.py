class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # thoughts:
        # keep track of how many of each tasks we have
        # cycle through all tasks but prioritizing most freq task off cooldown

        # A: 3
        # B: 3
        # heap: 
        # q: (6, -1, A), (7, -1, B)
        # timer: 5
        # 

        heap = [] # to prioritize most frequent atsk
        q = deque() # keep track of cool down

        count = Counter(tasks) # init heap
        for key in count:
            val = count[key]
            heapq.heappush(heap, (-val, key)) # max heap
        
        timer = -1
        task_completed = 0
        while task_completed < len(tasks):
            timer += 1
            
            if q:
                if q[0][0] <= timer:
                    _, ct2, task_type2 = q.popleft()
                    heapq.heappush(heap, (ct2, task_type2))
                elif not heap:
                    timer = q[0][0] - 1
                    continue

            if not heap:
                continue

            ct, task_type = heapq.heappop(heap)
            ct += 1
            task_completed += 1
            if ct < 0:
                q.append((timer + n + 1, ct, task_type))
            
        return timer + 1


        



        