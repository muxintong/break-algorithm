class Solution_dpfunc:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        memo = [[0 for col in range(n)] for row in range(m)]

        def dp(i: int, j: int) -> int:
            # base case
            if i == -1 or j == -1: return 0

            # pre recursive：查memo
            if memo[i][j] != 0: return memo[i][j]

            # recursive
            res = 0
            if text1[i] == text2[j]:
                res = dp(i - 1, j - 1) + 1
            else:
                res = max(dp(i - 1, j), dp(i, j - 1))

            # post recursive: 写memo
            memo[i][j] = res

            return memo[i][j]

        return dp(m - 1, n - 1)


def main():
    # Input: text1 = "abcde", text2 = "ace"
    # Output: 3
    # Explanation: The longest common subsequence is "ace" and its length is 3.
    solution1 = Solution()
    print(solution1.longestCommonSubsequence(text1="abcde", text2="ace"))

    # Input: text1 = "abc", text2 = "abc"
    # Output: 3
    # Explanation: The longest common subsequence is "abc" and its length is 3.
    solution2 = Solution()
    print(solution2.longestCommonSubsequence(text1="abc", text2="abc"))

    # Input: text1 = "abc", text2 = "def"
    # Output: 0
    # Explanation: There is no such common subsequence, so the result is 0.
    solution3 = Solution()
    print(solution3.longestCommonSubsequence(text1="abc", text2="def"))


if __name__ == '__main__':
    main()
