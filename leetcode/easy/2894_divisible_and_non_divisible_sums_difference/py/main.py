"""
* File: main.py
* Author: Ragib Asif
* GitHub: https://github.com/ragibasif
* LinkedIn: https://www.linkedin.com/in/ragibasif/
* SPDX-License-Identifier: MIT
* Copyright (c) 2025 Ragib Asif
* Version 1.0.0
*
* Problem: 2894 - divisible_and_non_divisible_sums_difference
* Platform: leetcode
* Difficulty: easy
* URL: https://leetcode.com/problems/divisible-and-non-divisible-sums-difference/description/
"""


class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        num1 = num2 = 0
        for i in range(1, n + 1):
            if i % m != 0:
                num1 += i
            else:
                num2 += i
        return num1 - num2
