#include <vector>
#include <string>
using namespace std;

class Solution {
public:
    int maxOperations(string s) {
        // 1001101
        // 0011101
        vector<int> ones{};

        auto s_length = s.length();

        for (size_t i = 0; i < s_length; i++)
        {
            if (s[i] == '1') {
                ones.push_back(i);
            }
        }

        uint32_t out{0};
        uint32_t window{1};

        for (size_t i = 0; !ones.empty() && i < ones.size() - 1; i++)
        {
            // 0011101
            auto cur_idx = ones[i];
            auto second_idx = ones[i + 1];
            
            if (second_idx - 1 == cur_idx) {
                window++;
                continue;
            }

            // 0, 2
            out += window;

            window++;
        }

        if (!ones.empty() && s[s_length - 1] != '1') {
            out += window;
        }
        
        return out;
    }
};