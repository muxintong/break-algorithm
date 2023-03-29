from typing import List


class Solution:
    #  陆地：1
    #  海水：0
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        # 递归淹没陆地grid[i][j]==1上下左右四周的所有陆地，并返回被淹没的岛屿的面积
        def dfs(i: int, j: int) -> int:
            if i < 0 or j < 0 or i > m - 1 or j > n - 1:
                return 0

            if grid[i][j] == 0:
                return 0
            elif grid[i][j] == 1:
                grid[i][j] = 0  # 如果grid[i][j]==1是陆地，将其变成海水，标记为已经访问处理过

            return dfs(i - 1, j) + dfs(i + 1, j) + dfs(i, j - 1) + dfs(i, j + 1) + 1

        # 非封闭岛屿问题，无需处理上下左右四条边界线，直接遍历grid，处理是陆地的grid[i][j]即可
        max_area = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    max_area = max(max_area, dfs(i, j))
        return max_area


def main():
    # Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
    # Output: 6
    solution1 = Solution()
    print(solution1.maxAreaOfIsland(
        grid=[[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
              [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
              [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]))

    # Input: grid = [[0,0,0,0,0,0,0,0]]
    # Output: 0
    solution2 = Solution()
    print(solution2.maxAreaOfIsland(grid=[[0, 0, 0, 0, 0, 0, 0, 0]]))

    # Input [[1,1,0,1,1],[1,0,0,0,0],[0,0,0,0,1],[1,1,0,1,1]]
    # Output 4
    # Expected 3
    solution3 = Solution()
    print(solution3.maxAreaOfIsland([[1,1,0,1,1],[1,0,0,0,0],[0,0,0,0,1],[1,1,0,1,1]]))


if __name__ == '__main__':
    main()
