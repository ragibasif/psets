"""
* File: main.py
* Author: Ragib Asif
* GitHub: https://github.com/ragibasif
* LinkedIn: https://www.linkedin.com/in/ragibasif/
* SPDX-License-Identifier: MIT
* Copyright (c) 2025 Ragib Asif
* Version 1.0.0
*
* Problem: 3477 - fruits_into_baskets_ii
* Platform: leetcode
* Difficulty: easy
* URL: https://leetcode.com/problems/fruits-into-baskets-ii/description/
"""

# time: O(n ^ 2)
# space: O(1)


class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        counter = len(baskets)
        for i in fruits:
            j = 0
            while j < len(baskets):
                if baskets[j] and baskets[j] >= i:
                    baskets[j] = None
                    counter -= 1
                    break
                j += 1
        return counter
