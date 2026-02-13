# @lc app=leetcode id=347 lang=python3
from collections import Counter
from typing import List

# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_count = Counter(nums)
        top_n = num_count.most_common(k)
        # print(num_count)
        # print(top_n)
        # print(top_n[0][0],top_n[1][0])
        top_list = []
        for i in top_n:
            # print(i[0])
            top_list.append(i[0])
            # print(top_list)
        return top_list
        
# @lc code=end

if __name__ == "__main__":
    sol = Solution()
    print("Testing Example 1...")
    res1 = sol.topKFrequent([1,1,1,2,2,3], 2)