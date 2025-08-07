"""
* File: main.py
* Author: Ragib Asif
* GitHub: https://github.com/ragibasif
* LinkedIn: https://www.linkedin.com/in/ragibasif/
* SPDX-License-Identifier: MIT
* Copyright (c) 2025 Ragib Asif
* Version 1.0.0
*
* Problem: 1512 - number_of_good_pairs
* Platform: leetcode
* Difficulty: easy
* URL: https://leetcode.com/problems/number-of-good-pairs/description/
"""


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        res = 0
        for i in range(1, len(nums)):
            for j in range(i, len(nums)):
                if nums[i - 1] == nums[j]:
                    res += 1
        return res
