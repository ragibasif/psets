"""
* File: main.py
* Author: Ragib Asif
* GitHub: https://github.com/ragibasif
* LinkedIn: https://www.linkedin.com/in/ragibasif/
* SPDX-License-Identifier: MIT
* Copyright (c) 2025 Ragib Asif
* Version 1.0.0
*
* Problem: 0771 - jewels_and_stones
* Platform: leetcode
* Difficulty: easy
* URL: https://leetcode.com/problems/jewels-and-stones/
"""


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        hashset = set(jewels)
        res = 0
        for i in stones:
            if i in hashset:
                res += 1
        return res
