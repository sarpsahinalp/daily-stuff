#include <unordered_map>
#include <unordered_set>

using namespace std;

class TwoSum
{
private:
    vector<int> nums;
    unordered_map<int, int> numsMap;
    int count{0};

public:
    TwoSum() {}

    void add(int number)
    {
        nums.push_back(number);
        nums[number] += 1;
        count++;
    }

    bool find(int value)
    {
        for (size_t i = 0; i < count; i++)
        {
            auto search_val = value - nums[i];

            if (numsMap.contains(search_val)) {
                if (search_val == nums[i]) {
                    if (numsMap[search_val] > 1) {
                        return 1;
                    }
                } else if (numsMap[search_val] > 0) {
                    return 1;
                }
            }
        }
        

        return 0;
    }
};

/**
 * Your TwoSum object will be instantiated and called as such:
 * TwoSum* obj = new TwoSum();
 * obj->add(number);
 * bool param_2 = obj->find(value);
 */