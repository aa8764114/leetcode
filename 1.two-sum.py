#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#
# https://leetcode.com/problems/two-sum/description/
#
# algorithms
# Easy (56.96%)
# Likes:    67214
# Dislikes: 2501
# Total Accepted:    20.5M
# Total Submissions: 36M
# Testcase Example:  '[2,7,11,15]\n9'
#
# Given an array of integers nums and an integer target, return indices of the
# two numbers such that they add up to target.
# 
# You may assume that each input would have exactly one solution, and you may
# not use the same element twice.
# 
# You can return the answer in any order.
# 
# 
# Example 1:
# 
# 
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# 
# 
# Example 2:
# 
# 
# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# 
# 
# Example 3:
# 
# 
# Input: nums = [3,3], target = 6
# Output: [0,1]
# 
# 
# 
# Constraints:
# 
# 
# 2 <= nums.length <= 10^4
# -10^9 <= nums[i] <= 10^9
# -10^9 <= target <= 10^9
# Only one valid answer exists.
# 
# 
# 
# Follow-up: Can you come up with an algorithm that is less than O(n^2) time
# complexity?
#

from typing import List, Optional, Dict # 常用類型定義

# 1. 把 LeetCode 給你的 Class 貼在這裡
# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # --- 你的邏輯開始 ---
        # 題目: 1. Two Sum
        # 核心思維: 利用 Hash Map 儲存看過的數字與 index
        prevMap = {} # val : index
        
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
