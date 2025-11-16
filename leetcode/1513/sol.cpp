class Solution {

    // 1 +2 3 +3 6 +4 10 +5 15 +6 21 +7 28
public:
    int numSub(string s) {
        long long mod = 1e9 + 7;
        auto window = 0;
        auto out = 0;
        auto cur = 0;
        for (auto ch : s) {
            if (ch == '1') {
                window++;
                cur = ((long long) window + cur) % mod;
            } else {
                if (window > 0) {
                    out = ((long long) out + cur) % mod;
                    cur = window = 0;
                }
            }
        }

        return out + cur;
    }
};