# https://labuladong.github.io/algo/3/24/77/


from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # dp[i]:其值为以nums[i]结尾的LIS值
        # 求出数组中以每个数字结尾的LIS，最终答案为其中最大的
        dp = [1] * len(nums)
        for i in range(0, len(nums), 1):
            for j in range(0, i, 1):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)

        res = 0
        for i in range(len(nums)):
            res = max(res, dp[i])

        return res


def main():
    # Input: nums = [10,9,2,5,3,7,101,18]
    # Output: 4
    # Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
    solution1 = Solution()
    print(solution1.lengthOfLIS(nums=[10, 9, 2, 5, 3, 7, 101, 18]))

    # Input: nums = [0,1,0,3,2,3]
    # Output: 4
    solution2 = Solution()
    print(solution2.lengthOfLIS(nums=[0, 1, 0, 3, 2, 3]))

    # Input: nums = [7,7,7,7,7,7,7]
    # Output: 1
    solution3 = Solution()
    print(solution3.lengthOfLIS(nums=[7, 7, 7, 7, 7, 7, 7]))


if __name__ == '__main__':
    main()
