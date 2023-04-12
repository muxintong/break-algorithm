"""
给你一个整数数组 nums 和两个整数 k 和 t 。
请你判断是否存在 两个不同下标 i 和 j，使得 abs(nums[i] - nums[j]) <= t ，同时又满足 abs(i - j) <= k 。

如果存在则返回 true，不存在返回 false。
"""
from typing import List


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        i = 0
        j = 0
        while j < len(nums) - 1:
            j += 1
            if nums[i] == nums[j] and abs(nums[i] - nums[j]) <= valueDiff and abs(i - j) <= indexDiff: return True

            while j - i >= indexDiff and i < j:
                i += 1
                if nums[i] == nums[j] and i != j and abs(nums[i] - nums[j]) <= valueDiff and abs(i - j) <= indexDiff:
                    return True

        return False


def main():
    # 输入：nums = [1,2,3,1], k = 3, t = 0
    # 输出：true
    solution1 = Solution()
    print(solution1.containsNearbyAlmostDuplicate([1, 2, 3, 1], 3, 0))

    # 输入：nums = [1,0,1,1], k = 1, t = 2
    # 输出：true
    solution2 = Solution()
    print(solution2.containsNearbyAlmostDuplicate([1, 0, 1, 1], 1, 2))

    # 输入：nums = [1,5,9,1,5,9], k = 2, t = 3
    # 输出：false
    solution3 = Solution()
    print(solution3.containsNearbyAlmostDuplicate([1, 5, 9, 1, 5, 9], 2, 3))


if __name__ == '__main__':
    main()
