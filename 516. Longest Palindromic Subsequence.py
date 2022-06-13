# 首尾指针i，j相向移动
# dp方法含义：返回子串s[i..j]的最长回文子序列的长度
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        memo = [[0 for col in range(n)] for row in range(n)]

        def dp(i: int, j: int) -> int:
            # 递归出口
            if i==j and s[i]==s[j]:return 1
            elif i >= j: return 0

            # pre recursive:查memo
            if memo[i][j] != 0: return memo[i][j]

            # 递归：写memo
            if s[i] == s[j]:
                memo[i][j] = dp(i + 1, j - 1) + 2
            else:
                memo[i][j] = max(dp(i + 1, j), dp(i, j - 1))
            return memo[i][j]

        return dp(0, len(s) - 1)


def main():
    # Input: s = "bbbab"
    # Output: 4
    # Explanation: One possible longest palindromic subsequence is "bbbb".
    solution1 = Solution()
    print(solution1.longestPalindromeSubseq(s="bbbab"))

    # Input: s = "cbbd"
    # Output: 2
    # Explanation: One possible longest palindromic subsequence is "bb".
    solution2 = Solution()
    print(solution2.longestPalindromeSubseq(s="cbbd"))

    # Input "a"
    # Output 0
    # Expected 1
    solution3 = Solution()
    print(solution3.longestPalindromeSubseq(s="a"))

    # Input "aaa"
    # Output 2
    # Expected 3
    solution4 = Solution()
    print(solution4.longestPalindromeSubseq(s="aaa"))


if __name__ == '__main__':
    main()
