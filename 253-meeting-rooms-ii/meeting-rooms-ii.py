class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        rooms = [0]
        intervals.sort(key = lambda interval: interval[0]) # O(n log n to sort)
        for start, end in intervals: # O(n) to go thru
            found = 0
            if rooms[0] <= start:
                heapq.heappop(rooms)
                heapq.heappush(rooms, end)
            else:
                heapq.heappush(rooms, end)
        return len(rooms)
