"""
给你一个字符串表达式 s ，请你实现一个基本计算器来计算并返回它的值。

注意:不允许使用任何将字符串作为数学表达式计算的内置函数，比如 eval() 。

NOTE:
    · s 由数字、'+'、'-'、'('、')'、和 ' ' 组成
    · s 表示一个有效的表达式
    · '+' 不能用作一元运算(例如， "+1" 和 "+(2 + 3)" 无效)
    · '-' 可以用作一元运算(即 "-1" 和 "-(2 + 3)" 是有效的)
    · 输入中不存在两个连续的操作符
"""


class Solution:
    def calculate(self, s: str) -> int:
        res = 0

        def helper():
            stack = []
            num = 0
            sign = '+'
            for i, v in enumerate(self.s):
                if v.isdigit():
                    num = num * 10 + int(i)

                if v.isdigit() == False and v != ' ' or i == len(s) - 1:
                    if v == '+':
                        stack.append(+v)
                    if v == '-':
                        stack.append(-v)

                for s in stack:
                    self.res += s

        helper()
        return res


def main():
    # 输入：s = "1 + 1"
    # 输出：2
    solution1 = Solution()
    print(solution1.calculate(s="1 + 1"))

    # 输入：s = " 2-1 + 2 "
    # 输出：3
    solution2 = Solution()
    print(solution2.calculate(s=" 2-1 + 2 "))

    # 输入：s = "(1+(4+5+2)-3)+(6+8)"
    # 输出：23
    solution3 = Solution()
    print(solution3.calculate(s="(1+(4+5+2)-3)+(6+8)"))


if __name__ == '__main__':
    main()
