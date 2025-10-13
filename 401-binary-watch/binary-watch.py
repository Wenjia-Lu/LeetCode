class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        h = [1, 2, 4, 8]
        m = [1, 2, 4, 8, 16, 32]
        result = []

        def dfs(time, start_hr, start_min, count):
            if count == turnedOn:
                hr, mn = time
                if 0 <= hr <= 11 and 0 <= mn <= 59:  # valid time
                    s = f"{hr}:{mn:02d}"
                    if s not in result:
                        result.append(s)
                return
            # try hours
            for i in range(start_hr, len(h)):
                dfs([time[0]+h[i], time[1]], i+1, start_min, count+1)
            # try minutes
            for i in range(start_min, len(m)):
                dfs([time[0], time[1]+m[i]], start_hr, i+1, count+1)

        dfs([0, 0], 0, 0, 0)
        return result