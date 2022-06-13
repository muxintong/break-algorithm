class Solution:
    def findAnagrams(self, s: str, p: str):
        window = dict()
        need = dict()
        for c in p:
            need.setdefault(c, 0)
            need[c] += 1

        left = 0
        right = 0
        valid = 0

        res = []
        # expand window
        for right, in_win_char in enumerate(s):
            # update window
            if in_win_char in need.keys():
                window.setdefault(in_win_char, 0)
                window[in_win_char] += 1
                if window[in_win_char] == need[in_win_char]:
                    valid += 1

            # shrink window
            while right - left + 1 >= len(p):
                # update answer
                if valid == len(need):
                    res.append(left)

                out_win_char = s[left]
                left += 1
                if out_win_char in need.keys():
                    if window[out_win_char] == need[out_win_char]:
                        valid -= 1
                    window[out_win_char] -= 1

        return res


def main():
    # Output: [0,1,2]
    solution1 = Solution()
    print(solution1.findAnagrams("abab", "ab"))

    # Output: [0,6]
    solution2 = Solution()
    print(solution2.findAnagrams("cbaebabacd", "abc"))

    # "baa"
    # "aa"
    # Output []
    # Expected [1]
    solution3 = Solution()
    print(solution3.findAnagrams("baa", "aa"))


if __name__ == '__main__':
    main()
