from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        memory = [n] * n

        # dp定义：从索引p跳到最后一格，至少需要dp(nums,p)步
        def dp(p: int) -> int:
            if p >= n - 1: return 0

            if memory[p] != n: return memory[p]

            steps = nums[p]
            for i in range(1, steps + 1):
                subproblems = dp(p + i)
                memory[p] = min(memory[p], subproblems + 1)

            return memory[p]

        return dp(0)

    def jump_greedy(self, nums: List[int]) -> int:
        n = len(nums)
        # i、end标记了可以选择的跳跃步数
        end = 0
        # farthes记录最远的跳跃距离
        farthest = 0
        # jumps记录跳跃步数
        jumps = 0
        # NOTE: i最后的取值范围，不可取到n-1
        for i in range(n - 1):
            farthest = max(farthest, nums[i] + i)
            if end == i:
                jumps += 1
                end = farthest
        return jumps


def main():
    # 输入: nums = [2,3,1,1,4]
    # 输出: 2
    # 解释: 跳到最后一个位置的最小跳跃数是 2。
    #      从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。
    solution1 = Solution()
    print(solution1.jump_greedy(nums=[2, 3, 1, 1, 4]))

    # 输入: nums = [2,3,0,1,4]
    # 输出: 2
    solution1 = Solution()
    print(solution1.jump_greedy(nums=[2, 3, 0, 1, 4]))


if __name__ == '__main__':
    main()
