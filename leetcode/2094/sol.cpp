#include <vector>
#include <unordered_map>
#include <iostream>

using namespace std;

class Solution {
public:
    vector<int> findEvenNumbers(vector<int>& digits) {
        unordered_map<int, int> frequency;
        
        for (auto digit : digits)
        {
            frequency[digit] += 1;
            cout << frequency[digit] << endl;
        }
        

        return digits;
    }
};