"""
* File: main.py
* Author: Ragib Asif
* Email: ragib.asif30@myhunter.cuny.edu
* GitHub: https://github.com/ragibasif
* LinkedIn: https://www.linkedin.com/in/ragibasif/
* SPDX-License-Identifier: MIT
* Copyright (c) 2025 Ragib Asif
* Version 1.0.0
*
* Problem: 0001 - two_sum
* Platform: leetcode
* Difficulty: easy
* URL: https://leetcode.com/problems/two-sum/
"""


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = defaultdict()
        for i, j in enumerate(nums):
            to_find = target - j
            if to_find in hashmap:
                return [hashmap[to_find], i]
            hashmap[j] = i
