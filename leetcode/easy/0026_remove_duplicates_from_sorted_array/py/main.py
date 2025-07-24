"""
* File: main.py
* Author: Ragib Asif
* GitHub: https://github.com/ragibasif
* LinkedIn: https://www.linkedin.com/in/ragibasif/
* SPDX-License-Identifier: MIT
* Copyright (c) 2025 Ragib Asif
* Version 1.0.0
*
* Problem: 0026 - remove_duplicates_from_sorted_array
* Platform: leetcode
* Difficulty: easy
* URL: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
"""


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev: int = 0
        hole: int = 1
        counter: int = 1
        for index in range(1, len(nums)):
            if nums[index] == nums[prev]:
                continue
            else:
                nums[hole] = nums[index]
                prev = hole
                hole += 1
                counter += 1

        return counter
