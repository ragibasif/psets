"""
* File: main.py
* Author: Ragib Asif
* GitHub: https://github.com/ragibasif
* LinkedIn: https://www.linkedin.com/in/ragibasif/
* SPDX-License-Identifier: MIT
* Copyright (c) 2025 Ragib Asif
* Version 1.0.0
*
* Problem: 3467 - transform_array_by_parity
* Platform: leetcode
* Difficulty: easy
* URL: https://leetcode.com/problems/transform-array-by-parity/description/
"""


class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        evens = 0
        odds = 0
        for i in nums:
            if i & 1 == 0:
                evens += 1
            else:
                odds += 1
        res = []
        for j in range(evens):
            res.append(0)
        for k in range(odds):
            res.append(1)
        return res
