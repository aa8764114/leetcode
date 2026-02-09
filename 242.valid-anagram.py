# @lc app=leetcode id=242 lang=python3
from collections import Counter
# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if len(s) != len(t):
        #     return False
        # if sorted(s) == sorted(t):
        if Counter(s) == Counter(t):
            return True
        return False

# @lc code=end

if __name__ == "__main__":
    sol = Solution()
    res1 = sol.isAnagram("anagram","nagaram")