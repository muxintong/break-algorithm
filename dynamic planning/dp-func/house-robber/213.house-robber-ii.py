from typing import List

"""
环形房子：首尾房间不能同时被抢，
那么只可能有三种不同情况：
- 都不被抢；
- 第一间房子被抢最后一间不抢；
- 最后一间房子被抢第一间不抢。
"""


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return nums[0]
        memory = {}

        def dp(i: int, j: int) -> int:
            if i >= len(nums): return 0

            if memory.get((i, j)): return memory[(i, j)]

            memory[(i, j)] = max(dp(i + 1, j), nums[i] + dp(i + 2, j))

            return memory[(i, j)]

        return max(dp(0, n - 2), dp(1, n - 1))


def main():
    # 输入：nums = [2,3,2]
    # 输出：3
    # 解释：你不能先偷窃 1 号房屋（金额 = 2），然后偷窃 3 号房屋（金额 = 2）, 因为他们是相邻的。
    solution1 = Solution()
    print(solution1.rob([2, 3, 2]))

    # # 输入：nums = [1,2,3,1]
    # # 输出：4
    # # 解释：你可以先偷窃 1 号房屋（金额 = 1），然后偷窃 3 号房屋（金额 = 3）。
    # #     偷窃到的最高金额 = 1 + 3 = 4 。
    # solution2 = Solution()
    # print(solution2.rob([1, 2, 3, 1]))
    #
    # # 输入：nums = [1,2,3]
    # # 输出：3
    # solution3 = Solution()
    # print(solution3.rob(nums=[1, 2, 3]))


if __name__ == '__main__':
    main()
