from typing import List


class Solution:
    '''
    【子集|组合（元素可重不可复选）】
        需要进行剪枝，如果一个节点有多条值相同的树枝相邻，则只遍历第一条，剩下的都剪掉，不要去遍历。
        体现在代码上，需要先进行排序，让相同的元素靠在一起，如果发现 nums[i] == nums[i-1]，则跳过。
    '''

    # Input: nums = [1,2,2]
    # Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # 【元素可重复的子集问题】
        # 1.先对nums数组排序
        # 按升序排序，使相同元素靠在一起，后续在递归过程中对于相同元素只处理一次，后续相同元素跳过。
        nums.sort()
        res = []
        track = []

        def backtrack(start: int):
            # update res position
            # NOTE:此处添加的是路径列表track的一份拷贝值，否则在后续移除元素过程中致使track为空，最后导致res中什么也没加进去
            res.append(track.copy())

            for i in range(start, len(nums), 1):
                # 只处理一次相同元素，注意移动指针前需进行边界条件限制：
                #                                       指针前移i-1，需先保证 i>start
                #                                       指针后移1+1，需先保证 i<len(nums)-1
                # wrong:
                # [[], [1], [1, 2], [1, 2, 2], [1, 2], [2], [2, 2], [2]]
                # if nums[i] < len(nums) - 1 and nums[i] == nums[i + 1]:
                #     continue
                # right:
                # 剪枝逻辑，值相同的相邻树枝，只遍历第一条
                # [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]
                # 2.回溯方法中，针对排好序的数组：跳过相同元素
                if i > start and nums[i] == nums[i - 1]: continue
                    
                track.append(nums[i])
                backtrack(i + 1)
                track.remove(nums[i])

        backtrack(0)
        return res


def main():
    # Input: nums = [1,2,2]
    # Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
    solution1 = Solution()
    print(solution1.subsetsWithDup(nums=[1, 2, 2]))

    # Input: nums = [0]
    # Output: [[],[0]]
    solution2 = Solution()
    print(solution2.subsetsWithDup(nums=[0]))


if __name__ == '__main__':
    main()
