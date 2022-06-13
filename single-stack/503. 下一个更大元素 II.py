from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [-1] * n
        stack = nums[::-1]
        for i in range(n - 1, -1, -1):
            while stack and stack[-1] <= nums[i]:
                stack.pop()
            if stack:
                res[i] = stack[-1]
            stack.append(nums[i])
        return res

def main():
    # 输入: nums = [1,2,1]
    # 输出: [2,-1,2]
    # 解释: 第一个 1 的下一个更大的数是 2；
    # 数字 2 找不到下一个更大的数；
    # 第二个 1 的下一个最大的数需要循环搜索，结果也是 2。
    # solution1 = Solution()
    # print(solution1.nextGreaterElements([1,2,1]))

    print('---')

    # 输入: nums = [1,2,3,4,3]
    # 输出: [2,3,4,-1,4]
    solution2 = Solution()
    print(solution2.nextGreaterElements([1,2,3,4,3]))


if __name__ == '__main__':
    main()
