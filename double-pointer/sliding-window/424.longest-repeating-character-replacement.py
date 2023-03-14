class Solution:
    """
    滑动窗口：
    在滑动过程中统计各个字符出现的频率，window[char]=frequency
    因为最后求得的最长长度的解一定是在出现频次最多的字母上，在改变其他字母得到的最长连续长度
    滑动过程中，用窗口长度减去窗口中出现频次最大的字符的长度，若值大于k，则需减小窗口长度知道等于k

    """
    def characterReplacement(self, s: str, k: int) -> int:
        window={}
        left=0
        right=0
        res=0
        for s_r in s:
            right+=1
            window.setdefault(s_r,0)
            window[s_r]+=1

            while right-left+1
