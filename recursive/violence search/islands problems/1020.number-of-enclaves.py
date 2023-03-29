from typing import List


class Solution:
    # 0 sea
    # 1 land
    def numEnclaves(self, grid: List[List[int]]) -> int:

        # 淹没grid[i][j]上下左右的岛屿，并返回被淹没的岛屿面积
        def dfs(i: int, j: int) -> int:
            # 递归出口
            if i < 0 or j < 0 or i > m - 1 or j > n - 1:
                return 0

            # 选择grid[i][j]判断:land(1) or sea(0)?
            if grid[i][j] == 0:
                return 0
            elif grid[i][j] == 1:
                grid[i][j] = 0
                # return 1

            # NOTE:除了被淹没的上下左右四块岛屿的面积，还需加上被淹没的grid[i][j]的面积1
            return dfs(i - 1, j) + dfs(i + 1, j) + dfs(i, j - 1) + dfs(i, j + 1) + 1

        m = len(grid)
        n = len(grid[0])
        # 因所求为封闭岛屿面积，还需淹没上下+左右 四条边界线上的所有岛屿
        for j in range(n):
            dfs(0, j)
            dfs(m - 1, j)
        for i in range(m):
            dfs(i, 0)
            dfs(i, n - 1)

        # 遍历grid，淹没grid[i][j]是陆地1的上下左右四周的所有岛屿
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    res += dfs(i, j)
        return res


def main():
    # Input: grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
    # Output: 3
    solution1 = Solution()
    print(solution1.numEnclaves(grid=[[0, 0, 0, 0], [1, 0, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]))

    # Input: grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
    # Output: 0
    solution2 = Solution()
    print(solution2.numEnclaves(grid=[[0, 1, 1, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 0]]))


if __name__ == '__main__':
    main()
