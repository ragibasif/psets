"""
* File: main.py
* Author: Ragib Asif
* Email: ragib.asif30@myhunter.cuny.edu
* GitHub: https://github.com/ragibasif
* LinkedIn: https://www.linkedin.com/in/ragibasif/
* SPDX-License-Identifier: MIT
* Copyright (c) 2025 Ragib Asif
* Version 1.0.0
*
* Problem: 0242 - valid_anagram
* Platform: leetcode
* Difficulty: easy
* URL: https://leetcode.com/problems/valid-anagram/
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = defaultdict()
        for i in s:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1
        for j in t:
            if j in hashmap:
                hashmap[j] -= 1
            else:
                hashmap[j] = -1
        for k, v in hashmap.items():
            if v != 0:
                return False
        return True
