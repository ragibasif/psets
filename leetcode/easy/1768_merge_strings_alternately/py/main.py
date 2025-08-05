"""
* File: main.py
* Author: Ragib Asif
* GitHub: https://github.com/ragibasif
* LinkedIn: https://www.linkedin.com/in/ragibasif/
* SPDX-License-Identifier: MIT
* Copyright (c) 2025 Ragib Asif
* Version 1.0.0
*
* Problem: 1768 - merge_strings_alternately
* Platform: leetcode
* Difficulty: easy
* URL: https://leetcode.com/problems/merge-strings-alternately/description/
"""


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        l = r = 0
        while l < len(word1) and r < len(word2):
            res += word1[l]
            res += word2[r]
            l += 1
            r += 1
        if l < len(word1):
            res += word1[l:]
        elif r < len(word2):
            res += word2[r:]
        return res
