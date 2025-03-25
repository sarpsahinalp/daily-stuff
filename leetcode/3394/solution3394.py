class Solution(object):
    def checkValidCuts(self, n, rectangles):
        """
        :type n: int
        :type rectangles: List[List[int]]
        :rtype: bool
        """
        horizontalIntervals = []
        verticalIntervals = []

        for start_x, start_y, end_x, end_y in rectangles:
            horizontalIntervals.append([start_y, end_y])
            verticalIntervals.append([start_x, end_x])
        
        horizontalIntervals = sorted(horizontalIntervals)
        verticalIntervals = sorted(verticalIntervals)

        last = [-1, -1]
        count = 0
        for curPair in horizontalIntervals:
            if last[0] == -1 and last[1] == -1:
                last = curPair
                continue
            
            if curPair[0] < last[1]:
                last[1] = max(curPair[1], last[1])
            elif curPair[0] >= last[1]:
                count += 1
                last = curPair
            

            if count == 2:
                return True
        
        last = [-1, -1]
        count = 0
        for curPair in verticalIntervals:
            if last[0] == -1 and last[1] == -1:
                last = curPair
                continue
            
            if curPair[0] < last[1]:
                last[1] = max(curPair[1], last[1])
            elif curPair[0] >= last[1]:
                count += 1
                last = curPair
            

            if count == 2:
                return True

        return False
        