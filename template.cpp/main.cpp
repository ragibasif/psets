
/******************************************************************************/
/*                                  INCLUDES                                  */
/******************************************************************************/

// #include <algorithm>
// #include <bitset>
// #include <cassert>
// #include <chrono>
// #include <climits>
// #include <cmath>
// #include <cstdint>
// #include <functional>
#include <iostream>
// #include <iterator>
// #include <map>
// #include <numeric>
// #include <queue>
// #include <random>
// #include <set>
// #include <stack>
// #include <string>
// #include <tuple>
// #include <unordered_map>
// #include <unordered_set>
// #include <utility>
// #include <vector>

using namespace std;

/******************************************************************************/
/*                                   INPUT                                    */
/******************************************************************************/

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

    long long int n;
    if (!(cin >> n)) {
        return EXIT_FAILURE;
    }
    cout << n << '\n';
    return EXIT_SUCCESS;
} // solve

/******************************************************************************/
/*                    01101101 01100001 01101001 01101110                     */
/******************************************************************************/

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
