"""
* File: main.py
* Author: Ragib Asif
* GitHub: https://github.com/ragibasif
* LinkedIn: https://www.linkedin.com/in/ragibasif/
* SPDX-License-Identifier: MIT
* Copyright (c) 2025 Ragib Asif
* Version 1.0.0
*
* Problem: 0509 - fibonacci_number
* Platform: leetcode
* Difficulty: easy
* URL: https://leetcode.com/problems/fibonacci-number/
"""

# recursion, inefficient
# time: O(2^N) (exponential function calls since the function is getting called twice every time it doesn't meet the base case)
# space: O(N) (call stack size)


class Solution1:
    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        return self.fib(n - 1) + self.fib(n - 2)


# iterative dp
# time: O(N)
# space: O(1)


class Solution:
    def fib(self, n: int) -> int:
        # iterative dp, need to keep track of the previous two
        # iterate n times and keep track of previous two integers
        if n == 0 or n == 1:
            return n
        first: int = 0
        second: int = 1
        current: int = 0
        for i in range(2, n + 1):
            current = first + second
            first = second
            second = current
        return current
