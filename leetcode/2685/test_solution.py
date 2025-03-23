import pytest
from solution import Solution

def test_countCompleteComponents1():
    n = 6
    edges = [[0,1],[0,2],[1,2],[3,4]]
    solution = Solution()
    assert solution.countCompleteComponents(n, edges) == 3

def test_countCompleteComponents2():
    n = 6
    edges = [[0,1],[0,2],[1,2],[3,4],[3,5]]
    solution = Solution()
    assert solution.countCompleteComponents(n, edges) == 1

def test_countCompleteComponents3():
    n = 3
    edges = [[1,0],[2,0]]
    solution = Solution()
    assert solution.countCompleteComponents(n, edges) == 0

def test_countCompleteComponents4():
    n = 4
    edges = [[2,0],[3,1],[3,2]]
    solution = Solution()
    assert solution.countCompleteComponents(n, edges) == 0
