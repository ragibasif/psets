"""
* File: main.py
* Author: Ragib Asif
* GitHub: https://github.com/ragibasif
* LinkedIn: https://www.linkedin.com/in/ragibasif/
* SPDX-License-Identifier: MIT
* Copyright (c) 2025 Ragib Asif
* Version 1.0.0
*
* Problem: 0028 - find_the_index_of_the_first_occurrence_in_a_string
* Platform: leetcode
* Difficulty: easy
* URL: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        res = -1
        for i in range(len(haystack) - len(needle) + 1):
            temp = ""
            for j in range(len(needle)):
                temp += haystack[i + j]
            if temp == needle:
                res = i
                return res
        return res
