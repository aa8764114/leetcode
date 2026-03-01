#include <iostream>
#include <vector>
#include <unordered_map>
#include <string>
#include <algorithm>

using namespace std;

// 1. 把 LeetCode 給你的 Class 貼在這裡
// @lc code=start
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        // --- 你的邏輯開始 ---
        // 題目: 1. Two Sum
        // 核心思維: 利用 Hash Map 儲存看過的數字與 index
        unordered_map<int, int> prevMap; // val : index

        for (int i = 0; i < nums.size(); i++) {
            int diff = target - nums[i];
            if (prevMap.find(diff) != prevMap.end()) {
                return {prevMap[diff], i};
            }
            prevMap[nums[i]] = i;
        }
        return {};
        // --- 你的邏輯結束 ---
    }
};
// @lc code=end

// --- 輔助工具：讓 C++ 打印 vector 像 Python 一樣簡單 ---
template <typename T>
void printVector(const vector<T>& v) {
    cout << "[";
    for (int i = 0; i < v.size(); i++) {
        cout << v[i] << (i == v.size() - 1 ? "" : ", ");
    }
    cout << "]";
}

// 2. 本地測試區
int main() {
    Solution sol;

    // --- 測試案例 1 ---
    {
        cout << "Testing Example 1..." << endl;
        vector<int> nums = {2, 7, 11, 15};
        int target = 9;
        vector<int> expected = {0, 1};
        
        vector<int> res = sol.twoSum(nums, target);
        
        cout << "Result: "; printVector(res);
        cout << " | Expected: "; printVector(expected);
        cout << " | " << (res == expected ? "✅ PASS" : "❌ FAIL") << endl;
    }

    // --- 測試案例 2 ---
    {
        cout << "\nTesting Example 2..." << endl;
        vector<int> nums = {3, 2, 4};
        int target = 6;
        vector<int> expected = {1, 2};
        
        vector<int> res = sol.twoSum(nums, target);
        
        cout << "Result: "; printVector(res);
        cout << " | Expected: "; printVector(expected);
        cout << " | " << (res == expected ? "✅ PASS" : "❌ FAIL") << endl;
    }

    return 0;
}
