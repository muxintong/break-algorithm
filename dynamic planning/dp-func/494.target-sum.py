"""
本例含有重复子问题，需使用备忘录优化，原因如下：
【仅抽象出递归框架，查看不同状态转移之间的路径是否唯一】：唯一，不存在重叠子问题，无需备忘录
                                                   不唯一，存在重叠子问题，需使用备忘录去重

本题递归框架为：
def dp(i: int, target: int) -> int:
    dp(i - 1, target - nums[i])
    dp(i - 1, target + nums[i])
如果nums[i] = 0，这样就出现了两个「状态」完全相同的递归函数，无疑这样的递归计算就是重复的。
这就是重叠子问题，而且只要我们能够找到一个重叠子问题，那一定还存在很多的重叠子问题。
因此，状态 (i, remain) 是可以用备忘录技巧进行优化的：
！！！用Python的【哈希表dict】来做备忘录，其中dict的【key为dp方法所有入参组成的元组对：(dp_arg1, dp_arg2, ...)，即所有的可变状态的组合】
memory = dict()
{(dp_arg1_state1, dp_arg2_state2, ...):value1, (dp_arg1_state2, dp_arg2_state2, ...):value2, (dp_arg1_state3, dp_arg2_state3, ...):value3, ...}
"""

from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memory = dict()

        def dp(i: int, target: int) -> int:
            # base case
            if i == 0:
                if nums[i] == 0 and nums[i] == target:
                    return 2
                elif nums[i] == target or -nums[i] == target:
                    return 1
                else:
                    return 0

            # pre recursive:查memory
            # NOTE:需要把i和target的组合作为key，而不能仅把i作为key
            #      ！！！即需要把dp方法中所包含的所有可变状态的组合作为key！！！
            if memory.get((i,target)): return memory[(i,target)]

            # recursive:写memory
            ways_add = dp(i - 1, target - nums[i])
            ways_plus = dp(i - 1, target + nums[i])
            memory[(i,target)] = ways_add + ways_plus

            # post recursive:
            return memory[(i,target)]

        return dp(len(nums) - 1, target)
      
    def findTargetSumWays_WithoutMemo_TimeLimitError(self, nums: List[int], target: int) -> int:
        def dp(i: int, target: int) -> int:
            # base case
            if i == 0:
                if nums[i] == 0 and nums[i] == target:
                    return 2
                elif nums[i] == target or -nums[i] == target:
                    return 1
                else:
                    return 0

            # recursive
            ways_add = dp(i - 1, target - nums[i])
            ways_plus = dp(i - 1, target + nums[i])
            ways = ways_add + ways_plus

            return ways

        return dp(len(nums) - 1, target)


def main():
    # Input: nums = [1,1,1,1,1], target = 3
    # Output: 5
    # Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
    # -1 + 1 + 1 + 1 + 1 = 3
    # +1 - 1 + 1 + 1 + 1 = 3
    # +1 + 1 - 1 + 1 + 1 = 3
    # +1 + 1 + 1 - 1 + 1 = 3
    # +1 + 1 + 1 + 1 - 1 = 3
    solution1 = Solution()
    print(solution1.findTargetSumWays(nums=[1, 1, 1, 1, 1], target=3))

    # Input: nums = [1], target = 1
    # Output: 1
    solution2 = Solution()
    print(solution2.findTargetSumWays(nums=[1], target=1))

    # Input: [0,0,0,0,0,0,0,0,1] 1
    # Output: 128
    # Expected: 256
    solution3 = Solution()
    print(solution3.findTargetSumWays([0, 0, 0, 0, 0, 0, 0, 0, 1], 1))


if __name__ == '__main__':
    main()
