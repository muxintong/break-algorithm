from typing import List


class Solution:
    '''
    【子集（元素无重不可复选）】
    '''
    # Input: nums = [1,2,3]
    # Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
    # 子集问题 <==> 组合问题 ：通过保证元素之间的相对顺序不变【即在递归调用过程中使：列表指针变量i+1】来防止出现重复的子集
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # 结果集res:List[List[int]]，存储各个track
        res = []
        # 记录各个子集：List[int]
        track = []

        def backtrack(start: int):
            # 0.结果集更新位置
            res.append(track.copy())

            # 2.注意i的起始位start
            # NOTE:以下语句将会时i在0、1之间反复横跳，导致无限递归
            # for i in range(len(nums)):
            for i in range(start, len(nums), 1):
                # 递归前：将选择i的值 加入 路径列表track
                track.append(nums[i])
                # 递归：通过保证元素之间的相对顺序不变【即在递归调用过程中使：列表指针变量i+1】来防止出现重复的子集
                backtrack(i + 1)
                # 递归后：将选择i的值 移出于 路径列表track
                track.remove(nums[i])

        backtrack(0)
        return res


def main():
    # Input: nums = [1,2,3]
    # Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
    solution1 = Solution()
    print(solution1.subsets(nums=[1, 2, 3]))

    print('---')

    # Input: nums = [0]
    # Output: [[],[0]]
    solution2 = Solution()
    print(solution2.subsets(nums=[0]))


if __name__ == '__main__':
    main()
