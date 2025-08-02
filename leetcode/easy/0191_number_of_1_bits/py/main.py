"""
* File: main.py
* Author: Ragib Asif
* GitHub: https://github.com/ragibasif
* LinkedIn: https://www.linkedin.com/in/ragibasif/
* SPDX-License-Identifier: MIT
* Copyright (c) 2025 Ragib Asif
* Version 1.0.0
*
* Problem: 0191 - number_of_1_bits
* Platform: leetcode
* Difficulty: easy
* URL: https://leetcode.com/problems/number-of-1-bits/description/
"""

# time: O (n)
# space: O (1)


class Solution:
    def hammingWeight(self, n: int) -> int:
        counter = 0
        while n:
            counter += n & 1
            n >>= 1
        return counter
