from typing import List


class Solution:
    # sea: 1
    # land: 0
    def closedIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        def dfs(i: int, j: int):
            # 递归出口
            if i < 0 or j < 0 or i > m - 1 or j > n - 1:
                return

            # 选择grid[i][j]判断为：0 or 1
            if grid[i][j] == 1:
                return
            elif grid[i][j] == 0:
                grid[i][j] = 1  # 对于是陆地0的岛屿直接将其变成海水1，可避免visited数组的使用

            dfs(i - 1, j)  # 淹没上陆地
            dfs(i + 1, j)  # 淹没下陆地
            dfs(i, j - 1)  # 淹没左陆地
            dfs(i, j + 1)  # 淹没右陆地

        # 淹没上下边界的岛屿
        for j in range(n):
            dfs(0, j)  # 淹上
            dfs(m - 1, j)  # 淹下
        # 淹没左右边界的岛屿
        for i in range(m):
            dfs(i, 0)  # 淹左
            dfs(i, n - 1)  # 淹右

        # 淹没边界岛屿后剩下的岛屿数量即为所求
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    res += 1
                    # 因求岛屿的数量，故与陆地0待遇数量加1，并递归【淹没】该陆地周围（上下左右）的所有陆地即可
                    dfs(i, j)
        return res


def main():
    # Input: grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
    # Output: 2
    solution1 = Solution()
    print(solution1.closedIsland(grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]))

    print('---')

    # Input: grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
    # Output: 1
    solution2 = Solution()
    print(solution2.closedIsland(grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]))


if __name__ == '__main__':
    main()


