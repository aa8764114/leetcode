# @lc app=leetcode id=36 lang=python3
from typing import List


# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for row in board:
            crow = []
            for i in row:
                if i != '.':
                    crow.append(i)
            # print(crow)
            if len(crow) != len(set(crow)):
                print("row_False")
                return False
            
        for i in range(len(board)):
            col = []
            for row in board:
                if row[i] != '.':
                    col.append(row[i])
            if len(col) != len(set(col)):
                print("col_False")
                return False
            # print(col)

        for r in [0, 3, 6]:
            for c in [0, 3, 6]:
                cube = []
                for sr in range(r, r + 3):
                    for sc in range(c, c + 3):
                        # print(board[sr][sc])
                        if board[sr][sc] != '.':
                            cube.append(board[sr][sc])
                # print(cube)
                if len(cube) != len(set(cube)):
                    print("cube_False")
                    return False
        print("True")
        return True


# @lc code=end
if __name__ == "__main__":
    sol = Solution()
    # print("Testing Example 1...")
    res1 = sol.isValidSudoku(
        # [
        #     ["8", "3", ".", ".", "7", ".", ".", ".", "."],
        #     ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        #     [".", "9", "8", ".", ".", ".", ".", "6", "."],
        #     ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        #     ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        #     ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        #     [".", "6", ".", ".", ".", ".", "2", "8", "."],
        #     [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        #     [".", ".", ".", ".", "8", ".", ".", "7", "9"],
        # ]
        [
            ["5", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"],
        ]
    )
