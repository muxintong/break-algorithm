import bisect
from typing import List

"""
NOTE:本例不适用python二分查找库bisect的左右边界查找方法
bisect_left(a, x, lo=0, hi=None, *, key=None)
        Return the index where to 【insert】 item x in list a, assuming a is sorted.

        The return value i is such that all e in a[:i] have e < x, and all e in
        a[i:] have e >= x.  So if x already appears in the list, a.insert(i, x) will
        【insert】 just 【before】 the leftmost x already there.
 
bisect_right(a, x, lo=0, hi=None, *, key=None)
        Return the index where to insert item x in list a, assuming a is sorted.

        The return value i is such that all e in a[:i] have e <= x, and all e in
        a[i:] have e > x.  So if x already appears in the list, a.insert(i, x) will
        【insert】 just 【after】 the rightmost x already there.        
上述左右边界查找方法，当target不存在时，返回合适的插入位而不是题中的-1
当target存在时，返回左闭右开区间[left,right)，即左边界为target第一次出现的位置，右边界为target最后一次出现的位置+1.        
"""
class Solution:
    def left_bound(self, nums: List[int], target: int) -> int:
        if len(nums) == 0: return -1

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                right = mid - 1  # 收缩右边界确定左边界，mid=right+1
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1

        # mid=right+1的越界判断：
        if right + 1 > len(nums) - 1: return -1
        return left if nums[left] == target else -1

    def right_bound(self, nums: List[int], target: int) -> int:
        if len(nums) == 0: return -1

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                left = mid + 1  # 扩大左边界确定右边界，mid=left-1
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1

        # mid=left-1的越界判断：
        if left - 1 < 0: return -1
        return right if nums[right] == target else -1

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.left_bound(nums, target)
        right = self.right_bound(nums, target)

        return [left, right]

    def searchRange_stl(self, nums: List[int], target: int) -> List[int]:
        left = bisect.bisect_left(nums, target)
        right = bisect.bisect_right(nums, target)
        return [left, right - 1]


def main():
    # 输入：nums = [5,7,7,8,8,10], target = 8
    # 输出：[3,4]
    solution1 = Solution()
    print(solution1.searchRange(nums=[5, 7, 7, 8, 8, 10], target=8))

    # 输入：nums = [5,7,7,8,8,10], target = 6
    # 输出：[-1,-1]
    solution2 = Solution()
    print(solution2.searchRange(nums=[5, 7, 7, 8, 8, 10], target=6))

    # 输入：nums = [], target = 0
    # 输出：[-1,-1]
    solution3 = Solution()
    print(solution3.searchRange(nums=[], target=0))

    # 输入
    # [5,7,7,8,8,10]
    # 6
    # 输出
    # [1,0]
    # 预期结果
    # [-1,-1]
    solution4 = Solution()
    print(solution4.searchRange(nums=[5, 7, 7, 8, 8, 10], target=6))

    # 输入
    # [2,2]
    # 3
    solution4 = Solution()
    print(solution4.searchRange(nums=[2, 2], target=3))


if __name__ == '__main__':
    main()
