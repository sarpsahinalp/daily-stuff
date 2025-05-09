class Solution {
public:
    int climbStairs(int n) {
        if (n <= 2) {
            return n;
        }

        int last = 2;
        int forLast = 1;
        int output = 0;

        for (int i = 3; i < n; i++)
        {
            output += last + 1 + forLast + 3;
        }

        return output;
        
    }
};