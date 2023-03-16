"""
给你一个字符串 s 。我们要把这个字符串划分为尽可能多的片段，同一字母最多出现在一个片段中。
注意，划分结果需要满足：将所有划分结果按顺序连接，得到的字符串仍然是 s 。
返回一个表示每个字符串片段的长度的列表。
https://books.halfrost.com/leetcode/ChapterFour/0700~0799/0763.Partition-Labels/

core mind：
先记录每个字符出现的次数，若滑动的窗口内所有字符均达最大出现次数，
则该窗口符合题意，将其加入结果集；
同时右窗口后移一位，左窗口指向右窗口，开始新一轮滑动。
"""
from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        count = {}
        for c in s:
            count.setdefault(c, 0)
            count[c] += 1

        left = 0
        right = 0
        res = []
        window = {}

        for right, c in enumerate(s):
            window.setdefault(c, 0)
            window[c] += 1

            if self.cmp(count, window):
                res.append(right - left + 1)
                right += 1
                left = right

        return res

    def cmp(self, d1: dict, d2: dict) -> bool:
        for k2, v2 in d2.items():
            if v2 < d1[k2]: return False
        return True


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
