from typing import List


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(0, len(nums)):
            counts = 0
            for j in range(i, len(nums)):
                if nums[j] < nums[i]: counts += 1
            res.append(counts)

        return res


def main():
    # 输入：nums = [5,2,6,1]
    # 输出：[2,1,1,0]
    # 解释：
    # 5 的右侧有 2 个更小的元素 (2 和 1)
    # 2 的右侧仅有 1 个更小的元素 (1)
    # 6 的右侧有 1 个更小的元素 (1)
    # 1 的右侧有 0 个更小的元素
    solution1 = Solution()
    print(solution1.countSmaller(nums=[5, 2, 6, 1]))

    # 输入：nums = [-1]
    # 输出：[0]
    solution1 = Solution()
    print(solution1.countSmaller(nums=[-1]))

    # 输入：nums = [-1,-1]
    # 输出：[0,0]
    solution1 = Solution()
    print(solution1.countSmaller(nums=[-1, -1]))


if __name__ == '__main__':
    main()
