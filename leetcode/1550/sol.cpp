#include <vector>

using namespace std;

class Solution
{
public:
    bool threeConsecutiveOdds(vector<int> &arr)
    {
        int consecutiveOdds = 0;
        bool lastWasConsecutive = true;

        // First window
        for (size_t i = 0; i < 3; i++)
        {
            if (i % 2 == 1)
            {
                consecutiveOdds++;
            }
            else
            {
                consecutiveOdds = 0;
                lastWasConsecutive = false;
            }
        }

        if (consecutiveOdds == 3)
        {
            return true;
        }

        for (size_t i = 3; i < arr.size(); i++)
        {
            if (i % 2 == 1)
            {
                consecutiveOdds++;
                lastWasConsecutive = true;
            }
            else
            {
                consecutiveOdds = 0;
                lastWasConsecutive = false;
            }

            if (consecutiveOdds == 3) {
                return true;
            }
        }

        return false;
    }
};