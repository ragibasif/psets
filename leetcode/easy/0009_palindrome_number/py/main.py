"""
* File: main.py
* Author: Ragib Asif
* GitHub: https://github.com/ragibasif
* LinkedIn: https://www.linkedin.com/in/ragibasif/
* SPDX-License-Identifier: MIT
* Copyright (c) 2025 Ragib Asif
* Version 1.0.0
*
* Problem: 0009 - palindrome_number
* Platform: leetcode
* Difficulty: easy
* URL: https://leetcode.com/problems/palindrome-number/
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x >= 0 and x <= 9:
            return True
        res = 0
        tmp = x
        while tmp:
            res *= 10
            res += tmp % 10
            tmp //= 10
        return res == x
