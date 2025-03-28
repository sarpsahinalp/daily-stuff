from heapq import heappop, heappush


class Solution(object):
    def maxPoints(self, grid, queries):
        """
        :type grid: List[List[int]]
        :type queries: List[int]
        :rtype: List[int]
        """

        # Sort the queries hash them to return the correct solution, since 5 contains 2 etc.
        indexed_queries = list(enumerate(queries))
        sort = sorted(indexed_queries, key=lambda x: x[1])
        # Create a graph out of the edges function able to go left, down, right, up
        # Or act as if its a graph create a visited 
        self.visited = set()

        out = [0] * len(queries)
        frontier = [(grid[0][0], 0, 0)]
        self.visited.add((0, 0))

        sum = 0

        for idx, query in sort:
            sum += self.bfs(frontier, grid, query)
            out[idx] = sum
        # Store the visited in a place
        # Initial idea do bfs with visited for tree like search // is it too slow and too many memort
        # Second idea if the first doesn't pass union find would be suitable with some changes
        return out

        
    
    def bfs(self, frontier, grid, max):
        element_count = 0
        directions = [(0,1), (0,-1), (1,0), (-1,0)]

        while frontier and frontier[0][0] < max:
            val, r, c = heappop(frontier)

            element_count += 1

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and (nr, nc) not in self.visited:
                    self.visited.add((nr, nc))
                    heappush(frontier, (grid[nr][nc], nr, nc))
        
        return element_count
        