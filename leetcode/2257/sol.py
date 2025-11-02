from typing import List


class Solution:
    GUARDED = 1
    GUARD = 2
    WALL = 3

    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        map = [[0 for x in range(n)] for y in range(m)]
        count = 0

        for wall in walls:
            map[wall[0]][wall[1]] = self.WALL

        for guard in guards:
            map[guard[0]][guard[1]] = self.GUARD

        for guard in guards:
            # mark the places
            x = guard[1]
            y = guard[0]

            # go right
            cur = x + 1
            while cur < n:
                if map[y][cur] == self.GUARD or map[y][cur] == self.WALL:
                    break
                    
                map[y][cur] = 1
                cur += 1
            
            # go left
            cur = x - 1
            while cur >= 0:
                if map[y][cur] == self.GUARD or map[y][cur] == self.WALL:
                    break
                    
                map[y][cur] = 1
                cur -= 1

            # go up 
            cur = y - 1
            while cur >= 0:
                if map[cur][x] == self.GUARD or map[cur][x] == self.WALL:
                    break
                    
                map[cur][x] = 1
                cur -= 1

            # go down
            cur = y + 1
            while cur < m:
                if map[cur][x] == self.GUARD or map[cur][x] == self.WALL:
                    break
                    
                map[cur][x] = 1
                cur += 1
        
        count = 0
        for i in range(m):
            for j in range(n):
                if map[i][j] == 0:
                    count += 1
        
        return count


sol = Solution()

res = sol.countUnguarded(3, 3, [[1,1]], [[0,1],[1,0],[2,1],[1,2]])

print(res)