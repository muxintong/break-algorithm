from typing import List


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        memory = dict()
        n = len(matrix)

        def dp(i: int, j: int) -> int:
            # base case
            if i == 0: return matrix[0][j]

            # pre recursive:查memory
            if memory.get((i, j)): return memory[(i, j)]

            # recursive:写memory
            if j == 0:
                memory[(i, j)] = min(
                    dp(i - 1, j) + matrix[i][j],
                    dp(i - 1, j + 1) + matrix[i][j]
                )
            elif j == n - 1:
                memory[(i, j)] = min(
                    dp(i - 1, j) + matrix[i][j],
                    dp(i - 1, j - 1) + matrix[i][j]
                )
            else:
                memory[(i, j)] = min(
                    dp(i - 1, j - 1) + matrix[i][j],
                    dp(i - 1, j) + matrix[i][j],
                    dp(i - 1, j + 1) + matrix[i][j]
                )

            # post recursive:返回memory
            return memory[(i, j)]

        # 取j从0-n中最小的那个
        min_sum = 99999999
        for j in range(n):
            # 递归部分从i=n-1减至0
            min_sum = min(min_sum, dp(n - 1, j))
        return min_sum


def main():
    # Input: matrix = [[2,1,3],[6,5,4],[7,8,9]]
    # Output: 13
    # Explanation: There are two falling paths with a minimum sum as shown.
    solution1 = Solution()
    print(solution1.minFallingPathSum(matrix=[[2, 1, 3], [6, 5, 4], [7, 8, 9]]))

    # Input: matrix = [[-19,57],[-40,-5]]
    # Output: -59
    # Explanation: The falling path with a minimum sum is shown.
    solution2 = Solution()
    print(solution2.minFallingPathSum(matrix=[[-19, 57], [-40, -5]]))


if __name__ == '__main__':
    main()
