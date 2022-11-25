from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        memory = {}

        # dp方法含义：返回nums[i:]能抢到的最大值
        def dp(i: int) -> int:
            if i >= len(nums): return 0
            # before recursive:find in memory
            if memory.get(i): return memory[i]

            # 针对nums[i]这一位置有如下两种选择：
            # 不抢i，去下家i+1：dp(i+1)
            # 抢i，去下下家i+2：nums[i]+dp(i+2)
            res = max(dp(i + 1), nums[i] + dp(i + 2))
            memory[i] = res

            return memory[i]

        return dp(0)


def main():
    # 输入：[1,2,3,1]
    # 输出：4
    # 解释：偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
    #    偷窃到的最高金额 = 1 + 3 = 4 。
    solution1 = Solution()
    print(solution1.rob([1, 2, 3, 1]))

    # 输入：[2,7,9,3,1]
    # 输出：12
    # 解释：偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
    #    偷窃到的最高金额 = 2 + 9 + 1 = 12 。
    solution2 = Solution()
    print(solution2.rob([2, 7, 9, 3, 1]))

    # time limit error
    solution1 = Solution()
    print(solution1.rob(
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0]))


if __name__ == '__main__':
    main()
