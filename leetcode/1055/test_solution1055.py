import pytest
from solution1055 import Solution

def test_countCompleteComponents0():
    source = "abc"
    target = "abcab"
    solution = Solution()
    assert solution.shortestWay(source, target) == 2

def test_countCompleteComponents1():
    source = "abc"
    target = "acdbc"
    solution = Solution()
    assert solution.shortestWay(source, target) == -1

def test_countCompleteComponents2():
    source = "xyz"
    target = "xzyxz"
    solution = Solution()
    assert solution.shortestWay(source, target) == 3
