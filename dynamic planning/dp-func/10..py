class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memory = {}

        def dp(i: int, j: int) -> bool:
            if i == len(s) - 1:
                if j == len(p) - 1:
                    return True
                else:
                    while j + 1 < len(p):
                        if p[j + 1] != '*': return False
                        j += 2
                    return True
            if j == len(p) - 1 and i != len(s): return False

            if memory.get((i, j)): return memory[(i, j)]

            res = False
            if s[i] == p[j] or p[j] == '.':
                if j < len(p) - 1 and p[j + 1] != '*':
                    res = dp(i + 1, j + 1)
                elif j < len(p) - 1 and p[j + 1] == '*':
                    res = dp(i, j + 2) or dp(i, j)
            else:
                if j < len(p) - 1 and p[j + 1] != '*':
                    res = False
                elif j < len(p) - 1 and p[j + 1] == '*':
                    res = dp(i, j + 2)
            memory[(i, j)] = res
            return memory[(i, j)]

        return dp(0, 0)


def main():
    # Input: s = "aa", p = "a"
    # Output: false
    # Explanation: "a" does not match the entire string "aa".
    # solution1 = Solution()
    # print(solution1.isMatch(s="aa", p="a"))

    # Input: s = "aa", p = "a*"
    # Output: true
    # Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
    solution2 = Solution()
    print(solution2.isMatch(s="aa", p="a*"))
    #
    # # Input: s = "ab", p = ".*"
    # # Output: true
    # # Explanation: ".*" means "zero or more (*) of any character (.)".
    # solution3 = Solution()
    # print(solution3.isMatch(s="ab", p=".*"))
    #
    # # "aab" "c*a*b"
    # # 输出：false
    # # 预期结果：true
    # solution4 = Solution()
    # print(solution4.isMatch(s="aab", p="c*a*b"))


if __name__ == '__main__':
    main()
