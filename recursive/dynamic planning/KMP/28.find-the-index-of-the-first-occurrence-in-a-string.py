class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        N = len(haystack)
        M = len(needle)
        # dp[当前状态][当前遇到的字符]=下个状态
        dp = [[0] * 256 for row in range(M)]
        # base case
        dp[0][ord(needle[0])] = 1
        # 与当前状态相同的前一个状态X，初始化为0
        X = 0
        # 构建dp数组的状态转移图
        for j in range(1, M, 1):
            for c in range(0, 256, 1):
                dp[j][c] = dp[X][c]
            dp[j][ord(needle[0])] = j + 1
            # 更新前一个相同状态X
            X = dp[X][ord(needle[0])]

        # needle指针j初始指向0
        j = 0
        # haystack指针i
        for i in range(N):
            # 计算pat的下一个状态
            j = dp[j][ord(needle[0])]
            # 到达终止状态，返回匹配的起始索引
            if j == M: return i - M + 1
        # 最终没到达终止状态，匹配失败
        return -1


def main():
    # 输入：haystack = "sadbutsad", needle = "sad"
    # 输出：0
    # 解释："sad" 在下标 0 和 6 处匹配。
    # 第一个匹配项的下标是 0 ，所以返回 0 。
    solution1 = Solution()
    print(solution1.strStr(haystack = "sadbutsad", needle = "sad"))

    # 输入：haystack = "leetcode", needle = "leeto"
    # 输出：-1
    # 解释："leeto" 没有在 "leetcode" 中出现，所以返回 -1 。
    solution2 = Solution()
    print(solution2.strStr(haystack = "tleetcode", needle = "et"))


if __name__ == '__main__':
    main()
