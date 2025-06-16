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
* Problem: 0338 - counting_bits
* Platform: leetcode
* Difficulty: easy
* URL: https://leetcode.com/problems/counting-bits/
"""

# time: O(n)
# space: O(n)


class Solution:
    def countBits(self, n: int) -> List[int]:
        # test bits one at a time starting with the leas significant bit
        res = list()
        for i in range(n + 1):
            num_bits = 0
            x = i
            while x:
                num_bits += x & 1
                x >>= 1
            res.append(num_bits)
        return res
