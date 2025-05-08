from queue import PriorityQueue
from typing import List

def getPossibleMoves(moveCount, curTime, curPos, moveTimes, width, height, visited):
    result = []
    stepTime = (moveCount % 2) + 1

    for direction in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        new_pos = (curPos[0] + direction[0], curPos[1] + direction[1])
        if new_pos[0] > height - 1 or new_pos[0] < 0 or new_pos[1] > width - 1 or new_pos[1] < 0:
            continue
        move_time = moveTimes[new_pos[0]][new_pos[1]]
        time = max(move_time, curTime) + stepTime
        result.append((time, moveCount + 1, new_pos))

    return result

class Solution:

    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        width = len(moveTime[0])
        height = len(moveTime)
        pq = PriorityQueue()
        pos = (0, 0)
        visited = set()

        # Put value first then the position
        pq.put((0, 0, pos))

        while not pq.empty():
            time, steps, pos = pq.get()

            if pos in visited:
                continue

            visited.add(pos)

            if pos[0] == height - 1 and pos[1] == width - 1:
                return time

            for front in getPossibleMoves(steps, time, pos, moveTime, width, height, visited):
                pq.put(front)

        return 0