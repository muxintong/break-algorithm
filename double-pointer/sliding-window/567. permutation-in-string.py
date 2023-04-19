class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window = dict()
        need = dict()
        for c in s1:
            need.setdefault(c, 0)
            need[c] += 1

        left = 0
        right = 0
        valid = 0

        # expand window
        for right, in_win_char in enumerate(s2):
            # update window
            if in_win_char in need.keys():
                window.setdefault(in_win_char, 0)
                window[in_win_char] += 1
                if window[in_win_char] == need[in_win_char]:
                    valid += 1

            # update answer
            while right - left + 1 >= len(s1):
                if valid == len(need):
                    return True

                # shrink window
                out_win_char = s2[left]
                left += 1
                if out_win_char in need.keys():
                    if window[out_win_char] == need[out_win_char]:
                        valid -= 1
                    window[out_win_char] -= 1

        return False


def main():
    # Input: s1 = "ab", s2 = "eidbaooo"
    # Output: true
    # Explanation: s2 contains one permutation of s1("ba").
    solution1 = Solution()
    print(solution1.checkInclusion("ab", "eidbaooo"))

    # Input: s1 = "ab", s2 = "eidboaoo"
    # Output: false
    solution2 = Solution()
    print(solution2.checkInclusion(s1="ab", s2="eidboaoo"))


if __name__ == '__main__':
    main()
