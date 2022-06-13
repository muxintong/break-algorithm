from typing import List


class Solution:
    # 岛屿：'1'
    # 海水：'0'
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])

        # 淹没grid[i][j]上下左右的岛屿
        def dfs(i: int, j: int):
            if i < 0 or j < 0 or i > m-1 or j > n-1:
                return

            if grid[i][j] == '0':
                return
            elif grid[i][j] == '1':
                # NOTE:直接将grid[i][j]这块陆地的值置为海水'0'可避免标记数组visited的使用
                grid[i][j] = '0'

            dfs(i - 1, j)  # 淹没上陆地
            dfs(i + 1, j)  # 淹没下陆地
            dfs(i, j - 1)  # 淹没左陆地
            dfs(i, j + 1)  # 淹没右陆地

        res = 0
        # 遍历grid
        for i in range(m):
            for j in range(n):
                if grid[i][j]=='1':
                    res += 1
                    dfs(i, j)
        return res


def main():
    # Input: grid = [
    #   ["1","1","1","1","0"],
    #   ["1","1","0","1","0"],
    #   ["1","1","0","0","0"],
    #   ["0","0","0","0","0"]
    # ]
    # Output: 1
    solution1 = Solution()
    print(solution1.numIslands(grid = [
                                      ["1","1","1","1","0"],
                                      ["1","1","0","1","0"],
                                      ["1","1","0","0","0"],
                                      ["0","0","0","0","0"]
                                    ]))

    print('---')

    # Input: grid = [
    #   ["1","1","0","0","0"],
    #   ["1","1","0","0","0"],
    #   ["0","0","1","0","0"],
    #   ["0","0","0","1","1"]
    # ]
    # Output: 3
    solution2 = Solution()
    print(solution2.numIslands(grid = [
                                      ["1","1","0","0","0"],
                                      ["1","1","0","0","0"],
                                      ["0","0","1","0","0"],
                                      ["0","0","0","1","1"]
                                    ]))


if __name__ == '__main__':
    main()
