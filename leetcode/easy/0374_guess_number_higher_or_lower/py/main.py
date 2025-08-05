"""
* File: main.py
* Author: Ragib Asif
* GitHub: https://github.com/ragibasif
* LinkedIn: https://www.linkedin.com/in/ragibasif/
* SPDX-License-Identifier: MIT
* Copyright (c) 2025 Ragib Asif
* Version 1.0.0
*
* Problem: 0374 - guess_number_higher_or_lower
* Platform: leetcode
* Difficulty: easy
* URL: https://leetcode.com/problems/guess-number-higher-or-lower/description/
"""

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:


# time: O(log n)
class Solution:
    def guessNumber(self, n: int) -> int:
        l = 1
        r = n
        while l <= r:
            m = (l + r) // 2
            res = guess(m)
            if not res:
                return m
            elif res == 1:
                l = m + 1
            else:
                r = m - 1
        return l
