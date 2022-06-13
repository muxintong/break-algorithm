
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        slow = 0
        fast = 0

        # NOTE:结束条件！！！结束条件需为fast可以取到列表最后一个元素
        while fast <= len(nums) - 1:
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1

        # if slow == 0: return 1, nums[0]
        return slow, nums[0:slow]


def main():
    # Input: nums = [3,2,2,3], val = 3
    # Output: 2, nums = [2,2,_,_]
    solution1 = Solution()
    print(solution1.removeElement([3, 2, 2, 3], 3))

    # Input: nums = [0,1,2,2,3,0,4,2], val = 2
    # Output: 5, nums = [0,1,4,0,3,_,_,_]
    solution2 = Solution()
    print(solution2.removeElement([0, 1, 2, 2, 3, 0, 4, 2], val=2))

    # Input: nums = [2], val = 3
    # Output: [2]
    #
    # while fast < len(nums) - 1:
    # (0, []) 错
    # while fast < len(nums):
    # (1, [2]) 对
    solution3 = Solution()
    print(solution3.removeElement([2], val=3))


if __name__ == '__main__':
    main()
