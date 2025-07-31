"""
* File: main.py
* Author: Ragib Asif
* GitHub: https://github.com/ragibasif
* LinkedIn: https://www.linkedin.com/in/ragibasif/
* SPDX-License-Identifier: MIT
* Copyright (c) 2025 Ragib Asif
* Version 1.0.0
*
* Problem: 0036 - valid_sudoku
* Platform: leetcode
* Difficulty: medium
* URL: https://leetcode.com/problems/valid-sudoku/description/
"""

# time O(N^2)
# space O(N)


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check that they are numbers
        # check columns for validity
        for i in range(len(board)):  # row
            col_set = set()
            for j in range(len(board[0])):  # col
                if board[i][j] in col_set:
                    return False
                if not (board[i][j] == "."):
                    col_set.add(board[i][j])
        # check rows for validity
        for i in range(len(board[0])):  # col
            row_set = set()
            for j in range(len(board)):  # row
                if board[j][i] in row_set:
                    return False
                if not (board[j][i] == "."):
                    row_set.add(board[j][i])
        # treat each 3x3 as one box
        for i in range(3):
            for j in range(3):
                box_set = set()
                for k in range(i * 3, i * 3 + 3):
                    for m in range(j * 3, j * 3 + 3):
                        if board[k][m] in box_set:
                            return False
                        if not (board[k][m] == "."):
                            box_set.add(board[k][m])
        return True
