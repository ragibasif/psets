"""
Problem: 217 contains_duplicate
Platform: leetcode
Contest/Difficulty: easy
"""


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # hashset
        # time: O(N)
        # space: O(N)
        hashset = set()
        for i in nums:
            if i in hashset:
                return True
            hashset.add(i)
        return False
