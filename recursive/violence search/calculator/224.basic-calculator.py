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
            for i in range(len(s)):
                if s[i].isdigit():
                    num = num * 10 + num(s[i])
                    return

                # base case: 当遇到左括号时开启递归调用
                if s[i] == '(': self.calculate(s[i:])

                if s[i].isdigit() == False and s[i] == ' ' or i == len(s) - 1:  # NOTE:
                    if s[i] == '+':
                        stack.append(+num)

                    if s[i] == '-':
                        stack.append(-num)

                    if s[i]=='*':
                        pre=stack.pop()
                        stack.append(pre*num)

                    if s[i]=='/'

                # base case：当遇到右括号时结束递归调用
                if s[i] == ')': break


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
