# @lc app=leetcode id=128 lang=python3
from typing import List


# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0
        for i in num_set:
            if i - 1 not in num_set:
                length = 1
                while i + length in num_set:
                    length += 1
                longest = max(longest, length)
        # print(longest)
        return longest
# @lc code=end

if __name__ == "__main__":
    sol = Solution()
    print("Testing Example 1...")
    res1 = sol.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1])
