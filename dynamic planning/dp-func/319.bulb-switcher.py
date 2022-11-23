from math import sqrt


class Solution:
    def bulbSwitch(self, n: int) -> int:
        return int(sqrt(n))


def main():
    # 输入：n = 3
    # 输出：1
    # 解释：
    # 初始时, 灯泡状态 [关闭, 关闭, 关闭].
    # 第一轮后, 灯泡状态 [开启, 开启, 开启].
    # 第二轮后, 灯泡状态 [开启, 关闭, 开启].
    # 第三轮后, 灯泡状态 [开启, 关闭, 关闭].
    #
    # 你应该返回 1，因为只有一个灯泡还亮着。
    solution1 = Solution()
    print(solution1.bulbSwitch(n=3))

    # 输入：n = 0
    # 输出：0
    solution2 = Solution()
    print(solution2.bulbSwitch(n=0))

    # 输入：n = 1
    # 输出：1
    solution3 = Solution()
    print(solution3.bulbSwitch(n=1))


if __name__ == '__main__':
    main()
