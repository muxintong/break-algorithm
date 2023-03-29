from typing import List


class Solution:
    # 陆地：1
    # 海水：0
    # core mind：返回grid2中是grid1的子岛屿的个数，故以grid2为遍历主体，他的【总岛屿个数 - 不是1的子岛屿个数】即为所求
    # step：
    #   （1）2中不是1的子岛屿：即grid2[i][j]为1，但grid1[i][j]为0，调用dfs将这样的陆地淹没为岛屿。
    #   （2）dfs 求解grid2中岛屿的个数即为所求
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        m = len(grid2)
        n = len(grid2[0])

        def dfs(i: int, j: int):
            if i < 0 or j < 0 or i > m - 1 or j > n - 1:
                return

            if grid2[i][j] == 0:
                return
            elif grid2[i][j] == 1:
                grid2[i][j] = 0

            dfs(i - 1, j)
            dfs(i + 1, j)
            dfs(i, j - 1)
            dfs(i, j + 1)

        # (1)将2中不符合题意的岛屿淹没为海水
        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1 and grid1[i][j] == 0:
                    dfs(i, j)

        # (2)对2直接调用dfs即为所求
        res = 0
        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1:
                    res += 1
                    dfs(i, j)

        return res


def main():
    # Input: grid1 = [[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]], grid2 = [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]
    # Output: 3
    solution1 = Solution()
    print(solution1.countSubIslands(
        grid1=[[1, 1, 1, 0, 0], [0, 1, 1, 1, 1], [0, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 1, 0, 1, 1]],
        grid2=[[1, 1, 1, 0, 0], [0, 0, 1, 1, 1], [0, 1, 0, 0, 0], [1, 0, 1, 1, 0], [0, 1, 0, 1, 0]]))

    # Input: grid1 = [[1,0,1,0,1],[1,1,1,1,1],[0,0,0,0,0],[1,1,1,1,1],[1,0,1,0,1]], grid2 = [[0,0,0,0,0],[1,1,1,1,1],[0,1,0,1,0],[0,1,0,1,0],[1,0,0,0,1]]
    # Output: 2
    solution2 = Solution()
    print(solution2.countSubIslands(
        grid1=[[1, 0, 1, 0, 1], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0], [1, 1, 1, 1, 1], [1, 0, 1, 0, 1]],
        grid2=[[0, 0, 0, 0, 0], [1, 1, 1, 1, 1], [0, 1, 0, 1, 0], [0, 1, 0, 1, 0], [1, 0, 0, 0, 1]]))


if __name__ == '__main__':
    main()
