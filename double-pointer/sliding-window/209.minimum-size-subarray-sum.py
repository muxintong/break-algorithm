from typing import List

"""
给定一个含有 n 个正整数的数组和一个正整数 target 。

找出该数组中满足其和 ≥ target 的长度最小的 连续子数组 [numsl, numsl+1, ..., numsr-1, numsr] ，并返回其长度。如果不存在符合条件的子数组，返回 0 。
"""


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        right = 0
        sum = 0
        res = len(nums) + 1
        # expand window
        for right, num in enumerate(nums):
            sum += num

            while sum >= target:
                # update answer
                res = min(res, right - left + 1)
                # shrink window
                left += 1
                sum -= nums[left]

        return 0 if res == len(nums) + 1 else res


def main():
    # 输入：target = 7, nums = [2,3,1,2,4,3]
    # 输出：2
    # 解释：子数组 [4,3] 是该条件下的长度最小的子数组。
    solution1 = Solution()
    print(solution1.minSubArrayLen(target=7, nums=[2, 3, 1, 2, 4, 3]))

    # 输入：target = 4, nums = [1,4,4]
    # 输出：1
    solution1 = Solution()
    print(solution1.minSubArrayLen(target=4, nums=[1, 4, 4]))

    # 输入：target = 11, nums = [1,1,1,1,1,1,1,1]
    # 输出：0
    solution1 = Solution()
    print(solution1.minSubArrayLen(target=11, nums=[1, 1, 1, 1, 1, 1, 1, 1]))


if __name__ == '__main__':
    main()
