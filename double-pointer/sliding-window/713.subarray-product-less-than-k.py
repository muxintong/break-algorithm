from typing import List


class Solution:
    """
    给你一个整数数组 nums 和一个整数 k ，
    请你返回子数组内所有元素的乘积严格小于 k 的连续子数组的数目。

    core mind：
    滑动窗口问题，右窗口向前滑动时不断累计乘积，
    直到窗口内乘积值大于等于k，左窗口向前滑动减小窗口内乘积值。

    class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k<=1: return 0
        prod = 1
        ans = 0
        left = 0
        for right, num in enumerate(nums):
            prod *= num
            while prod >= k:
                prod //= nums[left]
                left+=1
            ans += right-left+1
        return ans
    """
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1: return 0

        left = 0
        right = 0

        res = 0
        multi = 1
        for right, num in enumerate(nums):
            multi = multi * num

            while multi >= k:
                multi = multi // nums[left]
                left += 1
            # NOTE: res？？？
            res += right - left + 1

        return res

    def numSubarrayProductLessThanK2(self, nums: List[int], k: int) -> int:
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
    # [10,9,10,4,3,8,3,3,6,2,10,10,9,3]
    # 19
    solution2 = Solution()
    print(solution2.numSubarrayProductLessThanK(nums=[10, 9, 10, 4, 3, 8, 3, 3, 6, 2, 10, 10, 9, 3], k=19))


if __name__ == '__main__':
    main()
