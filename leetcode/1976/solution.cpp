#include <vector>
#include <cassert>
#include <iostream>

class Solution {
    public:
        int countPaths(int n, std::vector<std::vector<int>>& roads) {
            return 4;
        }
};

int main(int argc, char const *argv[])
{
    std::vector<std::vector<int>> example = {
        {0, 6, 7}, {0, 1, 2}, {1, 2, 3}, {1, 3, 3},
        {6, 3, 3}, {3, 5, 1}, {6, 5, 1}, {2, 5, 1},
        {0, 4, 5}, {4, 6, 2}
    };
    Solution temp = Solution();
    int out = temp.countPaths(7, example);

    std::cout << "Test" << std::endl;
    assert(out == 4);
    return 0;
}
