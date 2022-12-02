from typing import List
from collections import defaultdict
import bisect

"""
区别dict的setdefault(key,defaultValue)与defaultdict
若访问字典中的key值不存在时会报KeyError错误，这时候就可以使用defaultdict类来避免这种错误。
defaultdict是属于collections 模块下的一个工厂函数，用于构建字典对象，接收一个函数（可调用）对象为作为参数。
参数返回的类型是什么，key对应value就是什么类型。
"""


class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        pos = defaultdict(list)
        for i, v in enumerate(s):
            pos[v].append(i)
        res = len(words)
        for w in words:
            if len(w) > len(s):
                res -= 1
                continue
            p = -1
            for c in w:
                ps = pos[c]
                j = bisect.bisect_right(ps, p)
                if j == len(ps):
                    res -= 1
                    break
                p = ps[j]

        return res


def main():
    # 输入: s = "abcde", words = ["a","bb","acd","ace"]
    # 输出: 3
    # 解释: 有三个是 s 的子序列的单词: "a", "acd", "ace"。
    solution1 = Solution()
    print(solution1.numMatchingSubseq(s="abcde", words=["a", "bb", "acd", "ace"]))

    # 输入: s = "dsahjpjauf", words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]
    # 输出: 2
    solution2 = Solution()
    print(solution2.numMatchingSubseq(s="dsahjpjauf", words=["ahjpjau", "ja", "ahbwzgqnuk", "tnmlanowax"]))


if __name__ == '__main__':
    main()
