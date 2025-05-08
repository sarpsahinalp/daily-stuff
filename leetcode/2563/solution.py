from typing import List


class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        sortNums = sorted(nums)

        left = 0
        right = len(nums) - 1
        out = 0
        leftMostPossible = -1

        while left < right:
            low = sortNums[left]
            high = sortNums[right]

            summed = low + high

            if summed < lower:
                left += 1
                continue
            
            if summed > upper:
                right -= 1
                continue

            if summed >= lower and summed <= upper:
                out += 1
                leftMostPossible = max(leftMostPossible, left)
        
            left += 1


        return out
    

sol = Solution()
nums = [0,1,7,4,4,5]
lower = 3
upper = 6
print(sol.countFairPairs(nums, lower, upper))

# 0     1 4 4 5 7
# Found       Found