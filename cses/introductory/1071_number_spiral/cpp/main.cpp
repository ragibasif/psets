/*
 * File: main.cpp
 * Author: Ragib Asif
 * Email: ragib.asif30@myhunter.cuny.edu
 * GitHub: https://github.com/ragibasif
 * LinkedIn: https://www.linkedin.com/in/ragibasif/
 * SPDX-License-Identifier: MIT
 * Copyright (c) 2025 Ragib Asif
 * Version 1.0.0
 *
 * Problem: 1071 - number_spiral
 * Platform: cses
 * Difficulty: introductory
 * URL: https://cses.fi/problemset/task/1071
 */

/******************************************************************************/
/*                                  INCLUDES                                  */
/******************************************************************************/

#include <algorithm>  // sort, binary_search, lower_bound, upper_bound, shuffle
#include <bitset>     // bitset - for binary data
#include <cassert>    // assert - for debugging
#include <chrono>     // chrono::steady_clock, chrono::system_clock
#include <climits>    // INT_MAX, INT_MIN
#include <cmath>      // sqrt, pow, abs
#include <cstdint>    // int64_t, uint64_t, etc. - fixed-width integer types
#include <functional> // greater, less - function objects and operations
#include <iostream>   // cout, cin, endl - Input/Output
#include <iterator>   // iterators and related items
#include <map>     // map, multimap - (non-hashed, tree) ordered key-value pairs
#include <numeric> // accumulate, gcd, lcm - numeric operations
#include <queue>   // queue, priority_queue
#include <random>  // mt19937, mt19937_64 (higher quality RNG than rand())
#include <set>     // set, multiset - (non-hashed, tree) ordered set
#include <stack>   // stack
#include <string>  // string
#include <tuple>
#include <unordered_map> // unordered_map - hash map
#include <unordered_set> // unordered_set - hash set
#include <utility>       // pair
#include <vector>        // vector - dynamic array

using namespace std;

/******************************************************************************/
/*                                   INPUT                                    */
/******************************************************************************/

// #include "dbg.h" // comment out before submitting

// R, C, (R,C), eq
// 1, 1,    01| 2^0 = 1
// 1, 2,    01| 2^1 = 2
// 1, 3,    09| 2^3 + 2^0 = 8 + 1 = 9
// 1, 4,    10| 2^3 + 2^1 = 8 + 2 = 10
// 1, 5,    25| 2^4 + 2^3 + 2^0= 16 + 8 + 1 = 25
// 2, 3,    08| 2^3 = 8
// 4, 2,    15| 2^3 + 2^2 + 2^1 + 2^0= 8 + 4 + 2 + 1 = 15
// 2, 2,    03| 2^1 + 2^0 = 2 + 1 = 3
// 3, 3,    07| 2^2 + 2^1 + 2^0 = 4 + 2 + 1 = 7
// 3, 4,    12| 2^3 + 2^2 = 8 + 4 = 12
// 5, 4,    20| 2^4 + 2^2 = 16 + 4 = 20
// 4, 4,    13| 2^3 + 2^2 + 2^0 = 8 + 4 + 1 = 13
// 5, 3,    19| 2^4 + 2^1 + 2^0 = 16 + 2 + 1 = 19
// 4, 5,    22| 2^4 + 2^2 + 2^1  = 16 + 4 + 2 = 22
// even number squares on row x, col 1
// odd number squares on row 1, col x

