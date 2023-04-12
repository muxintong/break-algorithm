"""
DNA序列 由一系列核苷酸组成，缩写为 'A', 'C', 'G' 和 'T'.。

例如，"ACGAATTCCG" 是一个 DNA序列 。
在研究 DNA 时，识别 DNA 中的重复序列非常有用。

给定一个表示 DNA序列 的字符串 s ，返回所有在 DNA 分子中出现不止一次的 长度为 10 的序列(子字符串)。
你可以按 任意顺序 返回答案。
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        all = dict()
        for i in range(len(s)):
            try:
                str = s[i:i + 10]
                if str in all:
                    all[str] += 1
                else:
                    all[str] = 1
            except:
                pass

        pr = []
        for k, v in all.items():
            if v > 1:
                pr.append(k)

        return pr

"""
from typing import List


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        need_len = 10
        window = dict()

        left = 0
        right = need_len
        while right < len(s) + 1:
            window.setdefault(s[left:right], 0)
            window[s[left:right]] += 1
            right += 1
            left += 1

        res = []
        for _, k in enumerate(window):
            if window[k] > 1: res.append(k)
        return res


def main():
    # 输入：s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
    # 输出：["AAAAACCCCC","CCCCCAAAAA"]
    solution1 = Solution()
    print(solution1.findRepeatedDnaSequences(s="AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))

    # 输入：s = "AAAAAAAAAAAAA"
    # 输出：["AAAAAAAAAA"]
    solution2 = Solution()
    print(solution2.findRepeatedDnaSequences(s="AAAAAAAAAAAAA"))

    # 输入： "AAAAAAAAAAA"
    # 输出： []
    # 预期结果： ["AAAAAAAAAA"]
    solution3 = Solution()
    print(solution3.findRepeatedDnaSequences("AAAAAAAAAAA"))


if __name__ == '__main__':
    main()
