from typing import List

"""
解决博弈问题的动态规划解法:
博弈问题的前提一般都是在两个聪明人之间进行，编程描述这种游戏的一般方法是【二维 dp 数组】，
数组中通过元组分别表示两人的最优决策。
之所以这样设计，是因为先手在做出选择之后，就成了后手，后手在对方做完选择后，就变成了先手。
这种角色转换使得我们可以重用之前的结果，典型的动态规划标志。
"""

"""
动规3要素：
1.dp数组含义 
dp[i][j].fir = x 表示，对于 piles[i...j] 这部分石头堆，先手能获得的最高分数为 x。
dp[i][j].sec = y 表示，对于 piles[i...j] 这部分石头堆，后手能获得的最高分数为 y。
2.穷举状态/选择
3.base case以及题目所求的最终状态
"""


class Pair:
    def __init__(self, first=0, second=0):
        self.first = first
        self.second = second


class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)

        dp = [[Pair()] * n for row in range(n)]
        # base case
        for i in range(n):
            dp[i][i].first = piles[i]
            dp[i][i].second = 0

        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n, 1):
                left = piles[i] + dp[i + 1][j].second
                right = piles[j] + dp[i][j - 1].second
                if left > right:
                    dp[i][j].first = left
                    dp[i][j].second = dp[i + 1][j].first  # 后手在做完决策后变为先手
                else:
                    dp[i][j].first = right
                    dp[i][j].second = dp[i][j - 1].second

        res = dp[0][n - 1]
        return res.first - res.second

    def PredictTheWinner(self, nums: List[int]) -> bool:
        # 先手的分数大于后手的分数则能赢
        return self.stoneGame(nums) >= 0


def main():
    # 输入：nums = [1,5,2]
    # 输出：false
    # 解释：一开始，玩家 1 可以从 1 和 2 中进行选择。
    # 如果他选择 2（或者 1 ），那么玩家 2 可以从 1（或者 2 ）和 5 中进行选择。如果玩家 2 选择了 5 ，那么玩家 1 则只剩下 1（或者 2 ）可选。
    # 所以，玩家 1 的最终分数为 1 + 2 = 3，而玩家 2 为 5 。
    # # 因此，玩家 1 永远不会成为赢家，返回 false 。
    solution1 = Solution()
    print(solution1.PredictTheWinner(nums=[1, 5, 2]))

    # 输入：nums = [1,5,233,7]
    # 输出：true
    # 解释：玩家 1 一开始选择 1 。然后玩家 2 必须从 5 和 7 中进行选择。无论玩家 2 选择了哪个，玩家 1 都可以选择 233 。
    # 最终，玩家 1（234 分）比玩家 2（12 分）获得更多的分数，所以返回 true，表示玩家 1 可以成为赢家。
    solution1 = Solution()
    print(solution1.PredictTheWinner(nums=[1, 5, 233, 7]))

    # 输入：nums = [2,4,55,6,8]
    # 输出：true
    # 预期结果：false
    solution1 = Solution()
    print(solution1.PredictTheWinner(nums=[2, 4, 55, 6, 8]))


if __name__ == '__main__':
    main()
