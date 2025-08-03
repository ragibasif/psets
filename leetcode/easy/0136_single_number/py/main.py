"""
* File: main.py
* Author: Ragib Asif
* GitHub: https://github.com/ragibasif
* LinkedIn: https://www.linkedin.com/in/ragibasif/
* SPDX-License-Identifier: MIT
* Copyright (c) 2025 Ragib Asif
* Version 1.0.0
*
* Problem: 0136 - single_number
* Platform: leetcode
* Difficulty: easy
* URL: https://leetcode.com/problems/single-number/description/
"""


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # xor - cancels out same numbers
        # time: o(n)
        # space: o(1)
        res = nums[0]
        for i in range(1, len(nums)):
            res ^= nums[i]
        return res
