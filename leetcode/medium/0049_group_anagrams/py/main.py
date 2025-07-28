"""
* File: main.py
* Author: Ragib Asif
* GitHub: https://github.com/ragibasif
* LinkedIn: https://www.linkedin.com/in/ragibasif/
* SPDX-License-Identifier: MIT
* Copyright (c) 2025 Ragib Asif
* Version 1.0.0
*
* Problem: 0049 - group_anagrams
* Platform: leetcode
* Difficulty: medium
* URL: https://leetcode.com/problems/group-anagrams/
"""

# time: O (n log n)
# space: O (n)


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = dict()
        for s in strs:
            temp = "".join(sorted(s))  # O(n log n)
            if not temp in hashmap:
                hashmap[temp] = []
            hashmap[temp].append(s)
        res = []
        for k, v in hashmap.items():
            res.append(v)
        return res
