class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        rooms = [0]
        # print(sorted(intervals))
        for start, end in sorted(intervals): # for each new meeting
            # print(f"Interval {(start, end)}")
            found = 0
            for room_number, room_endtime in enumerate(rooms): # go through existing rooms
                if not found and room_endtime <= start:
                    rooms[room_number] = end
                    found = 1
                    # print(f"Room {room_number} now holds {(start, end)}, replacing {room_endtime}")
            if not found: # if no room meets requirement
                rooms.append(end)
                # print(f"New room added to hold {(start, end)}. Total: {len(rooms)}")
        return len(rooms)
