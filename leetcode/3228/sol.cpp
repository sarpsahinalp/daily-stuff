#include <vector>
#include <string>
using namespace std;

class Solution {
public:
    int maxOperations(string s) {
        // 1001101
        // 0011101

        auto s_length = s.length();
        uint32_t out{0};
        uint32_t window{0};

        for (size_t i = 0; i < s_length; i++)
        {
            if (s[i] == '0') {
                while ((i + 1) < s_length && s[i + 1] == '0')
                {
                    i++;
                }
                out += window;
            } else {
                window++;
            }
        }

        return out;
    }
};