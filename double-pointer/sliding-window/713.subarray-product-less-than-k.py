from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        left = 0
        right = 0

        res = 0
        muti = 1
        for right, num in enumerate(nums):
            muti = muti * num
            if muti < k: res += 1

            while left <= right:
                muti = muti / nums[left]
                left += 1
                if muti < k: res += 1

        return res


def main():
    # 输入：nums = [10,5,2,6], k = 100
    # 输出：8
    # 解释：8 个乘积小于 100 的子数组分别为：[10]、[5]、[2],、[6]、[10,5]、[5,2]、[2,6]、[5,2,6]。
    # 需要注意的是 [10,5,2] 并不是乘积小于 100 的子数组。
    solution1 = Solution()
    print(solution1.numSubarrayProductLessThanK(nums=[10, 5, 2, 6], k=100))

    # 输入：nums = [1,2,3], k = 0
    # 输出：0
    solution2 = Solution()
    print(solution2.numSubarrayProductLessThanK(nums=[1, 2, 3], k=0))


if __name__ == '__main__':
    main()
