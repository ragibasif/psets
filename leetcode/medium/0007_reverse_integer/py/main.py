"""
* File: main.py
* Author: Ragib Asif
* GitHub: https://github.com/ragibasif
* LinkedIn: https://www.linkedin.com/in/ragibasif/
* SPDX-License-Identifier: MIT
* Copyright (c) 2025 Ragib Asif
* Version 1.0.0
*
* Problem: 0007 - reverse_integer
* Platform: leetcode
* Difficulty: medium
* URL: https://leetcode.com/problems/reverse-integer/
"""


# time: O(n), space: O(1)
class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        flag = False
        if x < 0:
            flag = True
            x = abs(x)
        while x:
            res *= 10
            res += x % 10
            x //= 10
        if flag:
            res -= 2 * res
        if not ((-2) ** 31 <= res <= (2**31) - 1):
            return 0
        return res


# second attempt, same solution but using pow function: time: O(n), space: O(1)


class Solution:
    def reverse(self, x: int) -> int:
        bound_left = pow(-2, 31)
        bound_right = pow(2, 31) - 1

        flag = False
        if x < 0:
            flag = True
        temp = abs(x)

        res = 0
        while temp:
            res *= 10
            res += temp % 10
            temp //= 10
        if flag:
            temp = 2 * res
            res -= temp
        if not (res >= bound_left and res <= bound_right):
            return 0
        return res
