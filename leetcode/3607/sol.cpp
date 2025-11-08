#include <vector>
#include <queue>
#include <set>
#include <unordered_set>
#include <stack>

using namespace std;

#include <vector>
#include <numeric> // For std::iota (a slightly cleaner way to init)

using namespace std;

class UnionFind {
public: 
    vector<int> parents;
    vector<int> sizes; // <-- 1. Add sizes vector

    UnionFind(int n) : parents(n), sizes(n, 1) { // <-- 2. Initialize vectors
        // Initializes parents to 0, 1, 2, ...
        // and all sizes to 1
        std::iota(parents.begin(), parents.end(), 0);
    }

    int find(int cur) {
        if (parents[cur] == cur) {
            return cur;
        }
        // Path compression (this part was already perfect)
        return parents[cur] = find(parents[cur]);
    }

    // Returns true if a union was performed, false if they were already united
    bool unionParent(int left, int right) {
        int parentLeft = find(left);
        int parentRight = find(right);

        // 3. Check if already in the same set
        if (parentLeft == parentRight) {
            return false; 
        }

        // 4. Union by size:
        // Attach the smaller tree (parentRight) to the larger tree (parentLeft)
        if (sizes[parentLeft] < sizes[parentRight]) {
            // Swap them so parentLeft is always the larger one
            swap(parentLeft, parentRight);
        }

        // Attach right's tree under left's tree
        parents[parentRight] = parentLeft;
        // Update the size of the new root
        sizes[parentLeft] += sizes[parentRight];
        
        return true;
    }
};


class Solution {
public:
    vector<int> processQueries(int c, vector<vector<int>>& connections, vector<vector<int>>& queries) {
        auto uf = UnionFind(c);

        vector<vector<int>> adjacency_list(c);

        for (auto connection : connections) {
            auto first = connection[0] - 1;
            auto second = connection[1] - 1;

            adjacency_list[first].push_back(second);
            adjacency_list[second].push_back(first);

            uf.unionParent(first, second);
        }

        unordered_set<int> visited;

        vector<set<int>> online_stations(c);

        for (int i = 0; i < c; i++) {
            // Find the canonical root for node 'i'
            int root = uf.find(i);
            // Add 'i' to the set corresponding to that root
            online_stations[root].insert(i);
        }

        vector<int> result;
        
        for (auto query : queries) 
        {
            auto op = query[0];
            auto node = query[1] - 1;

            if (op == 1) {
                auto parent = uf.find(node);

                if (online_stations[parent].empty()) {
                    result.push_back(-1);
                    continue;
                }
                
                if (online_stations[parent].contains(node)) {
                    result.push_back(node + 1);
                } else {
                    auto min_station = *online_stations[parent].begin();
                    result.push_back(min_station + 1);
                }
            } else {
                auto parent = uf.find(node);
                online_stations[parent].erase(node);
            }
        }


        return result;
    }
};