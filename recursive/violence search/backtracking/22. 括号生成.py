from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def backtrack(S, left, right):
            if len(S) == 2 * n:
                ans.append(''.join(S))
                return

            # 递归调用过程中进行左右括号相对位置判断
            if left < n:
                S.append('(')
                backtrack(S, left + 1, right)
                S.pop()
            # 注意：此处是右括号索引要【小于】左括号索引
            if right < left:
                S.append(')')
                backtrack(S, left, right + 1)
                S.pop()

        backtrack([], 0, 0)
        return ans

    def generateParenthesis_rightToleft(self, n: int) -> List[str]:
        if n == 0: return []
        res = []
        track = []

        def backtrack(left: int, right: int) -> None:
            # 使用base case限制左右括号相对位置
            # 从右向左放置，右大左小为正确形式
            if right < left: return
            # 从右向左放置，从你减至0，结束条件为减至0
            if left < 0 or right < 0: return
            if left == 0 and right == 0:
                # res.append(track.copy())
                res.append(''.join(track.copy()))
                return

            # 尝试放一个右括号
            track.append(')')
            backtrack(left, right - 1)
            track.remove(')')
            # track.pop()

            # 尝试放一个左括号
            track.append('(')
            backtrack(left - 1, right)
            track.remove('(')
            # track.pop()

        backtrack(n, n)
        return res

    def generateParenthesis_leftToright(self, n: int) -> List[str]:
        res = []
        track = []

        def backtrack(left: int, right: int) -> None:
            # 从左向右放置，则左大右小为正确形式
            if left < right: return
            # if left > right: return
            # 从左向右放置，从0开始放到n，结束条件不能大于n
            if left > n or right > n: return
            if left == n and right == n:
                res.append(''.join(track.copy()))
                return

            # right
            track.append(')')
            backtrack(left, right + 1)
            track.remove(')')
            # track.pop()

            # left
            track.append('(')
            backtrack(left + 1, right)
            track.remove('(')
            # track.pop()

        backtrack(0, 0)
        return res


def main():
    # 输入：n = 3
    # 输出：["((()))","(()())","(())()","()(())","()()()"]
    solution1 = Solution()
    print(solution1.generateParenthesis(n=3))
    print(solution1.generateParenthesis_leftToright(n=3))
    print(solution1.generateParenthesis_rightToleft(n=3))
    print('---')

    # 输入：n = 1
    # 输出：["()"]
    solution2 = Solution()
    print(solution2.generateParenthesis(n=1))
    print(solution2.generateParenthesis_leftToright(n=1))
    print(solution2.generateParenthesis_rightToleft(n=1))


if __name__ == '__main__':
    main()
