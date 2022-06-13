# dp[i][j] 的含义是：对于 s1[1..i] 和 s2[1..j]，它们的 LCS 长度是 dp[i][j]。
'''
NOTE: 对于m行n列的二维数组
    java二维数组初始化：int[][] dp = new int[m + 1][n + 1];                         <=前行后列
    python二维数组初始化：dp = [[0 for col in range(n+1)] for row in range(m+1)]    <=前列后行
'''
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        # 定义：text1[0..i-1]和text2[0..j-1]的lcs长度为dp[i][j]
        dp = [[0 for col in range(n+1)] for row in range(m+1)]
        # 目标：text1[0..m-1]和text2[0..n-1]的lcs长度，即dp[m][n]
        # base case: dp[0][..]=dp[..][0]=0

        for i in range(1, m + 1, 1):
            for j in range(1, n + 1, 1):
                # 现在i和j从1开始，故需减1
                if text1[i - 1] == text2[j - 1]:
                    # text1[i-1]和text2[j-1]相等，则该字符必在lcs中
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    # text1[i-1]和text2[j-1]不相等，则这两个字符必有一个不在lcs中
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

        return dp[m][n]


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
