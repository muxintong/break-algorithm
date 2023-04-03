"""
给你一个括号字符串 s ，它只包含字符 '(' 和 ')' 。一个括号字符串被称为平衡的当它满足：

任何左括号 '(' 必须对应两个连续的右括号 '))' 。
左括号 '(' 必须在对应的连续两个右括号 '))' 之前。
比方说 "())"， "())(())))" 和 "(())())))" 都是平衡的， ")()"， "()))" 和 "(()))" 都是不平衡的。

你可以在任意位置插入字符 '(' 和 ')' 使字符串平衡。

请你返回让 s 平衡的最少插入次数。

class Solution:
    def minInsertions(self, s: str) -> int:
        s = s.replace("))","]")
        count = s.count(")")
        s = s.replace(")","]")
        while "(]" in s:
            s = s.replace("(]","")
        return count + s.count("(") * 2 + s.count("]")
"""


class Solution:
    def minInsertions(self, s: str) -> int:
        # left记录需要添加的左括号数
        left = 0
        right = 0

        for i in range(len(s)):
            if s[i] == '(':
                right += 2
                # NOTE:此处需判断right的奇偶
                if right % 2 == 1:
                    left += 1
                    right -= 1
            elif s[i] == ')':
                right -= 1
                if right == -1:
                    left += 1
                    right += 2

        return left + right


def main():
    # 输入： "(()))(()))()())))"
    # 输出： 1
    # 预期结果： 4
    solution6 = Solution()
    print(solution6.minInsertions("(()))(()))()())))"))

    # 输入：s = "(()))"
    # 输出：1
    # 解释：第二个左括号有与之匹配的两个右括号，但是第一个左括号只有一个右括号。我们需要在字符串结尾额外增加一个 ')' 使字符串变成平衡字符串 "(())))" 。
    solution1 = Solution()
    print(solution1.minInsertions(s="(()))"))

    # 输入：s = "())"
    # 输出：0
    # 解释：字符串已经平衡了。
    solution2 = Solution()
    print(solution2.minInsertions(s="())"))

    # 输入：s = "))())("
    # 输出：3
    # 解释：添加 '(' 去匹配最开头的 '))' ，然后添加 '))' 去匹配最后一个 '(' 。
    solution3 = Solution()
    print(solution3.minInsertions(s="))())("))

    # 输入：s = "(((((("
    # 输出：12
    # 解释：添加 12 个 ')' 得到平衡字符串。
    solution4 = Solution()
    print(solution4.minInsertions(s="(((((("))

    # 输入：s = ")))))))"
    # 输出：5
    # 解释：在字符串开头添加 4 个 '(' 并在结尾添加 1 个 ')' ，字符串变成平衡字符串 "(((())))))))" 。
    solution5 = Solution()
    print(solution5.minInsertions(s=")))))))"))


if __name__ == '__main__':
    main()
