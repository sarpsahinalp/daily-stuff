#include <string>
#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int countBalancedPermutations(string num) {
        // 1. Idea have a backtracking stuff and check whether in each step it completes the necessary stuff
        
        // First have a vector with possibble values that can be put in the current run
    }
};

int main() {
    Solution sol;

    // 2. Read the input string (e.g. “12321”) from stdin:
    string num;
    if (!(cin >> num)) {
        cerr << "No input provided\n";
        return 1;
    }

    // 3. Call your method and print the result:
    int answer = sol.countBalancedPermutations(num);
    cout << answer << "\n";

    return 0;
}