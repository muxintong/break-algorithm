"""
https://leetcode.com/problems/reverse-string/
https://labuladong.github.io/algo/2/18/23/
"""
from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s) - 1

        while left < right:
            temp = s[left]
            s[left] = s[right]
            s[right] = temp

            left += 1
            right -= 1


def main():
    # Input: s = ["h","e","l","l","o"]
    # Output: ["o","l","l","e","h"]
    # s = ["h", "e", "l", "l", "o"]
    solution1 = Solution()
    solution1.reverseString(s)
    print(s)

    # Input: s = ["H","a","n","n","a","h"]
    # Output: ["h","a","n","n","a","H"]
    s = ["H","a","n","n","a","h"]
    solution2 = Solution()
    solution2.reverseString(s)
    print(s)


if __name__ == '__main__':
    main()
