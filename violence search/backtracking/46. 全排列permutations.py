'''
NOTE:LeetCode提示超时时，去掉导包语句及所有注释即可通过
'''
from typing import List


class Solution:
    '''
    【排列（元素无重不可复选）】
    '''
    def permute(self, nums: List[int]) -> List[List[int]]:
        # 最终结果集result：存储track
        res = []

        # 符合题意的选择列表指针集：存储符合题意的选择列表指针i对应的值nums[i]
        track = []
        # 标记数组used，用于记录nums[i]是否被使用
        used = [False for j in range(len(nums))]

        def backtrack(used: List[bool])->None:
            # 结束条件：当track的长度等于nums的长度时，说明已经完成了一个全排列
            if len(track) == len(nums):
                # NOTE：此处添加的是track的副本，否则当后续撤销选择时，track指向的内容将不存在，导致res全为空
                res.append(track.copy())
                return

            for i in range(len(nums)):
                # 1.1 针对不符合题意的选择i：跳过该选择，进行下一次循环判断
                if used[i]: continue
                # 1.2 针对符合题意的选择i：加入存储 符合题意的选择 的路径列表tarck ，并将i标记为已经被使用过。
                track.append(nums[i])
                used[i] = True

                # 2. core：recursive
                backtrack(used)

                # 3.递归之后撤销选择，还原该决策树：路径列表中移出nums[i]这一选择，并将i标记为未被使用。
                track.remove(nums[i])
                used[i] = False

        backtrack(used)
        return res


class Solution2:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        track = []
        used = [False for i in range(len(nums))]

        def backtrack(used: List[bool]) -> None:
            '''
            排列问题：使用标记一个元素是否被访问过的used数组
            组合问题：使用位置变量start，控制元素之间的相对顺序，是传入【i+1：元素i无重，不可复用】还是【i：元素i可重，可复用】
            '''
            # 递归出口：当track的长度增至和nums长度一致时，即为一个符合题意的全排列，将该track加入结果集res中
            if len(track) == len(nums):
                res.append(track.copy())

            for i in range(len(nums)):
                if used[i]: continue
                used[i] = True
                track.append(nums[i])

                backtrack(used)

                used[i] = False
                track.remove(nums[i])

        backtrack(used)
        return res


def main():
    # Input: nums = [1,2,3]
    # Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
    solution1 = Solution()
    print(solution1.permute(nums=[1, 2, 3]))

    # Input: nums = [0,1]
    # Output: [[0,1],[1,0]]
    solution2 = Solution()
    print(solution2.permute(nums=[0, 1]))

    # Input: nums = [1]
    # Output: [[1]]
    solution3 = Solution()
    print(solution3.permute(nums=[1]))


if __name__ == '__main__':
    main()
