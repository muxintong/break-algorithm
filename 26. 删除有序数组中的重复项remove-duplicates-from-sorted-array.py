from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        slow = 0
        fast = 0
        while fast < len(nums):
            if nums[fast] != nums[slow]:
                slow += 1
                # 保持nums[0-slow]无重复
                nums[slow] = nums[fast]

            fast += 1

        return slow + 1


def main():
    # Input: nums = [1,1,2]
    # Output: 2, nums = [1,2,_]
    solution1=Solution()
    print(solution1.removeDuplicates([1,1,2]))

    # Input: nums = [1,1,2]
    # Output: 2, nums = [1,2,_]
    solution1=Solution()
    print(solution1.removeDuplicates([1,1,2]))


if __name__=='__main__':
    main()
