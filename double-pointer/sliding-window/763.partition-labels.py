"""
给你一个字符串 s 。我们要把这个字符串划分为尽可能多的片段，同一字母最多出现在一个片段中。
注意，划分结果需要满足：将所有划分结果按顺序连接，得到的字符串仍然是 s 。
返回一个表示每个字符串片段的长度的列表。
https://books.halfrost.com/leetcode/ChapterFour/0700~0799/0763.Partition-Labels/
"""
from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        window = {}
        for c in enumerate(s):
            window.setdefault(c, 0)
            window[c] += 1

        visited = []
        for c in s:
            visited[c] = False

        left = 0
        right = 0
        res = []
        for right, in_win_char in enumerate(s):
            window[in_win_char] -= 1
            visited[in_win_char]=1


def main():
    # 输入：s = "ababcbacadefegdehijhklij"
    # 输出：[9,7,8]
    # 解释：
    # 划分结果为 "ababcbaca"、"defegde"、"hijhklij" 。
    # 每个字母最多出现在一个片段中。
    # 像 "ababcbacadefegde", "hijhklij" 这样的划分是错误的，因为划分的片段数较少。
    solution1 = Solution()
    print(solution1.partitionLabels(s="ababcbacadefegdehijhklij"))

    # 输入：s = "eccbbbbdec"
    # 输出：[10]
    solution2 = Solution()
    print(solution1.partitionLabels(s="eccbbbbdec"))


if __name__ == '__main__':
    main()
