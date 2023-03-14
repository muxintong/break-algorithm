from typing import List

"""
给定一个非负整数数组 A，如果该数组每对相邻元素之和是一个完全平方数，则称这一数组为正方形数组。

返回 A 的正方形排列的数目。两个排列 A1 和 A2 不同的充要条件是存在某个索引 i，使得 A1[i] != A2[i]。

输入：[1,17,8]
输出：2
解释：
[1,8,17] 和 [17,8,1] 都是有效的排列。
"""
'''
    【排列（元素可重不可复选）】
    '''


def permuteUnique(self, nums: List[int]) -> List[List[int]]:
    nums.sort()
    self.res = []
    check = [0 for i in range(len(nums))]

    self.backtrack([], nums, check)
    return self.res


def backtrack(self, sol, nums, check):
    if len(sol) == len(nums):
        self.res.append(sol)
        return

    for i in range(len(nums)):
        if check[i] == 1:
            continue
        if i > 0 and nums[i] == nums[i - 1] and check[i - 1] == 0:
            continue
        check[i] = 1
        self.backtrack(sol + [nums[i]], nums, check)
        check[i] = 0


class Solution:
    """
    排列问题：元素可重，不可复选
    """

    def numSquarefulPerms(self, nums: List[int]) -> int:
        nums.sort()
        perms = []

        track = []

        used = [False for i in range(len(nums))]

        def backtrack(used: List[bool]) -> None:
            if len(track) == len(nums):
                perms.append(track.copy())

            for i in range(len(nums)):
                if used[i]: continue
                if i > 0 and nums[i] == nums[i - 1] and nums[i - 1] == False: continue

                used[i] = True
                track.append(nums[i])

                backtrack(used)

                track.remove(nums[i])
                used[i] = False

        backtrack(used)
        return perms

        # res = []
        # for


def main():
    # 输入：[1,17,8]
    # 输出：2
    # 解释：
    # [1,8,17] 和 [17,8,1] 都是有效的排列。
    solution1 = Solution()
    print(solution1.numSquarefulPerms([1, 17, 8]))

    # 输入：[2,2,2]
    # 输出：1
    solution2 = Solution()
    print(solution2.numSquarefulPerms([2, 2, 2]))


if __name__ == '__main__':
    main()
