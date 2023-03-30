""""
给你一个字符串表达式 s ，请你实现一个基本计算器来计算并返回它的值。

整数除法仅保留整数部分。

你可以假设给定的表达式总是有效的。所有中间结果将在 [-231, 231 - 1] 的范围内。

注意：不允许使用任何将字符串作为数学表达式计算的内置函数，比如 eval() 。

NOTE:
    · 1 <= s.length <= 3 * 105
    · s 由整数和算符 ('+', '-', '*', '/') 组成，中间由一些空格隔开
    · s 表示一个 有效表达式
    · 表达式中的所有整数都是非负整数，且在范围 [0, 231 - 1] 内
    · 题目数据保证答案是一个 32-bit 整数
"""
from typing import List


class Solution:
    def calculate(self, s: str) -> int:

        def helper(s: List) -> int:
            res = 0
            stack = []
            num = 0
            sign = '+'
            for i, v in enumerate(s):
                if v.isdigit():
                    num = num * 10 + int(v)

                # base case：当遇到左括号时开启递归调用
                if v == '(': helper(s)

                if not v.isdigit() and v != ' ' or i == len(s) - 1:
                    if v == '+':
                        stack.append(+num)
                        break
                    if v == '-':
                        stack.append(-num)
                        break
                    if v == '*':
                        stack[-1] = stack[-1] * num
                        break
                    if v == '-':
                        stack[-1] = stack[-1] // num
                        break
                    # 更新符号，同时将数字清零
                    sign = v
                    num = 0

                # base case：遇到右括号结束递归
                if v == ')': break

            return sum(stack)

        return helper(list(s))


def main():
    # 输入：s = "3+2*2"
    # 输出：7
    solution1 = Solution()
    print(solution1.calculate(s="3+2*2"))

    # # 输入：s = " 3/2 "
    # # 输出：1
    # solution2 = Solution()
    # print(solution2.calculate(s=" 3/2 "))
    #
    # # 输入：s = " 3+5 / 2 "
    # # 输出：5
    # solution3 = Solution()
    # print(solution3.calculate(s=" 3+5 / 2 "))


if __name__ == '__main__':
    main()
