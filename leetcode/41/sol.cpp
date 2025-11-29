#include <vector>
#include <unordered_set>

using namespace std;

class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
        unordered_set<int> seen;

        for (size_t i = 0; i < nums.size(); i++)
        {
            seen.insert(nums[i]);
        }

        auto min = 1;

        while (seen.count(min) > 0) {
            min++;
        }

        return min;
        
    }
};