"""
这道题又涉及到两人的博弈，也可以用动态规划算法暴力试，比较麻烦。
但我们只要对规则深入思考，就会大惊失色：只要你足够聪明，你是必胜无疑的，因为你是先手。
因为题目有两个条件很重要：一是石头总共有偶数堆，石头的总数是奇数。这两个看似增加游戏公平性的条件，反而使该游戏成为了一个割韭菜游戏。我们以 piles=[2, 1, 9, 5] 讲解，假设这四堆石头从左到右的索引分别是 1，2，3，4。

如果我们把这四堆石头按索引的奇偶分为两组，即第 1、3 堆和第 2、4 堆，
那么这两组石头的数量一定不同，也就是说一堆多一堆少。
因为石头的总数是奇数，不能被平分。

而作为第一个拿石头的人，你可以控制自己拿到所有偶数堆，或者所有的奇数堆。
你最开始可以选择第 1 堆或第 4 堆。
如果你想要偶数堆，你就拿第 4 堆，这样留给对手的选择只有第 1、3 堆，他不管怎么拿，第 2 堆又会暴露出来，你就可以拿。
同理，如果你想拿奇数堆，你就拿第 1 堆，留给对手的只有第 2、4 堆，他不管怎么拿，第 3 堆又给你暴露出来了。

也就是说，你可以在第一步就观察好，奇数堆的石头总数多，还是偶数堆的石头总数多，然后步步为营，就一切尽在掌控之中了。

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        return True

"""

"""
动规解法：
1.dp 数组含义：
    dp[i][j].fir = x 表示，对于 piles[i...j] 这部分石头堆，先手能获得的最高分数为 x。
    dp[i][j].sec = y 表示，对于 piles[i...j] 这部分石头堆，后手能获得的最高分数为 y。
    
    举例理解一下，假设 piles = [2, 8, 3, 5]，索引从 0 开始，那么：
    dp[0][1].fir = 8 意味着：面对石头堆 [2, 8]，先手最多能够获得 8 分；
    dp[1][3].sec = 5 意味着：面对石头堆 [8, 3, 5]，后手最多能够获得 5 分。
    我们想求的答案是先手和后手最终分数之差，按照这个定义也就是 dp[0][n-1].fir - dp[0][n-1].sec，即面对整个 piles，先手的最优得分和后手的最优得分之差。

2.状态转移方程
    首先要找到所有「状态」和每个状态可以做的「选择」，然后择优。
    根据前面对 dp 数组的定义，状态显然有三个：开始的索引 i，结束的索引 j，当前轮到的人。
    dp[i][j][fir or sec]
        其中：
        0 <= i < piles.length
        i <= j < piles.length
    
    对于这个问题的每个状态，可以做的选择有两个：选择最左边的那堆石头，或者选择最右边的那堆石头。 我们可以这样穷举所有状态：
    n = piles.length
    for 0 <= i < n:
        for j <= i < n:
            for who in {fir, sec}:
                dp[i][j][who] = max(left, right)
    上面的伪码是动态规划的一个大致的框架，
    这道题的难点在于，两人足够聪明，而且是交替进行选择的，
    也就是说先手的选择会对后手有影响，这怎么表达出来呢？
    --------------------------------
    dp[i][j].fir = max(piles[i] + dp[i+1][j].sec, piles[j] + dp[i][j-1].sec)
    dp[i][j].fir = max(     选择最左边的石头堆     ,     选择最右边的石头堆      )
    # 解释：我作为先手，面对 piles[i...j] 时，有两种选择：
    # 要么我选择最左边的那一堆石头，然后面对 piles[i+1...j]
    # 但是此时轮到对方，相当于我变成了后手；
    # 要么我选择最右边的那一堆石头，然后面对 piles[i...j-1]
    # 但是此时轮到对方，相当于我变成了后手。
    
    if 先手选择左边:
        dp[i][j].sec = dp[i+1][j].fir
    if 先手选择右边:
        dp[i][j].sec = dp[i][j-1].fir
    # 解释：我作为后手，要等先手先选择，有两种情况：
    # 如果先手选择了最左边那堆，给我剩下了 piles[i+1...j]
    # 此时轮到我，我变成了先手；
    # 如果先手选择了最右边那堆，给我剩下了 piles[i...j-1]
    # 此时轮到我，我变成了先手。
    --------------------------------------
3.base case 
    dp[i][j].fir = piles[i]
    dp[i][j].sec = 0
    其中 0 <= i == j < n
    # 解释：i 和 j 相等就是说面前只有一堆石头 piles[i]
    # 那么显然先手的得分为 piles[i]
    # 后手没有石头拿了，得分为 0

    遍历方向：由已知状态base case=>最终状态即为遍历方向
    base case 是斜着的，而且我们推算 dp[i][j] 时需要用到 dp[i+1][j] 和 dp[i][j-1]：
    算法应该倒着遍历 dp 数组。
"""

from typing import List


class Pair:
    def __init__(self, first=0, second=0):
        self.first = first
        self.second = second


class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)

        # dp 数组含义：
        # dp[i][j].fir = x 表示，对于 piles[i...j] 这部分石头堆，先手能获得的最高分数为 x。
        # dp[i][j].sec = y 表示，对于 piles[i...j] 这部分石头堆，后手能获得的最高分数为 y。
        dp = [[Pair()] * n for row in range(n)]
        # base case
        for i in range(n):
            dp[i][i].first = piles[i]
            dp[i][i].second = 0

        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n, 1):
                # 做选择：选择左 or 右
                left = piles[i] + dp[i + 1][j].second
                right = piles[j] + dp[i][j - 1].second
                # 先手左选择：先手会选择左右两侧最大的结果，其选择影响后手的选择
                if left > right:
                    dp[i][j].first = left
                    dp[i][j].second = dp[i + 1][j].first  # 后手变为先手
                else:
                    dp[i][j].first = right
                    dp[i][j].second = dp[i][j - 1].second

        res = dp[0][n - 1]
        if res.first - res.second >= 0:
            return True
        else:
            return False


def main():
    # 输入：piles = [5,3,4,5]
    # 输出：true
    # 解释：
    # Alice 先开始，只能拿前 5 颗或后 5 颗石子 。
    # 假设他取了前 5 颗，这一行就变成了 [3,4,5] 。
    # 如果 Bob 拿走前 3 颗，那么剩下的是 [4,5]，Alice 拿走后 5 颗赢得 10 分。
    # 如果 Bob 拿走后 5 颗，那么剩下的是 [3,4]，Alice 拿走后 4 颗赢得 9 分。
    # 这表明，取前 5 颗石子对 Alice 来说是一个胜利的举动，所以返回 true 。
    solution1 = Solution()
    print(solution1.stoneGame(piles=[5, 3, 4, 5]))

    # 输入：piles = [3,7,2,3]
    # 输出：true
    solution1 = Solution()
    print(solution1.stoneGame(piles=[3, 7, 2, 3]))


if __name__ == '__main__':
    main()
