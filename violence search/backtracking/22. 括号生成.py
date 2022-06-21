from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def backtrack(S, left, right):
            if len(S) == 2 * n:
                ans.append(''.join(S))
                return
            if left < n:
                S.append('(')
                backtrack(S, left + 1, right)
                S.pop()
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
            if right < left: return
            if left < 0 or right < 0: return
            if left == 0 and right == 0:
                # res.append(track.copy())
                res.append(''.join(track.copy()))
                return
            # 尝试放一个右括号
            track.append(')')
            backtrack(left, right - 1)
            track.remove(')')
            # 尝试放一个左括号
            track.append('(')
            backtrack(left - 1, right)
            track.remove('(')
            
        backtrack(n, n)
        return res

    def generateParenthesis_leftToright(self, n: int) -> List[str]:
        res = []
        track = []

        def backtrack(left: int, right: int) -> None:
            if left < right: return
            # if left > right: return
            if left > n or right > n: return
            if left == n and right == n:
                res.append(''.join(track.copy()))
                return

            # right
            track.append(')')
            backtrack(left, right + 1)
            track.remove(')')
            # left
            track.append('(')
            backtrack(left + 1, right)
            track.remove('(')

        backtrack(0, 0)
        return res


def main():
    # 输入：n = 3
    # 输出：["((()))","(()())","(())()","()(())","()()()"]
    solution1 = Solution()
    print(solution1.generateParenthesis(n=3))
    print('---')

    # 输入：n = 3
    # 输出：["((()))","(()())","(())()","()(())","()()()"]
    solution1 = Solution()
    print(solution1.generateParenthesis_rightToleft(n=3))
    print('---')

    # 输入：n = 3
    # 输出：["((()))","(()())","(())()","()(())","()()()"]
    solution1 = Solution()
    print(solution1.generateParenthesis_leftToright(n=3))
    print('---')

    # # 输入：n = 1
    # # 输出：["()"]
    # solution2 = Solution()
    # print(solution2.generateParenthesis(n=1))


if __name__ == '__main__':
    main()
