class Solution:
    def palindrome(self, s: str, left: int, right: int):
        # NOTE:边界条件
        # 左边界需取到数组第一个元素0，右边界需取到数组最后一个元素len-1
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        res = s[left + 1:right]
        return res

    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1: return s

        res = ""
        for i in range(len(s)):
            # 分奇odd、偶even讨论
            odd = self.palindrome(s, i, i)
            even = self.palindrome(s, i, i + 1)
            if len(res) < len(odd): res = odd
            if len(res) < len(even): res = even

        return res


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
