"""
* File: main.py
* Author: Ragib Asif
* GitHub: https://github.com/ragibasif
* LinkedIn: https://www.linkedin.com/in/ragibasif/
* SPDX-License-Identifier: MIT
* Copyright (c) 2025 Ragib Asif
* Version 1.0.0
*
* Problem: 0344 - reverse_string
* Platform: leetcode
* Difficulty: easy
* URL: https://leetcode.com/problems/reverse-string/description/
"""


# time: O(n)
# space: O(1)
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l = 0
        r = len(s) - 1
        while l <= r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
