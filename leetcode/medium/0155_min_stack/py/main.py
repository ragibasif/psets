"""
* File: main.py
* Author: Ragib Asif
* GitHub: https://github.com/ragibasif
* LinkedIn: https://www.linkedin.com/in/ragibasif/
* SPDX-License-Identifier: MIT
* Copyright (c) 2025 Ragib Asif
* Version 1.0.0
*
* Problem: 0155 - min_stack
* Platform: leetcode
* Difficulty: medium
* URL: https://leetcode.com/problems/min-stack/description/
"""


# main stack keeps track of elements
# min stack keeps track of min elements
# user only knows about the main stack, the min stack is internal
# operations are done as if only the main stack exists
# this is a regular stack that also knows the minimum element
class MinStack:

    def __init__(self):
        self.buffer = []
        self.min_buffer = []

    def push(self, val: int) -> None:
        self.buffer.append(val)
        if not len(self.min_buffer):
            self.min_buffer.append(val)
        else:
            self.min_buffer.append(min(self.min_buffer[-1], val))

    def pop(self) -> None:
        self.buffer.pop()
        self.min_buffer.pop()

    def top(self) -> int:
        return self.buffer[-1]

    def getMin(self) -> int:
        return self.min_buffer[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
