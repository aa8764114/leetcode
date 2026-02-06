# @lc app=leetcode id=217 lang=python3
from typing import List, Optional, Dict  # 常用類型定義
from collections import Counter


# @lc code=start
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        counts = Counter(nums)
        for i in nums:
            if counts[i] > 1:
                print("TRUE")
                return True
        print("FALSE")
        return False


# @lc code=end

if __name__ == "__main__":
    sol = Solution()
    res1 = sol.containsDuplicate([2, 7, 11, 15])
