from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        K = 2
        dp = [[[0] * 2 for k in range(K + 1)] for i in range(n)]
        # NOTE:由于本例中交易次数为2（不是两个特殊值：1或不限交易次数），
        # 故还需对交易次数k进行穷举。
        for i in range(n):
            for k in range(K, 0, -1):
                if i - 1 == -1:
                    dp[i][k][0] = 0
                    dp[i][k][1] = -prices[i]
                    continue

                dp[i][k][0] = max(dp[i - 1][k][0], dp[i - 1][k][1] + prices[i])
                dp[i][k][1] = max(dp[i - 1][k][1], dp[i - 1][k - 1][0] - prices[i])

        return dp[n - 1][K][0]


def main():
    # 输入：prices = [3,3,5,0,0,3,1,4]
    # 输出：6
    # 解释：在第 4 天（股票价格 = 0）的时候买入，在第 6 天（股票价格 = 3）的时候卖出，这笔交易所能获得利润 = 3-0 = 3 。
    #     随后，在第 7 天（股票价格 = 1）的时候买入，在第 8 天 （股票价格 = 4）的时候卖出，这笔交易所能获得利润 = 4-1 = 3 。
    solution1 = Solution()
    print(solution1.maxProfit(prices=[3, 3, 5, 0, 0, 3, 1, 4]))

    # 输入：prices = [1,2,3,4,5]
    # 输出：4
    # 解释：在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。  
    #      注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。  
    #      因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。
    solution2 = Solution()
    print(solution2.maxProfit(prices=[1, 2, 3, 4, 5]))

    # 输入：prices = [7,6,4,3,1]
    # 输出：0
    # 解释：在这个情况下, 没有交易完成, 所以最大利润为 0。
    solution3 = Solution()
    print(solution3.maxProfit(prices=[7, 6, 4, 3, 1]))

    # 输入：prices = [1]
    # 输出：0
    solution4 = Solution()
    print(solution4.maxProfit(prices=[1]))


if __name__ == '__main__':
    main()
