"""
* File: main.py
* Author: Ragib Asif
* GitHub: https://github.com/ragibasif
* LinkedIn: https://www.linkedin.com/in/ragibasif/
* SPDX-License-Identifier: MIT
* Copyright (c) 2025 Ragib Asif
* Version 1.0.0
*
* Problem: 1108 - defanging_an_ip_address
* Platform: leetcode
* Difficulty: easy
* URL: https://leetcode.com/problems/defanging-an-ip-address/description/
"""


class Solution:
    def defangIPaddr(self, address: str) -> str:
        rep = "[.]"
        res = ""
        for i in address:
            res += rep if i == "." else i
        return res
