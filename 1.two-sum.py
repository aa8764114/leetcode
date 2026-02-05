# @lc app=leetcode id=1 lang=python3
from typing import List, Optional, Dict
# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {} # val : index
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
# @lc code=end
if __name__ == "__main__":
    sol = Solution()
    print("Testing Example 1...")
    res1 = sol.twoSum([2, 7, 11, 15], 9)
    print(f"Result: {res1} | Expected: [0, 1] | {'PASS' if res1 == [0, 1] else 'FAIL'}")
    print("\nTesting Example 2...")
    res2 = sol.twoSum([3, 2, 4], 6)
    print(f"Result: {res2} | Expected: [1, 2] | {'PASS' if res2 == [1, 2] else 'FAIL'}")