// -----------|
// 16 8 4 2 1 |
// -----------|
//  4 3 2 1 0 |
// -----------|-------|-------|
//  0 0 0 0 0 | (r,c) | int   |
//------------|-------|-------|
//  0 0 0 0 1 | (1,1) |   01  | -> 2^0
//  0 0 0 1 0 | (1,2) |   02  | -> 2^1
//  0 1 0 0 1 | (1,3) |   09  | -> 2^3 + 2^1
//  0 1 1 0 0 | (1,4) |   10  | -> 2^3 + 2^2
//  1 1 0 0 1 | (1,5) |   25  | -> 2^4 + 2^3 + 2^0
//------------|-------|-------|
//  0 0 1 0 0 | (2,1) |   04  | -> 2^2
//  0 0 0 1 1 | (2,2) |   03  | -> 2^1 + 2^0
//  0 1 0 0 0 | (2,3) |   08  | -> 2^3
//  0 1 0 1 1 | (2,4) |   11  | -> 2^3 + 2^1 + 2^0
//  1 1 0 0 0 | (2,5) |   24  | -> 2^4 + 2^3
//------------|-------|-------|
//  0 0 1 0 1 | (3,1) |   05  | -> 2^2 + 2^0
//  0 0 1 1 0 | (3,2) |   06  | -> 2^2 + 2^1
//  0 0 1 1 1 | (3,3) |   07  | -> 2^2 + 2^1 + 2^0
//  0 1 1 0 0 | (3,4) |   12  | -> 2^3 + 2^2
//  1 0 1 1 1 | (3,5) |   23  | -> 2^4 + 2^2 + 2^1 + 2^0
//------------|-------|-------|
//  1 0 0 0 0 | (4,1) |   16  | -> 2^4
//  0 1 1 1 1 | (4,2) |   15  | -> 2^3 + 2^2 + 2^1 + 2^0
//  0 1 1 1 0 | (4,3) |   14  | -> 2^3 + 2^2 + 2^1
//  0 1 1 0 1 | (4,4) |   13  | -> 2^3 + 2^2 + 2^0
//  1 0 1 1 0 | (4,5) |   22  | -> 2^4 + 2^2 + 2^1
//------------|-------|-------|
//  1 0 0 0 1 | (5,1) |   17  | -> 2^4 + 2^0
//  1 0 0 1 0 | (5,2) |   18  | -> 2^4 + 2^1
//  1 0 0 1 1 | (5,3) |   19  | -> 2^4 + 2^1 + 2^0
//  1 0 1 0 0 | (5,4) |   20  | -> 2^4 + 2^2
//  1 0 1 0 1 | (5,5) |   21  | -> 2^4 + 2^2 + 2^0
//------------|-------|-------|

// switch direction once you get to a perfect square

// row: even && >= col
//      - row * row - (col - 1)
// row: odd > col
//      - row * row - (col + 1)
// col: odd && >= row
//      - col * col - (row - 1)
// col: even > row
//      - col * col - (col + 1)

#define FAST_IO                                                                \
    ios_base::sync_with_stdio(false);                                          \
    cin.tie(NULL);                                                             \
    cout.tie(NULL);

#define USACO_IO(s)                                                            \
    do {                                                                       \
        freopen(((s) + ".in").c_str(), "r", stdin);                            \
        freopen(((s) + ".out").c_str(), "w", stdout);                          \
    } while (0)

#define LOCAL_IO                                                               \
    do {                                                                       \
        freopen("input.txt", "r", stdin);                                      \
        freopen("output.txt", "w", stdout);                                    \
    } while (0)

/******************************************************************************/
/*                                 CONSTANTS                                  */
/******************************************************************************/

const int MOD = 1e9 + 7;
const int INF = 1e9;
const long long int LLINF = 4e18;
const double PI = acos(-1.0);

/******************************************************************************/
/*                                   SOLVE                                    */
/******************************************************************************/

int solve(void) {
    // row: odd > col
    //      - row * row - (col + 1)
    // col: odd && >= row
    //      - col * col - (row - 1)
    // col: even > row
    //      - col * col - (col + 1)

    unsigned long long int r, c;
    if (!(cin >> r)) {
        return EXIT_FAILURE;
    }
    cin >> c;
    unsigned long long int result;

    if (r % 2 == 0 && r >= c) {
        result = (r * r);
        if (c > 1) {
            result -= c - 1;
        }
    } else if (c % 2 != 0 && c >= r) {
        result = c * c;
        if (r > 1) {
            result -= r - 1;
        }
    } else if (r % 2 != 0 && r > c) {
        result = r * r;
        if (c % 2 != 0) {
            result -= (r - c) * c;
        } else {
            result -= (c + 1);
        }
    } else if (c % 2 == 0 && c > r) {
        result = c * c - c - (c / 2);
        result += r - 1;
    }
    cout << result << "\n";
    return EXIT_SUCCESS;
} // solve

/******************************************************************************/
/*                    01101101 01100001 01101001 01101110                     */
/******************************************************************************/

#define LOCAL

int main(void) {
    FAST_IO;

#ifdef LOCAL
    LOCAL_IO;
#endif // LOCAL

#ifdef USACO
    USACO_IO("problem");
#endif // USACO

    int t;
    // t = 1;
    cin >> t; // Uncomment for multiple test cases
    for (int i = 0; i < t; i++) {
        if (solve()) {
            break;
        }
    }

    cerr << endl
         << "Finished in " << clock() * 1.0 / CLOCKS_PER_SEC << " sec" << endl;

    return EXIT_SUCCESS;
} // main
