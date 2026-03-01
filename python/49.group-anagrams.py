# @lc app=leetcode id=49 lang=python3
from typing import List, Optional, Dict  # 常用類型定義
from collections import Counter

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for str in strs:
            key = "".join(sorted(str))
            if key not in res:
                res[key] = []
            res[key].append(str)
        # print(list(res.values()))
        return (list(res.values()))
# @lc code=end

if __name__ == "__main__":
    sol = Solution()
    res1 = sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"])