#include <string>
#include <iostream>
#include <unordered_map>
#include <vector>

using namespace std;

class Solution {
public:
    int lengthAfterTransformations(string s, int t) {
        std::vector<int> freq(26);
        for (auto cur : s) {
            freq[cur - 'a']++;
        }

        for (int i = 0; i < t; i++)
        {
            std::vector<int> temp(26);
            for (int j = 0; j < 26; j++) {
                if (j == 25) {
                    temp[0] += freq[j];
                    temp[1] = (temp[1] + freq[j]) % 1000000007;
                } else {
                    if (freq[j] > 0) {
                        temp[j + 1] += freq[j];
                    }
                }
            }
            freq = std::move(temp);
        }

        int sum = 0;
        for (auto num : freq) {
            sum += num;
            sum %= 1000000007;
        }

        return sum;
    }
};

int main() {
    Solution sol = Solution();

    int res = sol.lengthAfterTransformations("azbk", 1);

    cout << res << endl;
}