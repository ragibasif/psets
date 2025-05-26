"""
Problem: 1929 concatenation_of_array
Platform: leetcode
Contest/Difficulty: easy
"""

import List


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # just push back the the elements of the current array to itself
        for i in range(len(nums)):
            nums.append(nums[i])
        return nums
