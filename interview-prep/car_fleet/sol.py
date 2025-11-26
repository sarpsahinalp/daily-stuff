from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars_times = sorted([[position[i], (target - position[i]) / speed[i]] for i in range(len(position))], key=lambda x: -x[0])

        # [[7, 3.0], [4, 3.0], [1, 4.5], [0, 10.0]]

        stack = []
        out = 0
        for _, time in cars_times:
            if stack:
                # do nothing
                last_time = stack[-1]

                if last_time >= time:
                        continue

            stack.append(time)
            out += 1

        return out  