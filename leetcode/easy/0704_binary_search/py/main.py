"""
* File: main.py
* Author: Ragib Asif
* GitHub: https://github.com/ragibasif
* LinkedIn: https://www.linkedin.com/in/ragibasif/
* SPDX-License-Identifier: MIT
* Copyright (c) 2025 Ragib Asif
* Version 1.0.0
*
* Problem: 0704 - binary_search
* Platform: leetcode
* Difficulty: easy
* URL: https://leetcode.com/problems/binary-search/description/
"""


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # time: O(log n)
        # space: O(1)
        left = 0
        right = len(nums) - 1
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] == target:
                return middle
            elif nums[middle] > target:
                right = middle - 1
            else:
                left = middle + 1
        return -1
