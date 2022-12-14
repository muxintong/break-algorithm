from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1: return True

        n = len(nums)
        farthest = 0
        for i in range(n):
            farthest = max(farthest, i + nums[i])
            if farthest <= i:
                return False

        return farthest >= n - 1


def main():
    # # 输入：nums = [2,3,1,1,4]
    # # 输出：true
    # # 解释：可以先跳 1 步，从下标 0 到达下标 1, 然后再从下标 1 跳 3 步到达最后一个下标。
    # solution1 = Solution()
    # print(solution1.canJump(nums=[2, 3, 1, 1, 4]))
    #
    # # 输入：nums = [3,2,1,0,4]
    # # 输出：false
    # # 解释：无论怎样，总会到达下标为 3 的位置。但该下标的最大跳跃长度是 0 ， 所以永远不可能到达最后一个下标。
    # solution1 = Solution()
    # print(solution1.canJump(nums=[3, 2, 1, 0, 4]))

    # 输入：[0]
    # 输出：false
    # 预期结果：true
    # solution1 = Solution()
    # print(solution1.canJump(nums=[0]))

    # 输入：[2,0,0]
    # 输出：false
    # 预期结果：true
    solution1 = Solution()
    print(solution1.canJump(nums=[2,0,0]))


if __name__ == '__main__':
    main()
