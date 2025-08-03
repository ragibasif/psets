"""
* File: main.py
* Author: Ragib Asif
* GitHub: https://github.com/ragibasif
* LinkedIn: https://www.linkedin.com/in/ragibasif/
* SPDX-License-Identifier: MIT
* Copyright (c) 2025 Ragib Asif
* Version 1.0.0
*
* Problem: 0268 - missing_number
* Platform: leetcode
* Difficulty: easy
* URL: https://leetcode.com/problems/missing-number/description/
"""

# time: O(N)
# space: O(1)


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # get sum of 1 to n
        # if sum of 1 to n == sum of nums:
        # then 0 is missing
        sum_of_nat = (len(nums) * (len(nums) + 1)) // 2
        sum_of_nums = sum(nums)

        return sum_of_nat - sum_of_nums
