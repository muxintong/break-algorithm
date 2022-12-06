from typing import List


class Solution:
    # 若吃香蕉的速度是x根/小时，则需f(x)小时吃完所有的香蕉
    def f(self, piles: List[int], x):
        hours = 0
        for i in range(0, len(piles), 1):
            hours += piles[i] // x  # NOTE:此处为整除双斜线，而非带有小数点的单斜线除法
            if piles[i] % x != 0: hours += 1
        return hours

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # 自变量x，即吃香蕉速度的取值范围
        # 初始化left为吃香蕉的最小速度
        left = 1
        # 初始化right为吃香蕉的最大速度+1，+1的原因是使用左闭右开区间
        # right = 1000000000 + 1
        right = 0
        for i in range(0, len(piles)):
            right = max(piles[i], right)
        right += 1

        while left < right:
            mid = left + (right - left) // 2
            if self.f(piles, mid) == h:
                # 要求计算x的最小值，即为求解左侧边界问题，需收缩右边界
                right = mid
            elif self.f(piles, mid) > h:
                # 函数值偏大，且f为关于自变量x的单调递减函数，
                # 故需增大x，即x的左边界left右移
                left = mid + 1
            elif self.f(piles, mid) < h:
                right = mid

        return left


def main():
    # 输入：piles = [3,6,7,11], h = 8
    # 输出：4
    solution1 = Solution()
    print(solution1.minEatingSpeed(piles=[3, 6, 7, 11], h=8))

    # 输入：piles = [30,11,23,4,20], h = 5
    # 输出：30
    solution1 = Solution()
    print(solution1.minEatingSpeed(piles=[30, 11, 23, 4, 20], h=5))

    # 输入：piles = [30,11,23,4,20], h = 6
    # 输出：23
    solution1 = Solution()
    print(solution1.minEatingSpeed(piles=[30, 11, 23, 4, 20], h=6))


if __name__ == '__main__':
    main()
