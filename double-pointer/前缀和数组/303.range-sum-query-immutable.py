from typing import List
from itertools import accumulate
import operator


class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.n = len(nums)
        self.prefix_nums = [0] * (self.n + 1)

    def sumRange(self, left: int, right: int) -> int:
        # prefix_nums = list(accumulate(self.nums, operator.add))
        # print(prefix_nums)
        # return prefix_nums[right] - prefix_nums[left]
        return self.prefix_sum[right + 1] - self.prefix_nums[left]

    def prefix_sum(self, nums: List[int]) -> int:
        for i in range(1, self.n):
            self.prefix_nums[i] = self.prefix_nums[i - 1] + nums[i - 1]


# Your NumArray object will be instantiated and called as such:
# 输入：
# ["NumArray", "sumRange", "sumRange", "sumRange"]
# [[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
# 输出：
# [null, 1, -1, -3]
#
# 解释：
numArray = NumArray([-2, 0, 3, -5, 2, -1])
print(numArray.sumRange(0, 2))  # return 1 ((-2) + 0 + 3)
print(numArray.sumRange(2, 5))
print(numArray.sumRange(0, 5))
