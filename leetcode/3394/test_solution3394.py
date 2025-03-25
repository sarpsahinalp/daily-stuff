from solution3394 import Solution
import pytest

def test_checkValidCuts0():
    sol = Solution()
    n = 5
    rectangles = [[1,0,5,2],[0,2,2,4],[3,2,5,3],[0,4,4,5]]
    assert sol.checkValidCuts(n, rectangles) == True

def test_checkValidCuts1():
    sol = Solution()
    n = 4
    rectangles = [[0,0,1,1],[2,0,3,4],[0,2,2,3],[3,0,4,3]]
    assert sol.checkValidCuts(n, rectangles) == True

def test_checkValidCuts2():
    sol = Solution()
    n = 4
    rectangles = [[0,2,2,4],[1,0,3,2],[2,2,3,4],[3,0,4,2],[3,2,4,4]]
    assert sol.checkValidCuts(n, rectangles) == False
    