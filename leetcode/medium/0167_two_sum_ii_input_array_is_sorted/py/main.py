"""
* File: main.py
* Author: Ragib Asif
* GitHub: https://github.com/ragibasif
* LinkedIn: https://www.linkedin.com/in/ragibasif/
* SPDX-License-Identifier: MIT
* Copyright (c) 2025 Ragib Asif
* Version 1.0.0
*
* Problem: 0167 - two_sum_ii_input_array_is_sorted
* Platform: leetcode
* Difficulty: medium
* URL: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
"""


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # input array sorted: two pointers
        # start at each end, left pointer increments and right pointer decrements until found
        left = 0
        right = len(numbers) - 1
        while left < right:
            temp_sum = numbers[left] + numbers[right]
            if temp_sum == target:
                return [left + 1, right + 1]
            elif temp_sum > target:
                right -= 1
            else:
                left += 1

        return [left + 1, right + 1]
