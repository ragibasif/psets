"""
* File: main.py
* Author: Ragib Asif
* GitHub: https://github.com/ragibasif
* LinkedIn: https://www.linkedin.com/in/ragibasif/
* SPDX-License-Identifier: MIT
* Copyright (c) 2025 Ragib Asif
* Version 1.0.0
*
* Problem: 0013 - roman_to_integer
* Platform: leetcode
* Difficulty: easy
* URL: https://leetcode.com/problems/roman-to-integer/description/
"""


class Solution:
    def romanToInt(self, s: str) -> int:
        hashmap = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900,
        }
        res = i = 0
        while i < len(s):
            if i <= len(s) - 2:
                temp = s[i] + s[i + 1]
                if temp in hashmap:
                    res -= 2 * hashmap[s[i]]
            res += hashmap[s[i]]
            i += 1
        return res
