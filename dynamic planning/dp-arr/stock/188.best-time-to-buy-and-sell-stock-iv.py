from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        if n <= 0: return 0

        # dp [天数i: 1-n] [交易次数j：1-k] [第i天持有状态：0不持有，1持有]
        dp = [[[0] * 2 for j in range(k + 1)] for i in range(n)]

        # # k=0时的base case
        # for i in range(n):
        #     dp[i][0][0] = 0
        #     dp[i][0][1] = -99999

        for i in range(n):
            for j in range(k, 0, -1):
                # i=0时的base case
                if i - 1 == -1:
                    dp[i][j][0] = 0
                    dp[i][j][1] = -prices[i]
                    continue

                dp[i][j][0] = max(dp[i - 1][j][0], dp[i - 1][j][1] + prices[i])
                dp[i][j][1] = max(dp[i - 1][j][1], dp[i - 1][j - 1][0] - prices[i])

        return dp[n - 1][k][0]


def main():
    # 输入：k = 2, prices = [2,4,1]
    # 输出：2
    # 解释：在第 1 天 (股票价格 = 2) 的时候买入，在第 2 天 (股票价格 = 4) 的时候卖出，
    #       这笔交易所能获得利润 = 4-2 = 2 。
    solution1 = Solution()
    print(solution1.maxProfit(k=2, prices=[2, 4, 1]))

    # 输入：k = 2, prices = [3,2,6,5,0,3]
    # 输出：7
    # 解释：在第 2 天 (股票价格 = 2) 的时候买入，在第 3 天 (股票价格 = 6) 的时候卖出,
    #       这笔交易所能获得利润 = 6-2 = 4 。
    #      随后，在第 5 天 (股票价格 = 0) 的时候买入，在第 6 天 (股票价格 = 3) 的时候卖出,
    #      这笔交易所能获得利润 = 3-0 = 3 。
    solution2 = Solution()
    print(solution2.maxProfit(k=2, prices=[3, 2, 6, 5, 0, 3]))


if __name__ == '__main__':
    main()
