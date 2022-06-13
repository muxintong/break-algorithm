'''
NOTE:循坏内直接去重nSum2的：针对第一个元素去重目前不对，待修改。
'''
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[List[int]]:
        left = 0
        right = len(nums) - 1
        res = []
        while left < right:
            sum = nums[left] + nums[right]
            if sum == target:
                res.append([nums[left], nums[right]])
                left += 1
                right -= 1
            elif sum < target:
                left += 1
            else:
                right -= 1

        if res:
            unique_res_tuple = list(set([tuple(t) for t in res]))
            unique_res_list = [list(member) for member in unique_res_tuple]
            return unique_res_list
        return res

    def threeSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        for i in range(len(nums)):
            list2s = self.twoSum(nums[i + 1:len(nums)], target - nums[i])
            if list2s:
                for list2 in list2s:
                    list2.append(nums[i])
                    res.append(list2)

        if res:
            unique_res_tuple = list(set([tuple(t) for t in res]))
            unique_res_list = [list(member) for member in unique_res_tuple]
            return unique_res_list
        return res

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()

        res = []
        for i in range(len(nums)):
            list3s = self.threeSum(nums[i + 1:len(nums)], target - nums[i])
            if list3s:
                for list3 in list3s:
                    list3.append(nums[i])
                    res.append(list3)

        if res:
            unique_res_tuple = list(set([tuple(t) for t in res]))
            unique_res_list = [list(member) for member in unique_res_tuple]
            return unique_res_list
        return res

    # 针对结果集中无重复元素这一限制：使用内置方法set()去重
    def nSum(self, nums: List[int], target: int, n: int) -> List[List[int]]:
        nums.sort()

        res = []
        # base case
        if n < 2 or len(nums) < n: return res
        if n == 2:
            left = 0
            right = len(nums) - 1
            while left < right:
                sum = nums[left] + nums[right]
                if sum == target:
                    res.append([nums[left], nums[right]])
                    left += 1
                    right -= 1
                elif sum < target:
                    left += 1
                else:
                    right -= 1

        # recursive
        for i in range(len(nums)):
            sub_nSums = self.nSum(nums[i + 1:len(nums)], target - nums[i], n - 1)
            if sub_nSums:
                for sub_nSum in sub_nSums:
                    sub_nSum.append(nums[i])
                    res.append(sub_nSum)

        if res:
            unique_res_tuple = list(set([tuple(t) for t in res]))
            unique_res_list = [list(member) for member in unique_res_tuple]
            return unique_res_list
        return res

    # 针对结果集中无重复元素这一限制：在左右指针移动时使用循环跳过所有相同元素 + 对传入的第一个元素去重
    def nSum2(self, nums: List[int], target: int, n: int) -> List[List[int]]:
        nums.sort()

        res = []
        # base case
        if n < 2 or len(nums) < n: return res
        if n == 2:
            left = 0
            right = len(nums) - 1
            while left < right:
                sum = nums[left] + nums[right]
                left_val = nums[left]
                right_val = nums[right]
                if sum == target:
                    res.append([nums[left], nums[right]])
                    # NOTE：
                    # 由于数组已经排序，若要保证结果集无重复，则在左右指针移动时跳过所有相同元素即可
                    # 此时还需保证在移动过程中left指针不能超越right
                    while left < right and nums[left] == left_val: left += 1
                    while left < right and nums[right] == right_val: right -= 1
                elif sum < target:
                    while left < right and nums[left] == left_val: left += 1
                else:
                    while left < right and nums[right] == right_val: right -= 1

        # recursive
        for i in range(len(nums)):
            sub_nSums = self.nSum(nums[i + 1:len(nums)], target - nums[i], n - 1)
            if sub_nSums:
                for sub_nSum in sub_nSums:
                    sub_nSum.append(nums[i])
                    res.append(sub_nSum)

            # keypoint：不能让第一个数i重复，至于后面的数，复用的 nSum 函数会保证它们不重复。
            # 所以代码中必须用一个 while 循环来保证 nSum 中第一个元素i不重复。
            # while nums[i] == nums[i + 1] and i < len(nums) - 1: i += 1
            # NOTE：and条件下，若涉及数组【指针移动】及【指针越界判断】，需将【指针越界判断】置于最前面
            # ！！！指针移动之前必须进行越界判断！！！
            while i < len(nums) - 1 and nums[i] == nums[i + 1]:
                i += 1
                # 针对列表内所有元素均相同这一特殊情况:目前不对待改正
                # if i == len(nums) - 1: return res

        return res


def main():
    # -------------------------nSum------------------------------ #
    # Input: nums = [1,0,-1,0,-2,2], target = 0
    # Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
    nSum_solution1 = Solution()
    print(nSum_solution1.nSum(nums=[1, 0, -1, 0, -2, 2], target=0, n=4))

    # Input: nums = [2,2,2,2,2], target = 8
    # Output: [[2,2,2,2]]
    fourSum_solution2 = Solution()
    print(fourSum_solution2.nSum(nums=[1, 1, 3, 2, 2, 2, 2, 2, 2], target=8, n=4))

    # --------------------------------------------------------------- #


if __name__ == '__main__':
    main()
