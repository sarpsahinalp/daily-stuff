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
        self.visited = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]

        out = [0 for _ in range(len(queries))]
        frontier = []
        if grid[0][0] < sort[0][1]:
                frontier.append((0, 0))
        sum = 0
        for idx, query in sort:
            if len(frontier) == 0 and grid[0][0] < query:
                frontier.append((0, 0))
            frontier, number = self.bfs(frontier, grid, query)
            sum += number
            out[idx] = sum
        # Store the visited in a place
        # Initial idea do bfs with visited for tree like search // is it too slow and too many memort
        # Second idea if the first doesn't pass union find would be suitable with some changes
        return out



    def getPossibleElements(self, grid, i, j, elem, next_run):
        elems = []

        # Somehow check here if it's only because of the maximum number if so add them to the next numbers frontier instead
        
        # Up
        if i > 0 and not self.visited[i-1][j]:
            if grid[i-1][j] < elem:
                elems.append((i-1, j))
            else:
                next_run.append((i-1, j))

        # Down
        if i < len(grid) - 1 and not self.visited[i+1][j]:
            if grid[i+1][j] < elem:
                elems.append((i+1, j))
            else:
                next_run.append((i+1, j))

        # Left
        if j > 0 and not self.visited[i][j-1]: 
            if grid[i][j-1] < elem:
                elems.append((i, j-1))
            else:
                next_run.append((i, j-1))

        # Right
        if j < len(grid[0]) - 1 and not self.visited[i][j+1]:
            if grid[i][j+1] < elem:
                elems.append((i, j+1))
            else:
                next_run.append((i, j+1))

        return elems

        
    
    def bfs(self, frontier, grid, max):
        element_count = 0
        next_run = []
        while len(frontier) != 0:
            cur = frontier.pop(0)

            if self.visited[cur[0]][cur[1]]:
                continue

            if grid[cur[0]][cur[1]] >= max:
                next_run.append(cur)
                continue

            self.visited[cur[0]][cur[1]] = 1
            element_count += 1

            next_elems = self.getPossibleElements(grid, cur[0], cur[1], max, next_run)
            for el in next_elems:
                frontier.append(el)
        
        return next_run, element_count
        