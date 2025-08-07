"""
* File: main.py
* Author: Ragib Asif
* GitHub: https://github.com/ragibasif
* LinkedIn: https://www.linkedin.com/in/ragibasif/
* SPDX-License-Identifier: MIT
* Copyright (c) 2025 Ragib Asif
* Version 1.0.0
*
* Problem: 2942 - find_words_containing_character
* Platform: leetcode
* Difficulty: easy
* URL: https://leetcode.com/problems/find-words-containing-character/description/
"""


class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        res = set()
        for i, j in enumerate(words):
            for k in j:
                if k == x:
                    res.add(i)
                    continue
        return list(res)
