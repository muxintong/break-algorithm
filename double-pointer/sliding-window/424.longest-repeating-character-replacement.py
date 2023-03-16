class Solution:
    """
    给你一个字符串 s 和一个整数 k 。你可以选择字符串中的任一字符，并将其更改为任何其他大写英文字符。该操作最多可执行 k 次。
    在执行上述操作后，返回包含相同字母的最长子字符串的长度。

    core mind：
    滑动窗口问题，在滑动过程中统计各个字符出现的频率，window[char]=frequency
    因为最后求得的最长长度的解一定是在出现频次最多的字母上，在改变其他字母得到的最长连续长度
    滑动过程中，用窗口长度减去窗口中出现频次最大的字符的长度，若值大于k，则需减小窗口长度知道等于k
    class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, count, max_cnt = 0, defaultdict(int), 0
        for r, c in enumerate(s):
            count[c] += 1
            if count[c] > max_cnt:
                max_cnt = count[c]
            if r - l + 1 - max_cnt > k:
                count[s[l]] -= 1
                l += 1
        return r - l + 1
    """

    def characterReplacement(selfs, s: str, k: int) -> int:
        window = {}
        l = 0
        r = 0
        res = 0
        max_count = 0
        for r, c in enumerate(s):
            window.setdefault(c, 0)
            window[c] += 1
            if window[c] > max_count: max_count = window[c]
            if r - l + 1 - max_count > k:
                window[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res

    def characterReplacement2(self, s: str, k: int) -> int:
        window = {}
        dict()
        left = 0
        right = 0
        res = 0
        for right, in_char in enumerate(s):
            window.setdefault(in_char, 0)
            window[in_char] += 1

            len_win = right - left + 1
            max_in_win_char_frequency = self.max_value(window)
            while len_win - max_in_win_char_frequency > k and left < right:
                window[s[left]] -= 1
                left += 1

            res = max(res, right - left + 1)

        return res

    def max_value(self, window: dict) -> int:
        res = 0
        for v in window.values():
            res = max(res, v)
        return res


def main():
    # 输入：s = "ABAB", k = 2
    # 输出：4
    # 解释：用两个'A'替换为两个'B',反之亦然。
    solution1 = Solution()
    print(solution1.characterReplacement(s="ABAB", k=2))
    print(solution1.characterReplacement2(s="ABAB", k=2))
    print('---')

    # 输入：s = "AABABBA", k = 1
    # 输出：4
    # 解释：
    # 将中间的一个'A'替换为'B',字符串变为 "AABBBBA"。
    # 子串 "BBBB" 有最长重复字母, 答案为 4。
    solution2 = Solution()
    print(solution2.characterReplacement(s="AABABBA", k=1))
    print(solution2.characterReplacement2(s="AABABBA", k=1))
    print('---')

    # "EOEMQLLQTRQDDCOERARHGAAARRBKCCMFTDAQOLOKARBIJBISTGNKBQGKKTALSQNFSABASNOPBMMGDIOETPTDICRBOMBAAHINTFLH"
    # 7
    # right=11 ; wrong=10
    solution3 = Solution()
    print(solution3.characterReplacement(
        s="EOEMQLLQTRQDDCOERARHGAAARRBKCCMFTDAQOLOKARBIJBISTGNKBQGKKTALSQNFSABASNOPBMMGDIOETPTDICRBOMBAAHINTFLH", k=7))
    print(solution3.characterReplacement2(
        s="EOEMQLLQTRQDDCOERARHGAAARRBKCCMFTDAQOLOKARBIJBISTGNKBQGKKTALSQNFSABASNOPBMMGDIOETPTDICRBOMBAAHINTFLH", k=7))


if __name__ == '__main__':
    main()
