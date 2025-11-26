from typing import List


class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        intervals = []

        intervals.append([timeSeries[0], timeSeries[0] + duration])

        for i in range(1, len(timeSeries)):
            last = intervals[-1]
            cur_interval = [timeSeries[i], timeSeries[i] + duration]

            if last[1] > cur_interval[0]:
                last[1] = cur_interval[1]
            else:
                intervals.append(cur_interval)

        return sum(interval[1] - interval[0] for interval in intervals)