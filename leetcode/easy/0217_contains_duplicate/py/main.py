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
* Problem: 0217 - contains_duplicate
* Platform: leetcode
* Difficulty: easy
* URL: https://leetcode.com/problems/contains-duplicate/
"""


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        temp = set(nums)
        return len(nums) != len(temp)
