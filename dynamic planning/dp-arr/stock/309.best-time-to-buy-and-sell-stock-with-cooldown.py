from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0] * 2 for row in range(n)]
        for i in range(n):
            if i - 1 == -1:
                dp[i][0] = 0
                dp[i][1] = -prices[i]
                continue
            if i - 2 == -1:
                dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
                dp[i][1] = max(dp[i - 1][1], -prices[i])
                # dp[i][1] = max(dp[i-1][1], dp[-1][0]-prices[i])
                #          = max(dp[i-1][1], 0-prices[i])
                #          = max(dp[i-1][1], -prices[i])
                continue

            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            # 交易冷冻期设置：每次sell之后要等一天才能继续交易。
            # 即在第i天选择buy的时候，要从i-2的状态转移，而不是i-1.
            dp[i][1] = max(dp[i - 1][1], dp[i - 2][0] - prices[i])

        return dp[n - 1][0]


def main():
    # 输入: prices = [1,2,3,0,2]
    # 输出: 3
    # 解释: 对应的交易状态为: [买入, 卖出, 冷冻期, 买入, 卖出]
    solution1 = Solution()
    print(solution1.maxProfit(prices=[1, 2, 3, 0, 2]))

    # 输入: prices = [1]
    # 输出: 0
    solution2 = Solution()
    print(solution2.maxProfit(prices=[1]))


if __name__ == '__main__':
    main()
