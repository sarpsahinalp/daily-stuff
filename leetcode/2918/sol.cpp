#include <vector>
#include <iostream>
using namespace std;

class Solution
{
public:
    long long minSum(vector<int> &nums1, vector<int> &nums2)
    {
        // Get number of zeros in each and also the current sum
        long long zeroCount1 = 0;
        long long sum1 = 0;
        for (auto num : nums1)
        {
            if (num == 0)
            {
                zeroCount1++;
            }

            sum1 += num;
        }

        long long zeroCount2 = 0;
        long long sum2 = 0;

        for (auto num : nums2)
        {
            if (num == 0)
            {
                zeroCount2++;
            }

            sum2 += num;
        }

        // Cases

        // Both of them have zeros
        if (zeroCount1 > 0 && zeroCount2 > 0)
        {
            long long allSet1 = zeroCount1 + sum1;
            long long allSet2 = zeroCount2 + sum2;
            if (allSet1 > allSet2)
            {
                long long diff = allSet1 - sum2;
                return allSet1;
            } else if (allSet1 == allSet2) {
                return allSet1;
            } else {
                long long diff = allSet2 - sum1;
                return allSet2;
            }
            
            
            return -1;
        }
        // One of them does not have a zero
        else if (zeroCount1 > 0 || zeroCount2 > 0)
        {
            if (zeroCount1 > 0)
            {
                if (zeroCount1 + sum1 > sum2)
                {
                    return -1;
                }

                return sum2;
            }
            else
            {
                if (zeroCount2 + sum2 > sum1)
                {
                    return -1;
                }

                return sum1;
            }
        }
        // Both of them don't have zero
        else
        {
            return sum1 == sum2 ? sum1 : -1;
        }
    }
};