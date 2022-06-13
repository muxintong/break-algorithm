from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        memory = dict()

        def dp(i: int):
            # base case
            if i == 0:
                memory[0] = nums[0]
                return nums[0]

            if memory.get(i): return memory[i]

            # recursive
            if nums[i - 1] > 0:
                memory[i] = nums[i] + dp(i - 1)
            else:
                memory[i] = max(nums[i], nums[i] + dp(i - 1))

            return memory[i]

        max_subarr_len = 0
        for i in range(len(nums)):
            max_subarr_len = max(max_subarr_len, dp(i))

        return max_subarr_len


def main():
    # Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
    # Output: 6
    # Explanation: [4,-1,2,1] has the largest sum = 6.
    solution1 = Solution()
    print(solution1.maxSubArray(nums=[-2, 1, -3, 4, -1, 2, 1, -5, 4]))

    # Input: nums = [5,4,-1,7,8]
    # Output: 23
    solution1 = Solution()
    print(solution1.maxSubArray(nums=[5, 4, -1, 7, 8]))

    # Input: nums = [1]
    # Output: 1
    solution1 = Solution()
    print(solution1.maxSubArray(nums=[1]))


if __name__ == '__main__':
    main()
