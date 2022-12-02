from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0: return -1

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1

        return -1


def main():
    # 输入: nums = [-1,0,3,5,9,12], target = 9
    # 输出: 4
    # 解释: 9 出现在 nums 中并且下标为 4
    solution1 = Solution()
    print(solution1.search(nums=[-1, 0, 3, 5, 9, 12], target=9))

    # 输入: nums = [-1,0,3,5,9,12], target = 2
    # 输出: -1
    # 解释: 2 不存在 nums 中因此返回 -1
    solution2 = Solution()
    print(solution2.search(nums=[-1, 0, 3, 5, 9, 12], target=2))


if __name__ == '__main__':
    main()
