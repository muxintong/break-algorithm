from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[List[int]]:
        # 1.sort：由于外层传入时已经排好序,若无外层，此时需先排序
        nums.sort()

        # 2.left-right pointer
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
            # 对结果集res：二维list去重
            unique_res_tuple = list(set([tuple(t) for t in res]))
            # >>> lists1
            # [(1, 8), (2, 7)]
            # >>> lists1=[list(list1) for list1 in lists1]
            # >>> lists1
            # [[1, 8], [2, 7]]
            #
            # NOTE：转换后为list[(tuple), ...]形式，还需将内层tuple在转为list
            unique_res_list = [list(member) for member in unique_res_tuple]
            return unique_res_list
        return res

    def threeSum(self, nums: List[int], target: int) -> List[List[int]]:
        # 1.sort
        nums.sort()

        # 2.调用twoSum
        res = []
        for i in range(len(nums)):
            list2s = self.twoSum(nums[i + 1:len(nums)], target - nums[i])
            if list2s:
                for list2 in list2s:
                    list2.append(nums[i])
                    res.append(list2)

        if res:
            # 对二维list去重：
            unique_res_tuple = list(set([tuple(t) for t in res]))
            # 将内层tuple元组转为list：
            unique_res_list = [list(member) for member in unique_res_tuple]
            return unique_res_list
        return res


def main():
    # -------------------------threeSum------------------------------ #
    # Input: nums = [-1,0,1,2,-1,-4], target=0
    # Output: [[-1,-1,2],[-1,0,1]]
    threeSum_solution1 = Solution()
    print(threeSum_solution1.threeSum(nums=[-1, 0, 1, 2, -1, -4], target=0))

    # Input: nums = [], target=0
    # Output: []
    threeSum_solution2 = Solution()
    print(threeSum_solution2.threeSum(nums=[], target=0))

    # Input: nums = [0], target=0
    # Output: []
    threeSum_solution3 = Solution()
    print(threeSum_solution3.threeSum(nums=[0], target=0))


if __name__ == '__main__':
    main()
