from typing import List


class Solution:
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
