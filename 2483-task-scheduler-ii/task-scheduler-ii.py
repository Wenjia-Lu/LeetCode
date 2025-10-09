class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        # if len(set(tasks)) == 1:
        #     return (len(tasks) - 1) * (space + 1) + 1
        date_last_seen = {} # maps task type : last performed day (ind)
        day = 0
        i = 0
        while i < len(tasks):
            if tasks[i] not in date_last_seen:
                # first task of the type
                # just complete it
                # print(f"date {day + 1}: complete the {i}th task")
                date_last_seen[tasks[i]] = day
                i += 1 # complete the task
                day += 1
            else:
                # task has been seen before
                # so check if space has passed

                if day - date_last_seen[tasks[i]] > space:
                    # good to do the task
                    date_last_seen[tasks[i]] = day
                    i += 1
                    day += 1
                else:
                    # skips
                    # skip until day - date_last_seen[tasks[i]] > space
                    day = space + date_last_seen[tasks[i]] + 1
        return day



        