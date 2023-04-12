from typing import List

"""
给定一个字符串 s 和一个字符串数组 words。 words 中所有字符串 长度相同。

 s 中的 串联子串 是指一个包含 words 中所有字符串以任意顺序排列连接起来的子串。

例如，如果 words = ["ab","cd","ef"]， 那么 "abcdef"， "abefcd"，"cdabef"， "cdefab"，"efabcd"， 和 efcdab" 都是串联子串。 
"acdbef" 不是串联子串，因为他不是任何 words 排列的连接。

返回所有串联字串在 s 中的开始索引。你可以以 任意顺序 返回答案。
"""

"""
# class Solution:
#     def findSubstring(self, s: str, words: List[str]) -> List[int]:
#         res = []
#         wl = len(words)
#         el = len(words[0])
#         n = len(s)
#         words.sort()
#         def check(t, words):
#             for i, j in zip(t, words):
#                 if i != j:
#                     return False
#             return True
#         for i in range(n-wl*el+1):
#             t = [s[i+j*el:i+(j+1)*el] for j in range(wl)]
#             t.sort()
            
#             if check(t, words):
#                 print(words)
#                 print(t)
#                 res.append(i)
#         return res

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not words:
            return []
        w_len, s_len = len(words[0]), len(s)
        t_len = w_len * len(words)  # 子串的长度

        word_dict = {}  # words的哈希表
        for word in words:
            word_dict[word] = word_dict.get(word, 0) + 1

        ans = []
        for offset in range(w_len):
            lo, lo_max = offset, s_len - t_len
            while lo <= lo_max:
                tmp_dict = word_dict.copy()
                match = True
                for hi in range(lo + t_len, lo, -w_len):    # 从尾到头搜索单词
                    word = s[hi - w_len: hi]
                    if tmp_dict.get(word, 0) == 0:
                        match = False
                        break   # 当前单词不符合要求 直接停止这个子串的搜索
                    tmp_dict[word] -= 1
                if match:
                    ans.append(lo)
                lo = hi     # 对lo直接赋值 这就是相比法二优化的地方
        return ans
"""
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        window = dict()
        need = dict()
        len_words = 0
        for word in words:
            for c in word:
                need.setdefault(c, 0)
                need[c] += 1
            len_words = len(words) * len(word)

        left = 0
        right = 0
        valid = 0
        res = []
        for right, c in enumerate(s):
            window.setdefault(c, 0)
            window[c] += 1
            if c in need.keys():
                if window[c] == need[c]:
                    valid += 1

            while right - left + 1 >= len_words:
                if valid == len(need) and right - left + 1 == len_words: res.append(left)
                d_c = s[left]
                if d_c in need.keys():
                    if window[d_c] == need[d_c]:
                        valid -= 1
                window[d_c] -= 1
                left += 1

        return res


def main():
    # 输入：s = "barfoothefoobarman", words = ["foo","bar"]
    # 输出：[0,9]
    # 解释：因为 words.length == 2 同时 words[i].length == 3，连接的子字符串的长度必须为 6。
    # 子串 "barfoo" 开始位置是 0。它是 words 中以 ["bar","foo"] 顺序排列的连接。
    # 子串 "foobar" 开始位置是 9。它是 words 中以 ["foo","bar"] 顺序排列的连接。
    # 输出顺序无关紧要。返回 [9,0] 也是可以的。
    solution1 = Solution()
    print(solution1.findSubstring(s="barfoothefoobarman", words=["foo", "bar"]))

    # 输入：s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
    # 输出：[]
    # 解释：因为 words.length == 4 并且 words[i].length == 4，所以串联子串的长度必须为 16。
    # s 中没有子串长度为 16 并且等于 words 的任何顺序排列的连接。
    # 所以我们返回一个空数组。
    solution2 = Solution()
    print(solution2.findSubstring(s="wordgoodgoodgoodbestword", words=["word", "good", "best", "word"]))

    # 输入：s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
    # 输出：[6,9,12]
    # 解释：因为 words.length == 3 并且 words[i].length == 3，所以串联子串的长度必须为 9。
    # 子串 "foobarthe" 开始位置是 6。它是 words 中以 ["foo","bar","the"] 顺序排列的连接。
    # 子串 "barthefoo" 开始位置是 9。它是 words 中以 ["bar","the","foo"] 顺序排列的连接。
    # 子串 "thefoobar" 开始位置是 12。它是 words 中以 ["the","foo","bar"] 顺序排列的连接。
    solution3 = Solution()
    print(solution3.findSubstring(s="barfoofoobarthefoobarman", words=["bar", "foo", "the"]))


if __name__ == '__main__':
    main()
