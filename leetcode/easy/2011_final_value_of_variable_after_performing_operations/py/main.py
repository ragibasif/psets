"""
* File: main.py
* Author: Ragib Asif
* GitHub: https://github.com/ragibasif
* LinkedIn: https://www.linkedin.com/in/ragibasif/
* SPDX-License-Identifier: MIT
* Copyright (c) 2025 Ragib Asif
* Version 1.0.0
*
* Problem: 2011 - final_value_of_variable_after_performing_operations
* Platform: leetcode
* Difficulty: easy
* URL: https://leetcode.com/problems/final-value-of-variable-after-performing-operations/
"""


class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        res = 0
        for i in operations:
            if i[1] == "+":
                res += 1
            else:
                res -= 1
        return res
