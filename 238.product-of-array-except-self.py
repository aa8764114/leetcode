# @lc app=leetcode id=238 lang=python3
from typing import List

# index = 0 左邊沒東西
# index = len(nums)-1 右邊沒東西


# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(n - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res
# @lc code=end

if __name__ == "__main__":
    sol = Solution()
    res1 = sol.productExceptSelf([3, 0, 6, 7, 8])
