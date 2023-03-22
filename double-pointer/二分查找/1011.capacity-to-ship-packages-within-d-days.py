from typing import List


class Solution:
    # 设题目所求运输的载重为自变量x，f为当运载能力为x时的运输天数days
    def f(self, weights: List[int], x: int):
        cap = x
        days = 1
        for w in weights:
            if cap < w:
                days += 1
                cap = x
                cap -= w
            elif cap >= w:
                cap -= w

        return days

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = 0
        right = 1
        for w in weights:
            # 载重的最小值：weights数组中元素的最大值，因为每次至少得装走意见货物
            left = max(left, w)
            # 载重的最大值：weights数组所有元素之和，即一次把所有货物都装走
            right += w
        while left < right:
            mid = left + (right - left) // 2
            if self.f(weights, mid) == days:
                right = mid
            elif self.f(weights, mid) > days:
                left = mid + 1
            elif self.f(weights, mid) < days:
                right = mid
        return left


def main():
    # 输入：weights = [1,2,3,4,5,6,7,8,9,10], days = 5
    # 输出：15
    # 解释：
    # 船舶最低载重 15 就能够在 5 天内送达所有包裹，如下所示：
    # 第 1 天：1, 2, 3, 4, 5
    # 第 2 天：6, 7
    # 第 3 天：8
    # 第 4 天：9
    # 第 5 天：10
    #
    # 请注意，货物必须按照给定的顺序装运，因此使用载重能力为 14 的船舶并将包装分成 (2, 3, 4, 5), (1, 6, 7), (8), (9), (10) 是不允许的。
    solution1 = Solution()
    print(solution1.shipWithinDays(weights=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], days=5))

    # 输入：weights = [3,2,2,4,1,4], days = 3
    # 输出：6
    # 解释：
    # 船舶最低载重 6 就能够在 3 天内送达所有包裹，如下所示：
    # 第 1 天：3, 2
    # 第 2 天：2, 4
    # 第 3 天：1, 4
    solution1 = Solution()
    print(solution1.shipWithinDays(weights=[3, 2, 2, 4, 1, 4], days=3))

    # 输入：weights = [1,2,3,1,1], days = 4
    # 输出：3
    # 解释：
    # 第 1 天：1
    # 第 2 天：2
    # 第 3 天：3
    # 第 4 天：1, 1
    solution1 = Solution()
    print(solution1.shipWithinDays(weights=[1, 2, 3, 1, 1], days=4))


if __name__ == '__main__':
    main()
