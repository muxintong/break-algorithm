class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = dict()

        left = 0
        right = 0

        res = 0
        # expand window
        for right, in_win_char in enumerate(s):
            # update window
            window.setdefault(in_win_char, 0)
            window[in_win_char] += 1

            # shrink window
            while window[in_win_char] > 1:
                # shrink window
                out_win_char = s[left]
                left += 1
                # update window
                window[out_win_char] -= 1

            # update answer
            res = max(res, right - left + 1)

        return res


def main():
    # Input: s = "abcabcbb"
    # Output: 3
    # Explanation: The answer is "abc", with the length of 3.
    solution1 = Solution()
    print(solution1.lengthOfLongestSubstring("abcabcbb"))

    # Input: s = "bbbbb"
    # Output: 1
    # Explanation: The answer is "b", with the length of 1.
    solution2 = Solution()
    print(solution2.lengthOfLongestSubstring("bbbbb"))


if __name__ == '__main__':
    main()
