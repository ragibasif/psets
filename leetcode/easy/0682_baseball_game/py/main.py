"""
* File: main.py
* Author: Ragib Asif
* GitHub: https://github.com/ragibasif
* LinkedIn: https://www.linkedin.com/in/ragibasif/
* SPDX-License-Identifier: MIT
* Copyright (c) 2025 Ragib Asif
* Version 1.0.0
*
* Problem: 0682 - baseball_game
* Platform: leetcode
* Difficulty: easy
* URL: https://leetcode.com/problems/baseball-game/description/
"""


class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for i in operations:
            if i.isalpha():
                if i == "D":
                    stack.append(2 * stack[-1])
                else:
                    stack.pop()
            elif i == "+":
                stack.append(stack[-1] + stack[-2])
            else:
                stack.append(int(i))
        return sum(stack)
