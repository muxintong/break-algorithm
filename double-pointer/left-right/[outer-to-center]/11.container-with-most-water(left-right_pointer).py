"""
https://labuladong.github.io/algo/4/31/129/
https://leetcode.com/problems/container-with-most-water/
"""

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        # 左右指针l，r分别指向头尾，二者相向移动
        l = 0
        r = len(height) - 1

        res = 0
        while l < r:
            s = min(height[l], height[r]) * (r - l)
            res = max(res, s)
            # NOTE:左右指针的移动，移动指针高度小的，
            # 因为是求面积的最大值，移动高度小的才有可能使该高度变大，进而增大面积
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return res


def main():
    # Input: height = [1,8,6,2,5,4,8,3,7]
    # Output: 49
    solution1 = Solution()
    print(solution1.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))

    # Input: height = [1,1]
    # Output: 1
    solution2 = Solution()
    print(solution2.maxArea([1,1]))


if __name__ == '__main__':
    main()
