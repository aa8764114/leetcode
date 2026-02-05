from typing import List, Optional, Dict  # 常用類型定義


# 1. 把 LeetCode 給你的 Class 貼在這裡
# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # --- 你的邏輯開始 ---
        # 題目: 1. Two Sum
        # 核心思維: 利用 Hash Map 儲存看過的數字與 index
        prevMap = {}  # val : index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        # --- 你的邏輯結束 ---


# @lc code=end

# 2. 本地測試區 (按 Ctrl+Enter 立即反饋)
if __name__ == "__main__":
    # 初始化
    sol = Solution()

    # --- 測試案例 (把題目給的 Example 1 丟進來) ---
    print("Testing Example 1...")
    res1 = sol.twoSum([2, 7, 11, 15], 9)
    print(f"Result: {res1} | Expected: [0, 1] | {'PASS' if res1 == [0, 1] else 'FAIL'}")

    # --- 測試案例 (Example 2) ---
    print("\nTesting Example 2...")
    res2 = sol.twoSum([3, 2, 4], 6)
    print(f"Result: {res2} | Expected: [1, 2] | {'PASS' if res2 == [1, 2] else 'FAIL'}")
