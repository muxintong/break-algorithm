from typing import List


class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m = len(dungeon)
        n = len(dungeon[0])
        memory = [[-1] * n for row in range(m)]

        # 从 grid[i][j] 到达终点（右下角）所需的最少生命值是 dp(grid, i, j)。
        def dp(i: int, j: int) -> int:
            # base case
            if i == m - 1 and j == n - 1:
                if dungeon[i][j] >= 0:
                    return 1
                else:
                    return -dungeon[i][j] + 1
            # NOTE: eliminate IndexError(list index out of range)
            if i == m or j == n: return 999999

            # before recursive: find in memory
            if memory[i][j] != -1: return memory[i][j]
            # recursive
            res = min(dp(i, j + 1), dp(i + 1, j)) - dungeon[i][j]
            # after recursive:write in memory
            if res <= 0:
                memory[i][j] = 1    # 骑士生命值至少为1
            else:
                memory[i][j] = res

            return memory[i][j]

        return dp(0, 0)


def main():
    # in:[[-2,-3,3],[-5,-10,1],[10,30,-5]]
    # out:7
    solution1 = Solution()
    print(solution1.calculateMinimumHP([[-2, -3, 3], [-5, -10, 1], [10, 30, -5]]))


if __name__ == '__main__':
    main()
