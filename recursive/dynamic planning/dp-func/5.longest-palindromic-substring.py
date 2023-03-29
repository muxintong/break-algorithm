class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 1. dp[i][j]定义：对字符串s[i:j]来说其最长回文子串的长度是dp[i][j]
        dp = [[0 for col in range(len(s))] for row in range(len(s))]

        # 2. base case：对于单个字符，其最长回文子串的长度应为1
        for i in range(len(s)):
            dp[i][i] = 1

        # 3. 依据不同情况(s[i]与s[j]是否相等)列出状态转移方程
        for i in range(len(s) - 1, 0, -1):
            for j in range(i + 1, len(s), 1):
                if s[i] == s[j]:
                    dp[i][j] = dp[i - 1][j - 1] + 2
                elif s[i] != s[j]:
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

        return dp[0][len(s) - 1]


def main():
    # Input: s = "babad"
    # Output: "bab"
    # Explanation: "aba" is also a valid answer.
    soution1 = Solution()
    print(soution1.longestPalindrome("babad"))

    # Input: s = "cbbd"
    # Output: "bb"
    soution2 = Solution()
    print(soution2.longestPalindrome("cbbd"))

    # Input "a"
    # Output ""
    # Expected "a"
    soution2 = Solution()
    print(soution2.longestPalindrome("a"))


if __name__ == '__main__':
    main()
