from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        # dp [天数i：0-n] [第i天股票的持有状态：0不持有，1持有]
        dp = [[0] * 2 for row in range(n)]
        for i in range(n):
            # base case
            if i - 1 == -1:
                dp[i][0] = 0
                dp[i][1] = -prices[i]
                # NOTE:在此种情况下需跳出该循环继续执行，若缺少continue语句则结果不正确
                continue

            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            # NOTE：区别交易次数的两种特殊限制情况：k=1 及 不限制交易次数k
            # dp[i][1] = max(dp[i - 1][1], - prices[i])   # 限制交易次数k仅为1，则若第i天持有，则无i-1前一天的交易状态
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])    # 不限制交易次数k，即k为正无穷大

        return dp[n - 1][0]


def main():
    # 输入：prices = [7,1,5,3,6,4]
    # 输出：7
    # 解释：在第 2 天（股票价格 = 1）的时候买入，在第 3 天（股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5 - 1 = 4 。
    #      随后，在第 4 天（股票价格 = 3）的时候买入，在第 5 天（股票价格 = 6）的时候卖出, 这笔交易所能获得利润 = 6 - 3 = 3 。
    #      总利润为 4 + 3 = 7 。
    solution1 = Solution()
    print(solution1.maxProfit(prices=[7, 1, 5, 3, 6, 4]))

    # 输入：prices = [1,2,3,4,5]
    # 输出：4
    # 解释：在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5 - 1 = 4 。
    #     总利润为 4 。
    solution2 = Solution()
    print(solution2.maxProfit(prices=[1, 2, 3, 4, 5]))

    # 输入：prices = [7,6,4,3,1]
    # 输出：0
    # 解释：在这种情况下, 交易无法获得正利润，所以不参与交易可以获得最大利润，最大利润为 0 。
    solution3 = Solution()
    print(solution3.maxProfit(prices=[7, 6, 4, 3, 1]))


if __name__ == '__main__':
    main()
