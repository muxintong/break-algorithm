from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 调用removeElement方法：去除nums中的所有0，返回去除0之后的数组长度
        len_no_zero = self.removeElement(nums, 0)
        # 将len_no_zero之后的所有元素赋值为0
        while len_no_zero < len(nums):
            nums[len_no_zero] = 0
            len_no_zero += 1

        for num in nums:
            print(num)


    def removeElement(self, nums: List[int], val: int) -> int:
        slow = 0
        fast = 0

        while fast <= len(nums) - 1:
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1

        return slow


def main():
    # 输入: nums = [0,1,0,3,12]
    # 输出: [1,3,12,0,0]
    solution1 = Solution()
    solution1.moveZeroes(nums=[0, 1, 0, 3, 12])
    print('---')

    # 输入: nums = [0]
    # 输出: [0]
    solution2 = Solution()
    solution2.moveZeroes(nums = [0])

if __name__ == '__main__':
    main()
