from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        dp = [[0] * 2 for row in range(n)]
        for i in range(n):
            if i - 1 == -1:
                dp[i][0] = 0
                dp[i][1] = -prices[i] - fee
                # dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i] - fee)
                #          = max(dp[-1][1], dp[-1][0] - prices[i] - fee)
                #          = max(-无穷, 0 - prices[i] - fee)
                #          = -prices[i] - fee
                continue
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            # 每次交易都需要支付手续费，只需在买入股票时减去相应的手续费即可。
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i] - fee)

        return dp[n - 1][0]


def main():
    # 输入：prices = [1, 3, 2, 8, 4, 9], fee = 2
    # 输出：8
    # 解释：能够达到的最大利润:
    # 在此处买入 prices[0] = 1
    # 在此处卖出 prices[3] = 8
    # 在此处买入 prices[4] = 4
    # 在此处卖出 prices[5] = 9
    # 总利润: ((8 - 1) - 2) + ((9 - 4) - 2) = 8
    solution1 = Solution()
    print(solution1.maxProfit(prices=[1, 3, 2, 8, 4, 9], fee=2))

    # 输入：prices = [1,3,7,5,10,3], fee = 3
    # 输出：6
    solution2 = Solution()
    print(solution2.maxProfit(prices=[1, 3, 7, 5, 10, 3], fee=3))


if __name__ == '__main__':
    main()
