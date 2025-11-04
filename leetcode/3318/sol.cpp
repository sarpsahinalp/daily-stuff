#include <vector>
#include <queue>
#include <unordered_map>

using namespace std;

class Solution {
public:
    struct FreqNum {
        int freq;
        int num;
    };

    struct FreqNumComparator {
        bool operator()(const FreqNum& a, const FreqNum& b) {
            if (a.freq == b.freq) {
                return a.num < b.num;
            } 

            return a.freq < b.freq;
        }
    };

    vector<int> findXSum(vector<int>& nums, int k, int x) {
        priority_queue<FreqNum, vector<FreqNum>, FreqNumComparator> heap;
        auto n = nums.size();
        vector<int> res(n - k + 1, 0);

        auto left = 0;

        // lazy update the heap, make the element stay there and invalidate it from outside
        unordered_map<int, int> freqMap;

        // initialize first window
        for (auto i = 0; i < n; i++) {
            auto cur = nums[i];

            if (i > (k - 1)) {
                auto left_elem = nums[left];
                freqMap[left_elem] -= 1;
                heap.push({freqMap[left_elem], left_elem});
                left++;
            }

            freqMap[cur] += 1;
            heap.push({freqMap[cur], cur});
            if (i >= (k - 1)) {
                auto counter = 0;
                auto sum = 0;
                FreqNum arr[2];
                while (counter < x && !heap.empty()) {
                    auto top = heap.top();
                    
                    if (freqMap[top.num] == top.freq) {
                        arr[counter++] = top;
                        sum += top.freq * top.num;
                    }
                    heap.pop();
                }
                for (auto elem : arr) {
                    heap.push(elem);
                }
                res[left] = sum;
            }
        }

        return res;
    }
};