from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        track = []

        # backtrack返回放置n对括号的组合数
        def backtrack(left: int, right: int):
            if left == n and right == n:
                res.append(''.join(track.copy()))
                return

            # 尝试放一个右括号
            track.append(')')
            backtrack(left + 1, right)
            track.remove(')')

            # 尝试放一个左括号
            track.append('(')
            backtrack(left, right + 1)
            track.remove('(')

        backtrack(0,0)
        return res


def main():
    # 输入：n = 3
    # 输出：["((()))","(()())","(())()","()(())","()()()"]
    solution1 = Solution()
    print(solution1.generateParenthesis(n=3))

    # 输入：n = 1
    # 输出：["()"]
    solution2 = Solution()
    print(solution2.generateParenthesis(n=1))


if __name__ == '__main__':
    main()
