#include <vector>
#include <cassert>
#include <iostream>
#include <unordered_set>

using namespace std;

class Solution {
    public:
        int countPaths(int n, std::vector<std::vector<int>>& roads) {
            // Create adjacency list with hashtable
            vector<unordered_set<pair<int, int>>> adjacencyList(n);

            for (auto road : roads) {
                int from = road[0];
                int to = road[1];
                int weight = road[2];
                adjacencyList[from].insert({to, weight});
            }

            for (auto elem : adjacencyList) {
                for (auto pairs : elem) 
                {
                    cout << pairs << endl;
                }
                
            }
            return adjacencyList.size();
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

    if (out != 4) {
        printf("Expected: %d\n But was: %d", 4, out);
    }

    return 0;
}
