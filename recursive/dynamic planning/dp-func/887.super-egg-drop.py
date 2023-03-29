class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        memo = {}

        def dp(k, n):
            if (k, n) not in memo:
                if n == 0:
                    ans = 0
                elif k == 1:
                    ans = n
                else:
                    lo, hi = 1, n
                    # keep a gap of 2 x values to manually check later
                    while lo + 1 < hi:
                        x = (lo + hi) // 2
                        t1 = dp(k - 1, x - 1)
                        t2 = dp(k, n - x)

                        if t1 < t2: lo = x
                        elif t1 > t2: hi = x
                        else: lo = hi = x

                    ans = 1 + min(max(dp(k - 1, x - 1), dp(k, n - x))
                                  for x in (lo, hi))

                memo[k, n] = ans
            return memo[k, n]

        return dp(k, n)


def main():
    # 输入：k = 1, n = 2
    # 输出：2
    # 解释：
    # 鸡蛋从 1 楼掉落。如果它碎了，肯定能得出 f = 0 。
    # 否则，鸡蛋从 2 楼掉落。如果它碎了，肯定能得出 f = 1 。
    # 如果它没碎，那么肯定能得出 f = 2 。
    # 因此，在最坏的情况下我们需要移动 2 次以确定 f 是多少。
    solution1 = Solution()
    print(solution1.superEggDrop(k=1, n=2))

    # 输入：k = 2, n = 6
    # 输出：3
    solution2 = Solution()
    print(solution2.superEggDrop(k=2, n=6))

    # 输入：k = 3, n = 14
    # 输出：4
    solution3 = Solution()
    print(solution3.superEggDrop(k=3, n=14))


if __name__ == '__main__':
    main()
