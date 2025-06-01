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
* Problem: 3213 - test_problem
* Platform: testing
* Difficulty: t3
* URL: www.example.com
"""
import sys
from os import path


def solve(n: int, array: list[any]) -> None:
    # YOUR CODE HERE
    pass


class Input:

    def file_open(self) -> None:
        if path.exists("input.txt"):
            sys.stdin = open("input.txt", "r")
            sys.stdout = open("output.txt", "w")

    def file_close(self) -> None:
        if path.exists("input.txt"):
            sys.stdin.close()
            sys.stdout.close()

    def input(self) -> sys:
        return sys.stdin.readline().strip()


def main() -> None:
    input = Input()
    input.file_open()
    # t = 1  # single test case
    t = int(input.input())  # multiple test case
    for _ in range(t):
        n = int(input.input())  # number of inputs
        array = list(map(int, input.input().split()))  # inputs in an array
        solve(n, array)
    input.file_close()


if __name__ == "__main__":
    main()
