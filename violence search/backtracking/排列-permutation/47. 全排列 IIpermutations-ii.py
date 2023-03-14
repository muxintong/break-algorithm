'''
solution3:存在问题，带解决
'''
from typing import List


class Solution:
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

    def permuteUnique_wrong1(self, nums: List[int]) -> List[List[int]]:
        res = []
        track = []
        used = [False for i in range(len(nums))]

        def backtrack(nums: List[int]):
            # 递归出口
            if len(track) == len(nums):
                res.append(track.copy())
                return

            for i in range(len(nums)):
                if used[i] == True:
                    continue
                elif used[i] == False:
                    track.append(nums[i])
                    used[i] = True

                backtrack(nums)

                track.remove(nums[i])
                used[i] = False

        backtrack(nums)
        res_nodup_tuple = list(set([tuple(i) for i in res]))
        res_nodup_list = [list(i) for i in res_nodup_tuple]
        return res_nodup_list

    def permuteUnique_wrong2(self, nums: List[int]) -> List[List[int]]:
        res = []
        track = []
        used = [False for i in range(len(nums))]

        nums.sort()

        def backtrack(used: List[bool]) -> None:
            if len(track) == len(nums):
                res.append(track.copy())
                return

            for i in range(len(nums)):
                # if i > 0 and nums[i] == nums[i - 1] and not used[i-1]: continue
                # if i > 0 and nums[i] == nums[i - 1] and used[i-1]: continue

                if used[i]: continue
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]: continue
                # if i > 0 and nums[i] == nums[i - 1] and used[i-1]: continue

                used[i] = True
                track.append(nums[i])

                backtrack(used)

                track.remove(nums[i])
                used[i] = False

        backtrack(used)
        return res


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


def main():
    # Input: nums = [1,1,2]
    # Output:
    # [[1,1,2],
    #  [1,2,1],
    #  [2,1,1]]
    solution1 = Solution()
    print(solution1.permuteUnique(nums=[1, 1, 2]))

    # Input: nums = [1,2,3]
    # Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
    solution2 = Solution()
    print(solution2.permuteUnique(nums=[1, 2, 3]))

    # Input:
    # [2,2,1,1]
    # Output:
    # [[1,2,1,2],[1,2,2,1],[2,2,1,1],[2,1,1,2],[1,1,2,2]]
    # Expected:
    # [[1,1,2,2],[1,2,1,2],[1,2,2,1],[2,1,1,2],[2,1,2,1],[2,2,1,1]]
    solution3 = Solution()
    print(solution3.permuteUnique([2, 2, 1, 1]))
    # print(solution3.permuteUnique_wrong1([2, 2, 1, 1]))
    # print(solution3.permuteUnique_wrong2([2, 2, 1, 1]))

    print(solution3.permuteUnique([2, 2, 2]))


if __name__ == '__main__':
    main()
