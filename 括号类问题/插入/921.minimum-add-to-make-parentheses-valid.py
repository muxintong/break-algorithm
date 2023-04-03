class Solution:
    # 返回 为使结果字符串 s 有效而必须添加的最少括号数。
    def minAddToMakeValid(self, s: str) -> int:
        # left记录需要添加的左括号数
        left = 0
        # right记录需要添加的右括号数
        right = 0
        for i in range(len(s)):
            # 若遇到一个左括号，需要的右括号数应该加1
            if s[i] == '(':
                right += 1
            # 若遇到一个右括号，需要的右括号数-1
            elif s[i] == ')':
                right -= 1
                # 若右括号减少至负值时说明此时应该增加左括号数，同时将需要的右括号数重新置为0
                if right == -1:
                    right = 0
                    left += 1

        return left + right


def main():
    # 输入：s = "())"
    # 输出：1
    solution1 = Solution()
    print(solution1.minAddToMakeValid(s="())"))

    # 输入：s = "((("
    # 输出：3
    solution2 = Solution()
    print(solution2.minAddToMakeValid(s="((("))


if __name__ == '__main__':
    main()
