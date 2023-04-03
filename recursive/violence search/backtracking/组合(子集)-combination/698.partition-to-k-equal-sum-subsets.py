'''
NOTE:存在问题，还未解决
38 / 159 test cases passed.
Status: Time Limit Exceeded
'''
from typing import List


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        s = sum(nums)
        if s % k != 0 or k > len(nums): return False
        target = s // k

        buckets = [0 for i in range(k)]

        def backtrack(i: int, buckets: List) -> bool:
            # 1.递归出口：指针变量i遍历到len(nums)，
            # NOTE:出口条件为决策完最后一个元素[len(nums)-1]，i前移一位后指向len(nums)
            if i == len(nums):
                for bucket in buckets:
                    if bucket != target: return False
                # 若每个桶的和都=目标值target，则可均分为k等分
                return True

            # 2.遍历k个桶
            for j in range(k):
                # 2.1 递归前做选择，两种情况：nums[i] 可 | 不可 放入桶buckets[j]?
                if buckets[j] + nums[i] > target:
                    continue
                elif buckets[j] + nums[i] <= target:
                    buckets[j] += nums[i]
                    # 2.2 递归：将遍历nums这一过程打入递归
                    # NOTE:递归部分需要有返回值，否则该递归调用结果没有返回值，递归调用结果被舍弃，默认将None赋给res
                    if backtrack(i + 1, buckets): return True
                    # 2.3 递归后撤销选择
                    buckets[j] -= nums[i]
                    # NOTE：nums[i]装入哪个桶都不行
                    return False

        return backtrack(0, buckets)


def main():
    # Input: nums = [4,3,2,3,5,2,1], k = 4
    # Output: true
    # Explanation: It is possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.
    solution1 = Solution()
    print(solution1.canPartitionKSubsets(nums=[4, 3, 2, 3, 5, 2, 1], k=4))

    # Input: nums = [1,2,3,4], k = 3
    # Output: false
    solution2 = Solution()
    print(solution2.canPartitionKSubsets(nums=[1, 2, 3, 4], k=4))

    # Input: nums = [730,580,401,659,5524,405,1601,3,383,4391,4485,1024,1175,1100,2299,3908], k = 4
    # sum=28668  /  4 = 7167
    # Output: false
    solution3 = Solution()
    print(solution3.canPartitionKSubsets(
        nums=[730, 580, 401, 659, 5524, 405, 1601, 3, 383, 4391, 4485, 1024, 1175, 1100, 2299, 3908], k=4))


if __name__ == '__main__':
    main()
