"""
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
每个右括号都有一个对应的相同类型的左括号。
"""
import char as char


class Solution:
    def leftof(self, c: char) -> char:
        if c == ')':
            return '('
        elif c == ']':
            return '['
        return '{'

    def isValid(self, s: str) -> bool:
        # 利用栈先进后出特性进行匹配
        stack = []

        for i in range(len(s)):
            # 遇到左括号入栈
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                stack.append(s[i])
            # 遇到右括号同栈顶元素进行匹配，若匹配进行弹栈，继续下一对括号的匹配
            elif len(stack) > 0 and self.leftof(s[i]) == stack[-1]:
                stack.pop()
            # 若右括号同栈顶元素不匹配则说明不符合题意
            else:
                return False

        # 最后返回栈是否为空：
        # 为空则说明完成了所有匹配返回True；
        # 不空说明还存在未匹配的左括号，返回False。
        return len(stack) == 0


def main():
    # # 输入：s = "()"
    # # 输出：true
    # solution1 = Solution()
    # print(solution1.isValid(s="()"))
    #
    # # 输入：s = "()[]{}"
    # # 输出：true
    # solution2 = Solution()
    # print(solution2.isValid(s="()[]{}"))
    #
    # # 输入：s = "(]"
    # # 输出：false
    # solution3 = Solution()
    # print(solution3.isValid(s="(]"))

    # "]"
    solution4 = Solution()
    print(solution4.isValid(s="]"))


if __name__ == '__main__':
    main()
