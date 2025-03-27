class Solution(object):
    def minOperations(self, grid, x):
        """
        :type grid: List[List[int]]
        :type x: int
        :rtype: int
        """
        arr = []
        lastRemainder = []

        for row in grid:
            for el in row:
                if len(lastRemainder) == 0:
                    lastRemainder.append(el % x)
                    arr.append(el // x)
                    continue
                
                last = lastRemainder.pop()
                remainder = el % x
                if last != remainder:
                    return -1
                lastRemainder.append(el % x)
                arr.append(el // x)
        
        arr = sorted(arr)
        median = arr[len(arr) // 2]
        
        out = 0
        for elem in arr:
            out += abs(median - elem)
        return out