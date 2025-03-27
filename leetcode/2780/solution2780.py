from collections import defaultdict

class Solution(object):
    def minimumIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        first_split_map = defaultdict(int)
        second_split_map = defaultdict(int)
        n = len(nums)

        for el in nums:
            second_split_map[el] += 1
        
        for idx in range(n - 1):
            cur = nums[idx]
            first_split_map[cur] += 1
            second_split_map[cur] -= 1

            if first_split_map[cur] * 2 > idx + 1 and second_split_map[cur] * 2 > n - idx - 1:
                return idx
        
        return -1
        